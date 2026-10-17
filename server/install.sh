#!/usr/bin/env bash
set -euo pipefail
[[ $EUID == 0 ]] || { echo 'Run with sudo on the prepared server.' >&2; exit 1; }
cd "$(dirname "$0")/.."
for command in docker curl git python3 flock timeout sync systemctl; do command -v "$command" >/dev/null; done
docker compose version >/dev/null
docker network inspect xsolutions-proxy >/dev/null
[[ $(uname -m) == aarch64 ]] || { echo 'This installation expects ARM64.' >&2; exit 1; }
for path in /opt/johnny-dee-s-lounge /var/lib/johnny-dee-s-lounge-deploy /usr/local/share/johnny-dee-s-lounge; do
  [[ ! -L "$path" ]] || { echo 'Installation directories must not be symlinks.' >&2; exit 1; }
done
was_active=false
if systemctl is-active --quiet johnny-dee-s-lounge-update.timer; then was_active=true; fi
if systemctl cat johnny-dee-s-lounge-update.timer >/dev/null 2>&1; then systemctl stop johnny-dee-s-lounge-update.timer; fi
if systemctl cat johnny-dee-s-lounge-update.service >/dev/null 2>&1; then systemctl stop johnny-dee-s-lounge-update.service; fi
install -d -o root -g root -m 755 /opt/johnny-dee-s-lounge /usr/local/share/johnny-dee-s-lounge
install -d -o root -g root -m 700 /var/lib/johnny-dee-s-lounge-deploy
# Serialize administrator installation with any directly invoked updater too.
exec 9>/var/lib/johnny-dee-s-lounge-deploy/update.lock
flock -w 120 9
install -o root -g root -m 644 compose.production.yaml /usr/local/share/johnny-dee-s-lounge/compose.yaml
install -o root -g root -m 755 server/update-release.sh /usr/local/sbin/johnny-dee-s-lounge-update
install -o root -g root -m 644 server/johnny-dee-s-lounge-update.service /etc/systemd/system/johnny-dee-s-lounge-update.service
install -o root -g root -m 644 server/johnny-dee-s-lounge-update.timer /etc/systemd/system/johnny-dee-s-lounge-update.timer
# The retention observer and timer use this application's updater lock.
# Release our installation lock before installing the observer and shared timer.
flock -u 9
exec 9>&-
python3 server/retention/install_retention.py --config server/retention/app.json --service johnny-dee-s-lounge-update.service
systemctl daemon-reload
if [[ "$was_active" == true ]]; then systemctl start johnny-dee-s-lounge-update.timer; fi
echo 'Installed johnny-dee-s-lounge runtime and automatic image retention; existing app timer state preserved. For first setup, prepare HTTPS route then enable --now johnny-dee-s-lounge-update.timer.'
