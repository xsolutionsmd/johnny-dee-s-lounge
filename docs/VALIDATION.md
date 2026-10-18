# Validation

2026-10-17, speed-first delivery. Four real documents: `/`, `/menu/`, `/catering/`, `/visit/`. Primary navigation has no section-anchor destinations.

Initial release `eba3440f7952cf754cf52fa9410aa862a2349aa5` was built and tested locally, then published directly to Oracle before GitHub setup. It was subsequently replaced with Actions-built digest-pinned images in all three environments. Six initial CI/release runs passed. The 18 existing sibling containers retained their identities and images and remained healthy.

Checked: production build and static/resource checks; ARM64 read-only Nginx candidate health/version; four distinct pages and one H1 per page; every route loaded twice over HTTPS in all environments; actual production browser direct load/reload of each page; native back/forward; mobile navigation and active states; local menu filters; sourced phone, Maps and Facebook destinations. No real calls, submissions or orders were made. All public environments intentionally carry noindex.

Sol inspected rendered live pages at 1440×900 and 375×812, including full-page scrolling, every main page, mobile navigation and menu filter states. No clipping or rendering blockers were found. Astra addressed three findings in the follow-up source: brighter dark-section labels, centered bounded filtered menu cards, aligned homepage card buttons. Affected desktop/mobile views were inspected and `npm run check` passed. The All menu state restores two columns; single-result cards are centered on desktop and fit phones. All three homepage action bottoms match, and phone controls remain inside their cards.

The release workflow verifies the deployed revision; `scripts/verify-pages.py BASE_URL --revision SHA` checks each route twice, distinct content, noindex and version. Exact current revisions are at each environment's `/version.json` and in GitHub Actions/deployments. Detailed screenshots, operational receipts and Slack delivery history are retained in the private project handoff.

Initial-release limits: no current complete owner-issued menu/prices, current daily hours confirmation or catering terms/capacity. Photo permission was initially unknown and is now confirmed through Derek?s standing instruction. The six menu names are sourced examples. Listed hours carry a phone-confirmation note. That initial design used licensed fonts and original graphics; the current correction replaces it with the approved authentic logo and food collage. No booking, ordering, forms, database or staff-delivery integration is implied. This was a focused Chromium desktop/mobile pass, not exhaustive cross-browser certification.


## Reference-led correction, October 17-18, 2026

Astra selected Joe Allen after inspecting company facts, real assets and existing
menu/contact/directions functions. Desktop/mobile captures and concrete layout,
type, spacing and flow notes went to Claude. The actual four-page implementation
now uses the approved tankard logo, real food collage, photo-led Home, a menu-sheet
layout and one Instrument Sans family. Reference and result were compared at
1440x900 and375x812. Source images keep their proportions and are not enlarged.

Final local production build/static checks passed (11 built files). Astra inspected
all four rendered pages on desktop and phone, image loads and consistent fonts;
Visit also passed320px overflow/control containment. All/Seafood/Classics changed
visible menu groups correctly. Mobile navigation opened, Escape closed/refocused,
and a native Menu-to-Visit navigation plus back/forward restored distinct pages
and active labels. No external calls/orders were made. Home firstview includes
food, identity and actions; three desktop visit actions share a baseline.

First template release5e719dc passed all12 route/environment combinations twice,
exact source versions, noindex and all six push-event CI/release runs. Actual
production browser navigation+reload of every route also passed, with loaded local
media and no horizontal overflow. Gateway bytes were unchanged; all24containers
healthy. The concurrent Charcoal release changed only its own three images.

Fresh Sol High inspected allfour LIVE pages at1440x900/375x812, including lower
sections, mobile nav, menu states and matching reference captures. No blocking
finding. The sole P3 was an11.25px desktop Catering label offset. Astra's one-rule
scoped correction top-aligns the preparation rows at desktop widths. Local heading
tops and row bottoms now match; phone remains one contained column. Final production
check passed11files. No visual finding was deferred. The release workflow verifies
the active revision; use the live version endpoints and scripts/verify-pages.py
for current per-environment evidence.
This section supersedes the initial visual design above, not its historical evidence.


Final corrective release61ee672d465ec770703c019d493cbd428fd28f5c: allthree
origins healthy, exact revision and all12page/environment combinations returned
200 twice. Production Catering1440 labels now share540.5625/634.9921875 row tops
and aligned separators;375 stays one335px column with contained buttons and no
overflow. Astra visually inspected both. No review findings remain deferred.
Preview-only final KB commits preserve the identical app source; their deployed
revision is recorded by Actions and their uncached version endpoints.
