#!/usr/bin/env bash
# Explicit server-first production bootstrap, invoked by the release owner only.
# Run AFTER installing server/install.sh and loading the checked ARM64 image.
set -euo pipefail
umask 077
[[ $EUID == 0 ]] || { echo 'Run with sudo.' >&2; exit 1; }
revision=${1:?Expected full source SHA}
identity=${2:?Expected local Docker image ID}
[[ $revision =~ ^[0-9a-f]{40}$ ]]
[[ $identity =~ ^sha256:[0-9a-f]{64}$ ]]
slug=johnny-dee-s-lounge
root=/opt/$slug
state=/var/lib/$slug-deploy
alias="$slug-bootstrap:$revision"
source=https://github.com/xsolutionsmd/johnny-dee-s-lounge
[[ -d $root && -d $state && ! -L $root && ! -L $state ]]
exec 9>"$state/update.lock"
flock -w 30 9
! systemctl is-active --quiet "$slug-update.timer"
! systemctl is-active --quiet "$slug-update.service"
for path in "$root/compose.yaml" "$root/release.env" "$state/current.json" "$state/transaction" "$state/bootstrap.json"; do
  [[ ! -e $path && ! -L $path ]] || { echo "Existing state; inspect before retry: $path" >&2; exit 1; }
done
[[ -z $(docker ps -aq --filter "label=com.docker.compose.project=$slug") ]]
docker network inspect xsolutions-proxy >/dev/null
[[ $(docker image inspect "$alias" --format '{{.Id}}') == "$identity" ]]
[[ $(docker image inspect "$identity" --format '{{.Architecture}}') == arm64 ]]
[[ $(docker image inspect "$identity" --format '{{.Os}}') == linux ]]
[[ $(docker image inspect "$identity" --format '{{index .Config.Labels "org.opencontainers.image.revision"}}') == "$revision" ]]
[[ $(docker image inspect "$identity" --format '{{index .Config.Labels "org.opencontainers.image.source"}}') == "$source" ]]
compose=(docker compose --project-name "$slug" --project-directory "$root" --env-file "$root/release.env" -f "$root/compose.yaml")
started=false
complete=false
cleanup() {
  status=$?
  trap - EXIT
  if [[ $started == true && $complete != true ]]; then
    # Never remove a sibling or volume. Preserve failed recovery for inspection.
    if "${compose[@]}" rm --stop --force web; then
      rm -f -- "$root/compose.yaml" "$root/release.env" "$state/transaction"
    else
      echo "Recovery failed; preserve $state/transaction and runtime files." >&2
    fi
  fi
  exit "$status"
}
trap cleanup EXIT
trap 'exit 143' TERM
trap 'exit 130' INT
printf '%s\n' 'direct-bootstrap; inspect runtime and bootstrap.json before clearing' > "$state/transaction"
sync -f "$state/transaction"
started=true
install -m 644 "/usr/local/share/$slug/compose.yaml" "$root/compose.yaml"
# A real tag survives docker save/load and Compose rollback; no registry digest is fabricated.
printf 'APP_IMAGE=%s\n' "$alias" > "$root/release.env"
chmod 600 "$root/release.env"
"${compose[@]}" config --quiet
"${compose[@]}" up -d --no-build --pull never --wait --wait-timeout 90
cid=$("${compose[@]}" ps -q web)
[[ $(docker inspect "$cid" --format '{{.Image}}') == "$identity" ]]
actual=$(docker exec "$cid" wget -qO- http://127.0.0.1:8080/version.json)
python3 -c 'import json,sys; assert json.loads(sys.argv[1])["revision"] == sys.argv[2]' "$actual" "$revision"
docker exec "$cid" wget -qO- http://127.0.0.1:8080/ | python3 -c 'import sys; s=sys.stdin.read(); assert s.strip(); assert "website in progress" not in s.lower()'
python3 - "$state/bootstrap.json" "$revision" "$identity" "$alias" "$cid" <<'PY'
import datetime,json,sys
from pathlib import Path
Path(sys.argv[1]).write_text(json.dumps(dict(mode='direct-bootstrap',status='origin-healthy-awaiting-https',revision=sys.argv[2],image_id=sys.argv[3],image_alias=sys.argv[4],container=sys.argv[5],observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n')
PY
sync -f "$state/bootstrap.json"
complete=true
rm -f -- "$state/transaction"
echo "Origin healthy: $revision; publish the scoped Caddy route next. Updater remains paused."
