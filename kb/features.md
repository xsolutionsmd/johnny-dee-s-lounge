# Features

Static multipage site with integrated contact/directions and local menu browsing. This speed-first scope uses no database, payments, submission endpoint, or staff admin.

## Selected features

- **integrate**: Native multipage navigation at `/`, `/menu/`, `/catering/`, `/visit/`. Distinct HTML/main content, active page, responsive shared navigation/footer and normal browser history.
- **integrate**: Menu selection from sourced dish names, with no unverified prices or ingredient claims. Optional local category filter. Explain briefly that selections/availability may change; call for today's menu.
- **integrate**: Click-to-call `tel:+14106657000`, Google Maps directions to the confirmed street address and official Facebook updates.
- **integrate**: Catering hall information and phone inquiry; no capacity, pricing, availability or free-hall promise without current terms.

## Existing systems

Phone and Google Maps are operational destinations. Facebook is the matched published business profile. No validated ordering/reservation integration is established; none will be simulated.

## Operational checklist

Confirm current full menu/prices, daily hours, catering terms and media reuse permission. No fabricated contact form or order flow. These gaps do not prevent using the published phone/directions.

## Acceptance

| Phase | Feature | Scenario | Viewport | How tested | Result | Evidence |
|---|---|---|---|---|---|---|
| pre | Multipage | All four built documents have distinct main content | desktop/mobile | Build plus browser | pass | 2026-10-17 production build and focused 1440px/375px browser checks |
| pre | Navigation | Mobile menu and browser history work | mobile | Browser interaction | pass | 2026-10-17 production build and focused 1440px/375px browser checks |
| pre | Links | Phone, directions, Facebook destinations match evidence | all | Link inspection | pass | 2026-10-17 production build and focused 1440px/375px browser checks |
| live | Multipage | Every URL direct-loads and refreshes over HTTPS on every environment | all | HTTP and browser | pending | Await deployment |
