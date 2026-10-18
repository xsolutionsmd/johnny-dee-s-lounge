# Design brief

## Current refinement: fuller photography, structure and motion

Derek's October17–18 correction supersedes the prior sparse interpretation.
Astra implements this refinement directly, with **no Claude**, then Sol reviews
the rendered live result. Preserve the four native page URLs and actual business
destinations. The selected functions remain menu browsing, call, catering inquiry,
directions and social updates; a keyboard-accessible photo viewer supports the
expanded real-photo gallery. No booking or checkout is introduced.

Freshly inspected blueprint: https://joeallenrestaurant.com/ and its /menus/,
/about/ and /hours-location/ pages, desktop1440×900 and phone375×812. Match the
compact split navigation and overlapping centered brand, large photo directly
below it, spacious centered menu introduction, compact category row and balanced
two-column menu. Its About-page photo mosaic informs our real-food gallery beside
company copy. Use Johnny Dee's tankard branding, restrained black/white/warm paper,
one Instrument Sans family and only authentic business images.

Motion observations: live mobile drawer slides320px from the left in500ms with
page dimming; delivered styles use200ms interactive transitions and400ms image
fades. Fade-up utilities of500/750ms exist in the delivered stylesheet but were
not instantiated on the inspected Home/Menu/About pages. Our restrained section
entrances and cross-document fades are intentional polish adaptations, not a
claim those animations executed on the reference. Respect reduced motion. The
reference gallery declares lightbox links; the parent's initial multi-match click
did not establish runtime behavior. Sol's unique-target inspection owns that
observation. Our native photo dialog must work, including Escape/focus restoration.

Expanded media/menu evidence and page mapping are recorded in `media.md` and
`sources.md` as recovered. Earlier assertions that no additional imagery/menu
exists describe only the earlier bounded search and must not limit this pass.

Speed-first build, 2026-10-17. Frontend by Claude Opus 5.5 (design sub-agent).

## Visitor job and primary action

Find the neighborhood lounge, see a few sourced dishes, call (tel:+14106657000) for
today's menu or catering, and get directions to 1705 Amuskai Rd, Parkville, MD 21234.
Primary action: call. Secondary: directions.

## Content plan

Four separate documents, never homepage sections:

| Page | Visitor question | Content |
|---|---|---|
| `/` | What is this place? | Authentic logo and food-led opening, call and menu actions; four-dish menu sample; catering band; visit details |
| `/menu/` | What do they serve? | Seafood and Classics groups of six customer-mentioned dish names (offerings.md); filter markup; one note to call for soups, specials and the full menu |
| `/catering/` | Can I hold an event? | Catering hall (Facebook source); what to have in mind before calling; phone card. No capacity, packages, prices or booking |
| `/visit/` | When and where? | Address and directions, phone, listed hours with one confirm-by-phone note, Facebook link |

No prices, ingredients, reviews, ratings, founding year, capacity, ordering or reservations.

## Template site

### Corrective selection, after the first release

Astra searched and visually inspected these real sites on October 17–18, 2026,
AFTER release `7a795575`. The initial site did not use a selected live template.
The owner's correction requires a visible implementation, not retrospective credit.

The selected capabilities predate this search: separate pages, local menu
switching, phone inquiry and Maps directions. See the exact component-to-inspected
flow table in [features](features.md#function-first-reference-mapping-for-the-corrective-build).
Joe Allen demonstrates the menu/page/directions and larger-party phone-inquiry
patterns. Its phone text is not clickable, so the already-inspected Minetta mobile
tel action supplies that narrowly defined interaction reference; no visual theme
or booking functionality is imported from it.

**Selected: [Joe Allen NYC](https://joeallenrestaurant.com/).** Inspected its home,
[menu](https://joeallenrestaurant.com/menus/) and
[hours/location](https://joeallenrestaurant.com/hours-location/) at desktop 1440×900
and phone 375×812. Opened the mobile navigation; activated Dessert on its menu and
observed the content change. Examined telephone/directions destinations without
submitting a booking. Its clean centered brand, split desktop navigation, spare
white pages, restrained sans-serif typography, two-column menu and stacked mobile
menu are the composition template for the correction.

Why it fits the three inputs:

- **Company:** a neighborhood American restaurant/lounge with shrimp salad, soups,
  specialties and a catering hall. Johnny Dee's verified Facebook uses a black and
  white circular beer-tankard identity and a six-dish food collage. Straightforward
  food-and-neighborhood character is supported; the earlier ornate supper-club
  concept was not grounded in that identity. Use black/white, warm off-white and
  restrained dark accents, not Joe Allen's red identity or theater story.
- **Assets:** the official 851×315 food collage and 666×675 tankard logo are now
  authorized for direct site use by Derek's standing owner-permission instruction,
  explicitly reiterated during this correction. Local production copies are
  `/media/johnny-dees-food.jpg` and `/media/johnny-dees-logo.png`. No panorama,
  premises gallery or current full menu exists. Use the food image intact at its
  natural aspect ratio, bounded to its source resolution; use the real logo in
  the shared masthead. Replace the provisional embed with these reliable local
  images. Retain an ordinary official Facebook link.
- **Scope:** four separate pages, local menu category browsing, phone inquiry and
  directions. The selected reference has the needed menu switching and location
  flow. Do not copy its reservations, gifts or theater features; Johnny Dee's has
  no verified booking/ordering endpoint. Its map is an optional reference trait,
  not a reason to add a new API dependency.

Runners-up inspected desktop/mobile: [Minetta Tavern](https://www.minettatavernny.com/)
(home and mobile dinner menu) is too ornate and dependent on interior photography;
[Gertrude's](https://www.gertrudes.nyc/) (home and mobile menu) has useful separate
menus/events but its whimsical illustration identity and decorative serif are
less suited to this restaurant and the owner's typography correction.

Required visible adaptations for Claude:

- Replace the dark split illustration hero with a white/near-white restaurant
  masthead, centered compact REAL LOGO and balanced navigation inspired by Joe
  Allen. Strong plain-language heading and prominent call/menu actions paired
  with the genuine food collage. No fabricated logo, coupe/arch artwork or deco
  fans. The logo's existing lettering is preserved as branding, not restyled.
- Replace decorative menu cards with a spacious centered menu-sheet composition:
  category controls, readable dish rows, thin separators, balanced two-column
  desktop layout and one column on phones. Preserve the actual filter hooks.
- Recompose catering and visit with the same masthead, type scale, generous but
  bounded whitespace and concise centered page introductions. Keep real contact
  actions, listed-hours caveat and all four native page URLs.
- **One authored type family: self-hosted Instrument Sans**, including wordmark,
  headings, body, menu, navigation and buttons. Use weight/size for hierarchy.
  No italic serif accents, decorative lettering or extra display families.
  The original logo's lettering is an image, not an additional authored typeface.

Actual media mapping: official food collage → Home opening composition and bounded
Menu photo strip; official tankard logo → shared header on every page and footer
where useful; six sourced dish names → live HTML menu; official Facebook
description → concise soup/specialty/catering context. The monochrome tankard and
food photos inform the white/black restaurant theme. No competitor assets or code.

The first corrective draft used an official Meta embed while permission was
uncertain. Before release, Derek reiterated the updated standing asset-use
instruction, which confirms owner permission. This supersedes that temporary
restriction and the initial reference-only flag; direct local images are required.

Private rendered evidence: `private/runs/template-correction-r2.md`.
This selected brief precedes the corrective Claude implementation.

### Polish blueprint and matching-view comparison

The quality decision is based on the inspected design, not the restaurant's fame:
Joe Allen has a balanced split masthead, disciplined uppercase navigation, an
immediate food image, simple aligned menu columns, clear text-category states and
a coherent mobile stack. Its white/black typography makes the real photography
the focus. Adapt those specific relationships and details, with Johnny Dee's own
black-and-white logo and food image. Do not reproduce its red identity or imagery.

At 1440x900 the reference has an 88px navigation band with the centered logo
extending to 148px; its food photo starts immediately under that navigation. At
375x812 the mobile menu and centered logo frame the image without decorative
cards. Menu pages use restrained centered titles, two desktop columns and one
phone column. Our authentic roundel uses 112px desktop / 70px mobile, and the food
collage is limited to its natural 851x315 proportions rather than enlarged into
a blurry panorama. One self-hosted Instrument Sans family covers authored text;
consistent weights, spacing, rectangular buttons and clear focus/active states
provide hierarchy.

Astra compared the real draft at matching sizes after asset integration. The
text-first Home delayed photography relative to the reference. A focused Claude
follow-up was requested to make the opening photo-led, tighten its copy/actions,
and align the three visit actions. Desktop/mobile reference captures and exact
component notes were supplied before that edit; no new search or redesign was
started. The post-release Sol review must compare fidelity and polish as well as
imagery, fonts, spacing and overflow. The limited-resolution collage is the real
available business asset; polished composition cannot create missing photography.

## Initial visual direction (superseded by the corrective template above)

- **Concept:** a vintage neighborhood supper-club card. Espresso and oxblood rooms,
  cream paper, brass hairlines and deco ornament.
- **Type:** Fraunces variable (SOFT/WONK, italic accents) for the wordmark, headings
  and dish names; Instrument Sans for UI and labels. Both are OFL and self-hosted in
  `app/public/fonts`, so there are no external requests.
- **Palette:** ink #1b1311, oxblood #4e1519, wine #6e2029, paper #f8f0e1, cream
  #efe2c9, brass #d1a85c (dark backgrounds only), brass-deep #8a6424 (light), text #2a1c17.
- **Imagery:** no photography until the business clears media rights. Instead there
  is an original line illustration (arched doorway, coupe glass, sparkles) that draws
  once on load, plus a deco fan behind the catering band. The type-only wordmark does
  not trace the protected logo.
- **Motion:** one-time rise and line-draw entrances, cross-document view transitions,
  and hover underlines and arrow nudges. There is no ongoing motion, and everything is
  disabled under reduced motion.
- **Stitch:** one bounded attempt (project 16098297216476375507) timed out, and
  list_screens returned no screens, so the build used the planned fallback.

## Accepted decisions and corrections

- 2026-10-17 post-publication Sol rendered review covered all four routes at 1440px and 375px. Astra addressed all three findings: brighter small labels on dark sections, centered bounded single-category desktop menu results, and aligned homepage visit-card actions. Two-column All results and mobile card containment are preserved.
- 2026-10-17 owner: a real multipage site in which every nav tab is a distinct URL,
  never a #section. Shared header/footer, aria-current active state, mobile disclosure nav.
- 2026-10-17 latest owner correction: actual gathered business assets must appear
  in rendered pages. Derek's updated standing instruction confirms owner
  permission for this requested build. Use the two selected official assets
  directly, with provenance. No competitor, generated or third-party Maps photos.

## X Solutions standing design rules

- Thoughtful, distinctive, professional and clean: strong typography, authentic
  photography, smooth restrained motion, enjoyable interaction; necessary copy only.
- No decorative numbering: no section ordinals, numbered badges, photo prefixes or
  counters such as 01 / 02. Factual numbers (prices, phone, dates) are fine.
- Choose photos for composition, quality, real work shown, variety and recency across
  the whole history, not just the newest posts. Never present generated or competitor
  work as the client's.
- Check every form control against its containing card (including padding) on narrow
  phones, with enlarged text and focus states; page-level overflow checks are not enough.
- Native inputs, keyboard access, visible focus, reduced-motion support and a pause
  control for ongoing decorative movement.
- Consistent SVG arrows/icons (no text glyphs or emoji arrows). No visitor-facing demo,
  preview or "functionality" banners and no repeated disclaimers.
- Optimise without degrading the experience: right-sized media, lazy loading, no
  needless browser work.
