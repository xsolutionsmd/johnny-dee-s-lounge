# Static multipage contract

No backend submission or database is needed. Native page URLs: `/`, `/menu/`, `/catering/`, `/visit/`. Each has its own HTML document and main content. Shared navigation/footer, active-page state and mobile navigation. Browser history uses normal links. Nginx serves each directory index directly, including refresh.

Public actions: `tel:+14106657000`; Google Maps directions for Johnny Dee's Lounge, 1705 Amuskai Rd, Parkville MD 21234; verified Facebook page. No contact forms, checkout, reservation system or staff admin. No requests are claimed to be sent.

Menu filtering is local DOM behavior only, implemented by Astra after Claude supplies `[data-menu-filter]` buttons and `[data-menu-category]` item groups. Allowed filter values: all, seafood, classics. Buttons expose aria-pressed; results announce through `#menu-status` if filtering is present. A simple unfiltered menu is acceptable if source coverage is too thin. Mobile menu visual behavior belongs to Claude.

`/health` and uncached `/version.json` are the runtime contract. All environments use noindex. Required links and local resources are checked before publication.
