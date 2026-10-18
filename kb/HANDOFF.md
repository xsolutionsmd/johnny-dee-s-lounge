# Handoff

<!-- xs-status:start -->
Pipeline status (generated 2026-10-18T00:55:17.708530+00:00):

- **identity**: done
- **research**: done
- **spec**: done
- **assets**: done
- **delivery**: done
- **infra**: done
- **template**: done
- **build**: done
- **deploy**: todo: functional acceptance: every live row in kb/features.md ## Acceptance must pass (0/1 passing; at least one required)
<!-- xs-status:end -->

## Current state

Workflow: speed-first. Four real pages `/`, `/menu/`, `/catering/`, `/visit/`.
Repository: https://github.com/xsolutionsmd/johnny-dee-s-lounge.
The initial direct server release preceded GitHub/Actions, as requested. GitHub now
has main, derek-dev and abdul-dev, independent release workflows and environments.
PR2 published the visible reference-led correction at5e719dc to allthree environments.
This source also includes Astra's scoped follow-up to the sole Sol finding.

- Production: https://johnny-dee-s-lounge.xsolutionsmd.com
- Derek preview: https://johnny-dee-s-lounge-derek-dev.xsolutionsmd.com
- Abdul preview: https://johnny-dee-s-lounge-abdul-dev.xsolutionsmd.com
- Actions: https://github.com/xsolutionsmd/johnny-dee-s-lounge/actions

Each `/version.json` is the authoritative current deployed revision. Changes go
through the protected-main PR route; main is synced back to both previews.

## Reference, authentic assets and review

The first release lacked an inspected template. Astra then selected Joe Allen
from three inspected live candidates after deciding the menu/contact/directions
scope from research. Minetta supplies only the observed mobile tel behavior
missing from Joe Allen. Captures and concrete component/type/spacing notes went
to Claude. Exact flow mapping and rationale are in features.md and design-brief.md.

The actual site now has the real tankard logo, photo-led Home, genuine food
collage on Home/Menu, balanced navigation, restrained menu sheets and one authored
Instrument Sans family. The two official images are owner-approved under Derek's
standing instruction; media.md records provenance and actual page mapping.
Private originals and operational/commercial records stay outside this repository.

Sol inspected the released four pages on desktop and phone against the reference.
It confirmed a coherent professional result with actual assets and consistent
fonts; the low-resolution collage cannot reproduce a full photographic panorama.
The sole P3 was a desktop Catering label offset. Astra top-aligned those rows,
checked matching heading/separator positions and unchanged phone containment,
and passed the final build. No visual finding remains deferred.

## Verification and continuation

First corrective release5e719dc: all12route/environment combinations returned200
twice, allsix CI/release runs passed, actual production browser direct loads and
reloads passed. Filters, mobile nav/Escape, active pages, native history, sourced
phone/Maps/Facebook actions, real images and320px Visit containment were checked.
The final one-rule Catering fix passed targeted desktop/phone inspection and
production/static check. docs/VALIDATION.md records the review and check scope.

Use Actions and `/version.json` to check the current release; the reproducible
`scripts/verify-pages.py BASE_URL --revision SHA` proves every direct route/refresh.
The private checkpoint owns exact rollout receipts, screenshots, Slack milestones
and disposable cleanup. Future substantive changes require their own authorization.

## Remaining owner content

Current full menu/prices, confirmed daily hours and catering terms/capacity.
Higher-resolution food/interior photography would improve the image quality.
Six sourced dish examples and listed hours remain qualified. Phone, Maps and
Facebook are real destinations; no ordering, reservations or form delivery is
simulated. Asset permission is no longer pending.
