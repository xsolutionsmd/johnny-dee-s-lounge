# Static pages and local interaction contract

R5 refinement, October18,2026. No submission backend, database or customer account
is needed. Existing Nginx/runtime and external integrations are retained. Backend
needs are derived from the selected menu/navigation/contact/photo-viewing flows;
reference reservations, gifts and unrelated services are outside scope.

## Pages and integrations

- Native documents: `/`, `/menu/`, `/catering/`, `/visit/`; direct directory-index
  serving and refresh, ordinary browser history, shared active navigation.
- Call: `tel:+14106657000`; device dialer, no website submission or test call.
- Directions: `https://www.google.com/maps/dir/?api=1&destination=Johnny+Dee%27s+Lounge%2C+1705+Amuskai+Rd%2C+Parkville%2C+MD+21234`.
- Social: `https://www.facebook.com/p/Johnny-Dees-Lounge-100042693473168/`.
- `/health` and uncached `/version.json` identify the healthy deployed image.
  All environments retain noindex. No external runtime dependencies.

## Local state and behavior

Menu categories are `all`, `sandwiches`, `seafood`, `classics`, `specials`, `soups`.
Buttons `[data-menu-filter]` expose aria-pressed. Groups `[data-menu-category]`
use native hidden. `#menu-status` announces the number of visible dishes. Only
listed categories are accepted; rapid changes cancel the previous400ms entrance.
No inventory, availability, price or order is inferred from a selected category.
All28 entries remain in static HTML when scripting is unavailable.

Mobile navigation is a320px left drawer (bounded to viewport minus40px), with
close button, dimmed outside-dismiss, Escape, focus containment/restoration and
background inert while open. Resizing to desktop and bfcache restore reset it.

Home gallery links open the actual full-size local photograph in a native dialog.
Previous/next and Left/Right keys cycle selected photos; Escape/backdrop/close
restore opener focus. There is no autoplay and no server write. Without scripting,
ordinary links still open the underlying image. Native HTML dialog provides the
modal focus boundary; captions are polite live status.

Reduced-motion preference disables entrance/filter/hover/page animations. Other
users get a500ms drawer,200ms hover response,400ms category fade and750ms soft
section entrances. These are original code adapting observed reference patterns,
with additional section/page continuity as explicitly requested.

## Checks

Existing static runtime/link contracts were verified in prior releases and are
unchanged. R5 production/static build passes with allfour documents and local media.
New local state checks and live revision/route checks are recorded in
`docs/VALIDATION.md`; no call, message, booking or purchase is sent as a test.
