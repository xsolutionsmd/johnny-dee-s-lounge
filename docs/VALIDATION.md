# Validation

2026-10-17, speed-first delivery. Four real documents: `/`, `/menu/`, `/catering/`, `/visit/`. Primary navigation has no section-anchor destinations.

Initial release `eba3440f7952cf754cf52fa9410aa862a2349aa5` was built and tested locally, then published directly to Oracle before GitHub setup. It was subsequently replaced with Actions-built digest-pinned images in all three environments. Six initial CI/release runs passed. The 18 existing sibling containers retained their identities and images and remained healthy.

Checked: production build and static/resource checks; ARM64 read-only Nginx candidate health/version; four distinct pages and one H1 per page; every route loaded twice over HTTPS in all environments; actual production browser direct load/reload of each page; native back/forward; mobile navigation and active states; local menu filters; sourced phone, Maps and Facebook destinations. No real calls, submissions or orders were made. All public environments intentionally carry noindex.

Sol inspected rendered live pages at 1440×900 and 375×812, including full-page scrolling, every main page, mobile navigation and menu filter states. No clipping or rendering blockers were found. Astra addressed three findings in the follow-up source: brighter dark-section labels, centered bounded filtered menu cards, aligned homepage card buttons. Affected desktop/mobile views were inspected and `npm run check` passed. The All menu state restores two columns; single-result cards are centered on desktop and fit phones. All three homepage action bottoms match, and phone controls remain inside their cards.

The release workflow verifies the deployed revision; `scripts/verify-pages.py BASE_URL --revision SHA` checks each route twice, distinct content, noindex and version. Exact current revisions are at each environment's `/version.json` and in GitHub Actions/deployments. Detailed screenshots, operational receipts and Slack delivery history are retained in the private project handoff.

Limits: no current complete owner-issued menu/prices, current daily hours confirmation, catering terms/capacity, or photo reuse permission. The six menu names are sourced examples. Listed hours carry a phone-confirmation note. The site uses licensed fonts and original graphics; unapproved reference photography is excluded. No booking, ordering, forms, database or staff-delivery integration is implied. This was a focused Chromium desktop/mobile pass, not exhaustive cross-browser certification.
