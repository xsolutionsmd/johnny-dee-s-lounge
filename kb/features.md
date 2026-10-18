# Features

## R7 menu-photo behavior

Menu now contains38 sourced selections and20 matching dish photos. All six states
remain: All38, Sandwiches7, Seafood6, Classics4, Specials12, Soups & salads9.
Photographed dishes form aligned two-column lists on desktop and one column on
phones; unpictured items remain readable text without empty placeholders.
Historical specials and changing availability stay explicit. No new ordering,
submission or backend flow. Four native pages and verified destinations remain.


## Current R5/R6 accepted state

Expanded28-item published selection with six local category states (All,
Sandwiches, Seafood, Classics, Specials, Soups & salads); eight individual official
food/gathering photos plus the actual logo; Home photo viewer;500ms sliding mobile
drawer, soft page/section/filter transitions and reduced motion. All interactions
remain local or use the verified phone/Maps/Facebook destinations. No new backend.
The latest contract is [API](../docs/API.md). Earlier acceptance below is historical;
R5 full LIVE review and R6 focused call-target recheck passed. Exact production
revision: d8dfdb5562cf358a3f63aa6330b5139d80953af5.

Static multipage site with integrated contact/directions and local menu browsing. This speed-first scope uses no database, payments, submission endpoint, or staff admin.

## Selected features

- **integrate**: Native multipage navigation at `/`, `/menu/`, `/catering/`, `/visit/`. Distinct HTML/main content, active page, responsive shared navigation/footer and normal browser history.
- **integrate**: Menu selection from sourced dish names, with no unverified prices or ingredient claims. Optional local category filter. Explain briefly that selections/availability may change; call for today's menu.
- **integrate**: Click-to-call `tel:+14106657000`, Google Maps directions to the confirmed street address and official Facebook updates.
- **integrate**: Catering hall information and phone inquiry; no capacity, pricing, availability or free-hall promise without current terms.

## Existing systems

Phone and Google Maps are operational destinations. Facebook is the matched published business profile. No validated ordering/reservation integration is established; none will be simulated.

## Operational checklist

Confirm current full menu/prices, daily hours and catering terms. Derek's standing
instruction confirms business-asset use for this requested build. No fabricated
contact form or order flow. These gaps do not prevent using phone/directions.

## Function-first reference mapping for the corrective build

The functions above were selected in the initial scope on October17 BEFORE the
corrective reference search. The correction keeps that scope; the reference did
not introduce reservations, ordering or a form. Astra inspected the following
existing functions, then selected Joe Allen for company/asset/theme fit. This
mapping was made explicit during the owner's workflow refinement before release.

| Selected component | Inspected existing reference flow | Adaptation |
|---|---|---|
| Native separate pages + phone nav | https://joeallenrestaurant.com/ → /menus/ and /hours-location/; desktop split links and opened mobile disclosure observed | Four Johnny Dee's documents, shared nav/footer, active page, browser history |
| Local menu categories | https://joeallenrestaurant.com/menus/; activated Dessert and observed replacement content/active state; phone and desktop inspected | All / Seafood / Classics change only the menu results; no cart |
| Maps directions | https://joeallenrestaurant.com/hours-location/; actual Get directions link targets Google Maps directions API with its address | Same external directions flow using Johnny Dee's verified address |
| Telephone contact/inquiry | Joe Allen hours/location displays phone and explicitly directs larger parties to call; its phone text is NOT a tel link | Use Minetta's actual mobile tel link as the supplementary interaction reference below |
| Tap-to-call on phones | https://www.minettatavernny.com/menus/dinner; mobile persistent phone action and actual tel destination inspected without placing a call | Accessible tel links in Johnny's header and page CTAs; no sticky bar required |
| Catering hall inquiry | Joe Allen hours/location call-for-larger-parties instruction, no inquiry form used | Johnny's sourced hall information + direct phone CTA, no assumed capacity or online availability |
| Official social destination | Minetta's mobile header external Instagram link observed; Johnny's Facebook profile independently verified | Plain external official Facebook link; business images served locally |

Joe Allen is the visual composition reference. Minetta contributes only the
observed tap-to-call interaction, not its ornate theme. No calls, bookings or
submissions were performed on reference businesses. No required transactional
flow is missing because none was selected for this site.

## Initial-release acceptance (historical)

| Phase | Feature | Scenario | Viewport | How tested | Result | Evidence |
|---|---|---|---|---|---|---|
| pre | Multipage | All four built documents have distinct main content | desktop/mobile | Build plus browser | pass | 2026-10-17 production build and focused 1440px/375px browser checks |
| pre | Navigation | Mobile menu and browser history work | mobile | Browser interaction | pass | 2026-10-17 production build and focused 1440px/375px browser checks |
| pre | Links | Phone, directions, Facebook destinations match evidence | all | Link inspection | pass | 2026-10-17 production build and focused 1440px/375px browser checks |
| live | Multipage | Every URL direct-loads and refreshes over HTTPS on every environment | all | HTTP and browser | pass | All 12 environment/page combinations returned 200 twice at eba3440; production browser direct loads and reloads also passed |
| pre | Visual correction | Dark labels, single filtered menu, visit-card buttons | desktop/mobile | Rendered browser inspection | pass | Astra: brighter brass labels, centered 672px desktop result/343px phone result, aligned desktop buttons and contained mobile controls |


## Corrective-build acceptance

Pre-release: four distinct documents; authentic local image loads; consistent font;
all menu category states; mobile disclosure/Escape, active page and native history;
1440/375 rendered pages and320 Visit containment; final production/static check
all passed October17-18. Live route/reload and Sol review evidence follows release.


## Acceptance

| Phase | Feature | Scenario | Viewport | How tested | Result | Evidence |
|---|---|---|---|---|---|---|
| pre | Multipage | Four distinct documents and active navigation | desktop/mobile | Production check and rendered browser | pass | October18 corrective source: npm run check11files; four actual pages1440/375 |
| pre | Controls | Filters, mobile disclosure/Escape and native history | mobile | Browser interaction | pass | All/Seafood/Classics; Menu-to-Visit; back/forward; Escape focus restored |
| pre | Media and layout | Actual approved assets, one font, contained controls | desktop/mobile | Visual and DOM inspection | pass | Real logo/food load;1440/375 all pages;320Visit no overflow; Home buttons inside containers |
| live | Multipage | Four routes direct-load and refresh on all environments | all | HTTPS helper and browser | pass | 5e719dc: all12environment/route combinations HTTP200 twice, exact revisions and noindex; production rendered assets confirmed |

## R5 acceptance

| Phase | Feature | Scenario | Viewport | How tested | Result | Evidence |
|---|---|---|---|---|---|---|
| pre | Menu | Six category states and28 sourced selections |320px phone| Real clicks and visible group/count checks | pass | Counts6/4/4/6/8/28; no overflow |
| pre | Drawer | Open focus, Tab wrap, Escape/refocus and inert background |320px phone| Browser keyboard actions | pass | Close receives focus; reverse Tab reaches phone; forward Tab returns Close; Escape returns toggle |
| pre | Gallery | Open, next, Escape and opener restoration |375px phone| Browser controls and ArrowRight | pass | Photo/caption change, contained image, scroll unlock |
| pre | Visual fit | Eight actual photos, one family, corrected hero/menu proportions |1440/375;320Visit| Rendered comparison and measured geometry | pass | Sol blueprint P1/P2/P3 addressed by Astra; production check19files |

| live | Full interaction review | All pages; six filters/rapid/keyboard, all gallery paths, drawer focus/outside/Escape/resize, native direct loads/reloads/back/forward and CTA destinations |1440/375;320 controls| Sol hands-on LIVE review at57edc5e | pass | Prior full review; sole P3 call width corrected by Astra and verified below |
| live | Call-target correction | All four shared headers:44x44, centered icon, parent containment, zero overflow; actual added-padding clicks reach correct tel destination with external dispatch prevented |375x812 and320x812| Sol focused LIVE recheck atd8dfdb5 | pass | Eight measured/trusted-click checks; nav open/close/focus containment and desktop regression also pass |
| live | Final release routes | All four documents direct-load and uncached reload over HTTPS in all three environments; exact own branch revision, health and noindex |all| Read-only release audit and version verifier after final preview pushes | pass | Production staysd8dfdb5; previews carry the same app plus final documentation; consult each /version.json and Actions |

The19-file production/static check at sourcec5722dbe198e2b96eb76521e6793c32c628e72b4
is Astra's validated build evidence; no redundant local rebuild was run for handoff.
Physical touch, broader browser coverage and runtime reduced-motion emulation remain
unverified. Source reduced-motion rules were checked; no real call was dispatched.
