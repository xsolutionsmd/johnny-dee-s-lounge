#!/usr/bin/env python3
"""Explicitly add one Johnny Dee route using a fresh hash and shared gateway lock.

Run as root on Oracle, with --expected-sha from an immediate fresh server read.
Never upload a full Caddyfile from the workstation. No operation occurs on import.
"""
import argparse
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

SLUG = 'johnny-dee-s-lounge'
GATEWAY = Path('/opt/xsolutions-gateway/config/Caddyfile')
COMPOSE = ['docker', 'compose', '-f', '/opt/xsolutions-gateway/compose.yaml', 'exec', '-T', 'caddy', 'caddy']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def additive(before, slug):
    host = slug + '.xsolutionsmd.com'
    if host.encode() in before or re.search(rb'\b' + slug.encode() + rb':8080\b', before):
        raise ValueError('Hostname/upstream already present; inspect ownership instead of adding again')
    block = f'\n{host} {{\n    reverse_proxy {slug}:8080\n}}\n'.encode()
    return before + (b'' if before.endswith(b'\n') else b'\n') + block


def compare_replace(path, expected, replacement):
    # Shared flock serializes cooperating writers; the fresh hash refuses stale input.
    if path.is_symlink() or path.read_bytes() != expected:
        raise RuntimeError('Caddyfile changed concurrently; refusing overwrite')
    os.replace(replacement, path)


def run(args):
    return subprocess.run(args, check=True, text=True, capture_output=True, timeout=45).stdout.strip()


def containers():
    ids = run(['docker', 'ps', '-aq']).split()
    return {c['Id']: {'name':c['Name'], 'image':c['Image']} for c in json.loads(run(['docker', 'inspect', *ids]))}


def verify(host, revision):
    url = 'https://' + host
    args = ['curl', '-fsS', '--connect-timeout', '5', '--max-time', '10', '--resolve', host + ':443:127.0.0.1']
    actual = json.loads(run([*args, url + '/version.json']))['revision']
    if actual != revision:
        raise RuntimeError('Live revision differs from selected source SHA')
    headers = run([*args, '-I', url + '/'])
    if 'noindex' not in headers.lower() or not run([*args, url + '/']):
        raise RuntimeError('Expected nonempty noindex site')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--environment', choices=['production','derek-dev','abdul-dev'], default='production')
    parser.add_argument('--expected-sha', required=True)
    parser.add_argument('--revision', required=True)
    parser.add_argument('--prepare-preview', action='store_true', help='Install an unused preview route before its first updater release; does not claim a live preview')
    args = parser.parse_args()
    if os.geteuid() != 0 or not re.fullmatch('[0-9a-f]{64}', args.expected_sha) or not re.fullmatch('[0-9a-f]{40}', args.revision):
        parser.error('Root, a full gateway SHA256 and a full source SHA are required')
    if args.prepare_preview and args.environment == 'production':
        parser.error('Production bootstrap requires a healthy reviewed origin')
    slug = SLUG + ('' if args.environment == 'production' else '-' + args.environment)
    host = slug + '.xsolutionsmd.com'
    with open('/var/lock/xsolutions-gateway.lock', 'a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        before = GATEWAY.read_bytes()
        if sha(before) != args.expected_sha:
            raise RuntimeError('Fresh Caddy hash no longer matches; reread and review')
        after = additive(before, slug)
        siblings = containers()
        # Production is healthy before publication; unused previews may await CI.
        if not args.prepare_preview:
            cid = run(['docker', 'ps', '-q', '--filter', 'label=com.docker.compose.project=' + slug, '--filter', 'label=com.docker.compose.service=web'])
            if not cid or '\n' in cid:
                raise RuntimeError('Expected exactly one scoped origin')
            if run(['docker', 'inspect', cid, '--format', '{{.State.Health.Status}}']) != 'healthy':
                raise RuntimeError('Origin is not healthy')
            version = json.loads(run(['docker', 'exec', cid, 'wget', '-qO-', 'http://127.0.0.1:8080/version.json']))
            if version['revision'] != args.revision:
                raise RuntimeError('Origin revision differs')
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        backup = GATEWAY.with_name('Caddyfile.before-' + slug + '-' + stamp)
        with backup.open('xb') as stream:
            stream.write(before)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(backup, 0o600)
        fd, filename = tempfile.mkstemp(prefix='.Caddyfile-' + slug + '-', dir=GATEWAY.parent)
        candidate = Path(filename)
        installed = False
        try:
            with os.fdopen(fd, 'wb') as stream:
                stream.write(after)
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(candidate, 0o644)
            run([*COMPOSE, 'validate', '--config', '/etc/caddy/' + candidate.name, '--adapter', 'caddyfile'])
            compare_replace(GATEWAY, before, candidate)
            installed = True
            run([*COMPOSE, 'reload', '--config', '/etc/caddy/Caddyfile', '--adapter', 'caddyfile'])
            error = None
            for attempt in range(0 if args.prepare_preview else 12):
                try:
                    verify(host, args.revision)
                    error = None
                    break
                except (subprocess.SubprocessError, ValueError, KeyError, RuntimeError) as problem:
                    error = problem
                    time.sleep(2)
            if error:
                raise error
            if siblings != containers():
                raise RuntimeError('Container inventory changed during gateway update; inspect concurrent releases')
            receipt = {'host':host,'revision':args.revision,'status':'route-prepared-awaiting-updater' if args.prepare_preview else 'https-revision-verified','before_sha256':sha(before),'after_sha256':sha(after),'backup':str(backup),'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'containers_unchanged':True}
            Path('/var/lib/' + slug + '-deploy/gateway-bootstrap.json').write_text(json.dumps(receipt,indent=2)+'\n')
            print(json.dumps(receipt,indent=2))
        except BaseException:
            if installed:
                # Never restore an old snapshot over a later writer's changes.
                if GATEWAY.read_bytes() != after:
                    raise RuntimeError('Gateway changed after our write; refusing stale rollback. Preserve backup: ' + str(backup))
                candidate.write_bytes(before)
                os.chmod(candidate, 0o644)
                compare_replace(GATEWAY, after, candidate)
                run([*COMPOSE, 'reload', '--config', '/etc/caddy/Caddyfile', '--adapter', 'caddyfile'])
            raise
        finally:
            candidate.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
