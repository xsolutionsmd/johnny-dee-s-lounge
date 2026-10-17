# Oracle deployment

This generated contract is for one **stateless** HTTP image listening on `0.0.0.0:8080`, with Docker HEALTHCHECK and an uncached `/version.json` returning the exact build `revision`. Dockerfile accepts `REVISION` (or `APP_REVISION`) and `APP_SOURCE_URL`; labels must identify `https://github.com/xsolutionsmd/johnny-dee-s-lounge` and that revision. The runtime uses a read-only root and disposable `/tmp`, `/data`, `/config`; persistent user data requires an adapted stateful deployment, not this template.

Work on your personal preview branch (`derek-dev` or `abdul-dev`); its own workflow publishes only that preview. PRs into main check only. Merge the authorized preview-to-main PR to publish production. There is no shared dev branch. Only `oracle-release.yml` publishes production; each preview has its own independent publisher.

## Initial server-first bootstrap

For the initial launch, publish the reviewed real site on Oracle before creating/pushing the GitHub repository. Do not publish the scaffold placeholder. The release owner first commits the reviewed source locally and builds a checked `linux/arm64` image labelled with the full source SHA and source URL above. Tag it `johnny-dee-s-lounge-bootstrap:<SHA>`, transfer it with `docker save`, verify the transfer checksum, and `docker load` it on Oracle. This tag is deliberately outside the registered GHCR image repository and needs manual recovery-aware retirement later.

Upload only `server/`, `deploy/`, and `compose.production.yaml` to a unique staging directory. Run the generated `server/install.sh`; do not enable the app updater. Run `sudo bash server/bootstrap-direct.sh <SHA> <sha256:image-id>`. It verifies labels/architecture, starts the generated production Compose with `APP_IMAGE=johnny-dee-s-lounge-bootstrap:<SHA>` and `--pull never`, checks origin health/content/revision, and writes a separate `bootstrap.json`. It does not fabricate `current.json` or a registry digest. A failed/incomplete attempt requires inspecting its transaction/runtime files before retrying.

Read the current installed Caddyfile and SHA256 immediately before route publication. Run `sudo python3 deploy/add-oracle-route.py --expected-sha <fresh-Caddyfile-SHA256> --revision <source-SHA>`. This adds only the production route under `/run/lock/xsolutions-gateway.lock`, validates a staged file, refuses stale content, reloads gracefully, and checks HTTPS/noindex/revision and unchanged container identities. Rollback refuses to overwrite a concurrent gateway edit. All concurrent gateway writers must use that shared lock. The script never uploads a stale full gateway snapshot. Save the same scoped route in canonical gateway source after checking its current content; do not replace it wholesale from an older copy.

Only after production HTTPS and the real page are verified should the release owner create the repository, environments and branches, then publish Actions releases. Install each preview with its generated installer. Before its first release, use the route helper with `--environment <branch> --prepare-preview --expected-sha <fresh-hash> --revision <branch-SHA>`; this records route preparation, not a live preview. Enable only this company's app timers when the public repository/manifest prerequisites are ready. The first normal production updater replaces the local alias with the registry digest, preserving the bootstrap Compose/env for recovery; its verified release creates `current.json`. Retain the bootstrap tag while current runtime or `previous.env` refers to it, and recheck after the next successful replacement.

The generic first-installation steps below describe the normal GitHub-backed release path after that explicit initial bootstrap. These files are preparation until actually installed and verified.

## First installation

1. Verify unique `johnny-dee-s-lounge` project/network alias and unused `johnny-dee-s-lounge.xsolutionsmd.com`; inspect current server and gateway first. Set repository variable `ORACLE_HOST` to the verified Oracle IPv4. Make this repo's release assets and GHCR image `ghcr.io/xsolutionsmd/johnny-dee-s-lounge` accessible to anonymous pulls. **Do not make private code/images public** to fit this template; prepare authenticated discovery/pulls instead. Configure PR/required checks on main (`Check deployable app` and app checks) and main-only production environment, then observe actual dev-push and PR events.
2. Review generated files, including `server/retention/app.json`. Upload a focused copy to the server and run `sudo bash server/install.sh`. This leaves a new **application updater** timer paused and preserves an existing app timer's running state. It also registers the app with the shared automatic image-retention service and enables that service's hourly timer. Installer changes are separate administrator deployments; source-image releases never install root-owned scripts.
3. Back up gateway config; add only `deploy/oracle.caddy` to canonical and installed gateway source. Validate and gracefully reload the current gateway. DNS must point to Oracle. For an unused hostname this can precede the first image so final HTTPS verification can succeed. For occupied traffic, stage a healthy replacement before switching it.
4. Enable `sudo systemctl enable --now johnny-dee-s-lounge-update.timer`, merge the checked authorized main release, observe the main-push Actions run, then independently verify HTTPS and `/version.json` plus existing apps. The server uses outbound public downloads; no GitHub SSH credential is needed.

## One-command operations

- Manual publication/deployment of current main: `gh workflow run oracle-release.yml --ref main --repo xsolutionsmd/johnny-dee-s-lounge`. Rebuilding the same commit may produce the same image; an identical applied digest is an intentional no-op. Manual dev deployment needs its own isolated environment, never this production timer.
- Check/apply the currently approved release now: `sudo systemctl start johnny-dee-s-lounge-update.service`.
- Status: `sudo systemctl status johnny-dee-s-lounge-update.timer`; logs: `sudo journalctl -u johnny-dee-s-lounge-update.service -n 60 --no-pager`.
- Current image/revision: `sudo cat /var/lib/johnny-dee-s-lounge-deploy/current.json`.
- Persistently pause/resume: `sudo systemctl disable --now johnny-dee-s-lounge-update.timer` / `sudo systemctl enable --now johnny-dee-s-lounge-update.timer`.

## Automatic image retention

The installer copies the self-contained files in `server/retention/` to a shared root-owned image-retention installation and attaches a successful-update observer to `johnny-dee-s-lounge-update.service`. The shared hourly timer starts automatically; it needs no Codex task or further prompt. Configuration keeps the running release and two previous successfully observed, distinct image sets. It waits until three successful image sets are known before deleting anything for this app; simply finding an old downloaded image does not prove a successful release.

Deletion is limited to this registration's exact image repository, with a 24-hour grace period from the cleanup system's first observation of each local image. Running and stopped containers, retained successful images, recovery references and fresh candidates remain protected. Pending deployment/recovery evidence pauses deletion. Volumes, networks and unrelated images are outside this cleanup. Retained application images are not database backups, and automatic image cleanup is not a total disk-space quota; logs, user data and protected images may still grow.

A failed release observer creates `/var/lib/app-launchpad/image-retention/johnny-dee-s-lounge.uncertain` and blocks cleanup for this app until its successful history is reconciled. Preserve this marker while investigating. The installer refuses to downgrade or silently replace a different shared cleanup policy at the same version; update the reviewed shared policy version deliberately when changing it.

Status: `sudo systemctl status app-launchpad-image-retention.timer`; logs: `sudo journalctl -u app-launchpad-image-retention.service -n 60 --no-pager`; inspect a deletion plan without deleting images: `sudo app-image-retention plan`. The app's registration and update observer are installed separately from its release image, so app code cannot replace the root-owned cleanup engine.

## Recovery and maintenance

State is `/var/lib/johnny-dee-s-lounge-deploy`; runtime is `/opt/johnny-dee-s-lounge`; reviewed templates are `/usr/local/share/johnny-dee-s-lounge`. Replacements can briefly interrupt this app. Candidate failures preserve the running app; handled replacement/TLS/state failures restore prior Compose/image/state. A failed first deployment removes only its own unsuccessful service. Failed recovery keeps evidence. A `transaction` file after an unhandled kill/reboot blocks later updates; inspect its named `check.*` directory, prior Compose/env/current metadata, and actual container before a deliberate recovery. Do not simply delete the guard and retry. Automatic recovery from power loss is not promised.

Code rollback normally reverts the change on dev and publishes a checked corrective main commit. Back up app config/release state and gateway certificates to independent storage; the existing same-disk server backup does not automatically cover this app. Never use global prune or `down -v` for app repair.

For approved disposal of this app only: disable its timer, stop its service, remove its Caddy block from canonical/installed source and validate/reload, stop/remove only Compose project `johnny-dee-s-lounge`, and remove precisely its root-owned updater/unit/template/runtime/state files after verifying their paths and retaining any needed evidence. Unregister this app's retention configuration and observer when removing its updater; preserve the shared retention timer/engine for other registrations. Remove only its explicitly identified image tags, package and scratch repository when authorized. Preserve the shared gateway/network/certificates and all unrelated apps.

## Personal preview environments

This repository uses `main` for production plus long-lived personal preview branches; there is no shared `dev` branch, so the production workflow checks main pushes and PRs into main. Each preview is a fully separate stack: its own branch-scoped workflow, GHCR package, prerelease tags (`<branch>-<sha>`), Compose project, `/opt`, `/var/lib/...-deploy` and `/usr/local/share` paths, updater timer, retention registration and Caddy route. A preview publication never becomes the latest GitHub release and never changes production.

| Branch | Hostname | Slug / alias | Image | Workflow |
|---|---|---|---|---|
| `derek-dev` | `johnny-dee-s-lounge-derek-dev.xsolutionsmd.com` | `johnny-dee-s-lounge-derek-dev` | `ghcr.io/xsolutionsmd/johnny-dee-s-lounge-derek-dev` | `.github/workflows/oracle-derek-dev.yml` |
| `abdul-dev` | `johnny-dee-s-lounge-abdul-dev.xsolutionsmd.com` | `johnny-dee-s-lounge-abdul-dev` | `ghcr.io/xsolutionsmd/johnny-dee-s-lounge-abdul-dev` | `.github/workflows/oracle-abdul-dev.yml` |

Work on your own preview branch (directly or through feature-branch PRs into it); each push to it publishes and deploys only that preview. Promote with a reviewed PR from a preview branch into `main`. After each production release, merge `main` back into every preview branch so they do not drift.

Setup per preview, following production's first-installation steps: create the branch from main, create a GitHub environment with the same name restricted to that branch, make its GHCR package anonymously pullable under the same visibility rule as production, run `sudo bash server/<branch>/install.sh`, add `deploy/oracle-<branch>.caddy` to the gateway, validate and reload, then `sudo systemctl enable --now <slug>-update.timer`. Compose exports `APP_ENVIRONMENT`; previews should serve `noindex` and use only test data and test integrations.
