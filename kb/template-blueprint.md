# Reference reconstruction and adaptation blueprint

Observed October 17, 2026 EDT / October 18 UTC. This focused reconstruction was
performed during an active correction, after the provisional implementation
existed. It is not evidence that this workflow preceded coding, and it is not
post-publication acceptance.

Reference: [Home](https://joeallenrestaurant.com/),
[Menus](https://joeallenrestaurant.com/menus/),
[About](https://joeallenrestaurant.com/about/) and
[Hours & Location](https://joeallenrestaurant.com/hours-location/).
Browser inspection used 1440×900 and 375×812 CSS viewports. Matching captures of
all four reference pages and all four company pages, plus interaction captures,
are retained in the separate private analysis record. Reference captures are
research evidence, not assets to publish with this site.

Evidence labels below: **observed** means rendered browser behavior or measured
DOM geometry; **defined** means delivered public CSS/JS; **adaptation** means a
deliberate company implementation choice. Passive REA capture was unavailable:
the existing endpoint had failed discovery, and the available browser processes
used debugging pipes rather than the literal-port loopback CDP endpoint REA
requires. This is browser/source reconstruction, not successful REA analysis.

## Capabilities and page structure

The selected capabilities preceded reference selection. Preserve four native
company documents: `/`, `/menu/`, `/catering/`, `/visit/`. Menu categories, call,
directions, catering phone inquiry, official social and an expanded real-photo
gallery with a local viewer are the included functions. No form, order,
reservation, payment, availability engine or account is selected.

| Capability | Actual reference observation | Company requirement |
|---|---|---|
| Separate pages | Desktop links and mobile drawer lead to distinct Home/Menu/About/Location documents | Four company URLs; normal history, active page and direct loads |
| Menu categories | Main → Dessert on desktop and Main → Beer on phone replace visible local content without changing URL | Local category controls; clear selected state; keep sourced dish content |
| Directions | Location has a rendered Google map and Get directions link to Google Maps directions API, opening a new tab | Verified Parkville address; external directions link suffices |
| Phone inquiry | Reference displays phone as plain text and says to call for larger parties | Real `tel:+14106657000`; supplementary observed Minetta tel reference remains in [features](features.md) |
| Photo viewer | About image control opens an actual 17-image lightbox at both sizes; Next/Previous, close and keyboard navigation | Local viewer for company photos; accessible controls, Escape and focus restoration |
| Social | Supplementary social-link observation is documented in [features](features.md), not inferred from Joe Allen | Verified official Facebook destination |

Reservation/gift/theater/sibling-restaurant links exist on the reference but do
not belong to the company scope. Reference booking rules, payment policy,
accessibility claims and capacity are not company facts.

## Measured visual system

**Observed desktop masthead:** white navigation band ends at y=88. The centered
reference logo is approximately 155×148, x=642 at 1440px, overlapping the image
by 60px. Three compact links sit on each side; 32px gaps separate links. Header
is in document flow, not a sticky overlay. Authored desktop nav is uppercase
Work Sans 600 at 13.6px. Active/hover emphasis uses red. Adapt red to company ink
and use the intact tankard logo with a similarly prominent centered overlap.

**Observed phone masthead:** the reference retains a 155×148 centered logo and
88px image start; hamburger is a 44px target at x=15, y=21. It does not shrink
the reference logo to 70px. The draft's 108px logo and 76px band are a reasonable
adaptation for its round artwork and direct call utility, rather than an exact
measurement of the reference. Keep that distinction explicit.

**Observed Home:** one uninterrupted full-width food photograph starts at y=88.
At 1440×900 it is 687px tall; at 375×812 it is 599px tall. A compact approximately
125px footer completes the viewport. There is no visible headline, gradient,
CTA overlay, carousel or sequence of editorial sections on this reference Home.
Its quality comes from the table composition, scale and uncluttered masthead.
For Johnny Dee's, portrait food photographs may form a paired desktop opening
and a single phone opening; preserve plate composition and use restrained
contrast treatment for useful company copy/actions. Expanded content is an
intentional response to the richer company presentation scope.

**Observed Menu:** a white page without a top photo banner. Desktop title top
y=212, approximately 29.4px/44px, medium uppercase; brief two-line explanatory
copy at y=264 uses 15px/22.5px. Category text starts y=358. The core menu is 768px
wide, centered at x=336; two approximately 352px item columns have a 64px gutter.
Section heading top y=444 uses 22px/33px. First dish top y=509. Dish names use
16.8px medium uppercase; descriptions and prices use approximately 14.4px/18.7px.
Items are centered, with generous vertical breathing room, not individual cards.
Preserve hierarchy and rhythm without inventing company prices or ingredients.

On phone, title top is approximately y=208; content is 345px wide with 15px side
margins. Categories wrap, followed by a single centered item column. In the
inspected current phone reference some category labels sit too close together;
preserve clear separation and the draft's larger touch targets instead of
reproducing that defect. Company category names may require two rows.

**Observed About:** title shares the internal-page title rhythm. Desktop content
starts near y=320: a 672×600 photo mosaic at x=32, 32px gutter, then a 672px text
column at x=736. The mosaic has mixed tile sizes, 16px desktop gaps and 17 real
food/drink/interior photos; these are cropped inside tiles rather than spilling
outside their boundaries. On phone the mosaic is 345×600 at x=15, with tighter
gaps, followed by narrative after approximately 30px. Gallery layout settles
after image/plugin initialization. Johnny Dee's four-image portrait mosaic is
an asset-driven simplification, not a reproduction of the same tile count.

**Observed Location:** a full-width interactive map begins under the band,
405px tall desktop / approximately 365px phone. A centered white address panel
overlaps its lower portion; address and directions precede centered daily hours
and supporting copy. A lower photo mosaic follows. Johnny Dee's direct directions
and two-column address/hours layout is a substantial but legitimate adaptation:
no selected requirement needs a third-party embedded map or its network cost.

**Typography/color adaptation:** the reference uses Karla body and Work Sans
headings/UI, white, near-black and red. Johnny Dee's must keep one self-hosted
Instrument Sans family, medium headings, readable neutral body text, black/white
tankard identity and restrained warm paper backgrounds. Original logo lettering
remains image artwork. Do not add serif accents or decorative section numbers.

## Interaction and motion contract

| State/action | Evidence | Reproduction boundary |
|---|---|---|
| Open mobile navigation | Observed 320px left drawer over dimmed page; live transform transition measured 500ms ease | Draft uses the same scale/timing; close, outside dismiss, Escape, focus and scroll handling must remain useful |
| Select menu category | Observed local replacement and selected color; URL unchanged; delivered small menu script does not fetch data or animate results | Draft 400ms result fade/rise is added polish; do not claim exact reference parity |
| Link/button hover | Defined/observed interactive transitions approximately 200ms | Consistent company hover and focus feedback |
| Image load fade | Defined public CSS: opacity transition 400ms ease-in | Definition is not proof every image executed it |
| Section entrance | Defined 750ms fade-up utility; no instantiated fade utilities found in inspected Home/Menu/About DOM | Draft 750ms section reveal and 900ms hero image entrance are deliberate additions |
| Gallery open/next/close | Observed overlay, contained full image, next/previous controls and disabled Previous on first reference image; ArrowRight advances; Escape closes after transition | Draft viewer may wrap and omit counters; no visible decorative count; restore opener focus and respect reduced motion |
| Page transition | Reference cross-document animation not established | Draft native view transitions are an adaptation; do not require a framework/router |

The reference lightbox **did work in this pass**, superseding an earlier
unsuccessful click observation. Its full-image load and overlay settle
asynchronously. Opening/closing snapshots captured mid-transition must not be
mistaken for a permanent transparent or missing viewer.

No forms are selected, so validation/submission success states do not apply.
Menu/gallery image failure and offline states were not provoked; private server
rules are unknown. External Maps arrival, phone dialer and social sign-in are
integration boundaries, not transactions to simulate.

## Exact company asset mapping

Files below are under `app/public/media/`. Source IDs are public official
Facebook photo identifiers; source records and permissions are in [media](media.md).
All eight new draft photographs match the recovered rendition SHA-256 exactly.

| Local file | Official photo ID / date | Actual draft placement and constraint |
|---|---|---|
| `johnny-dees-logo.png` | 748612449905197 | Shared masthead/footer/favicon; intact 666×675 tankard artwork |
| `shrimp-pasta.jpg` | 6114920521856521 / 2022-07-13 | Home lead, 1536×2048; preserve plate composition |
| `ahi-tuna.jpg` | 1179688166797621 / 2024-04-17 | Home second desktop photo, 1536×2048; tuna salad, not steak |
| `soft-crab.jpg` | 1801544201278678 / 2026-05-01 | Home mosaic/viewer; historical seasonal offering |
| `shrimp-tomato.jpg` | 5020228011325783 / 2021-08-11 | Home mosaic and Menu ribbon; only 750×586, keep bounded |
| `ravioli.jpg` | 804720554294386 / 2022-11-02 | Home mosaic and Menu ribbon; historical special |
| `italian-sub.jpg` | 4419715034710420 / 2021-01-27 | Home mosaic and Catering food panel; no current package implied |
| `gathering.jpg` | 1085379506228488 / 2023-11-29 | Home gathering feature, Catering banner, Visit photo; historical paint night, no current schedule/capacity claim |
| `eggplant.jpg` | 860845338681907 / 2023-01-04 | Menu ribbon; historical kitchen dish |

Recovered soft-crab trays (1908144187285345) and turkey pot pie
(810521040381004) are not used in the inspected draft. The earlier
`johnny-dees-food.jpg` collage is retained locally but is not a visible draft
photo. No need to insert every available photograph. Do not relabel the turkey
pot pie as chowder, imply archival dishes are available today, enlarge the small
tomato photograph to a full-width hero, or import reference business media/code.

## Supporting implementation and remaining fit work

Static documents, local category state and local image-viewer state suffice.
Inputs are category IDs and photo index; outputs are visible menu groups,
accessible status, selected image and caption. No records are written and no
custom API/database is implied. Phone, Google Maps and Facebook handle external
actions. Keep actual company destinations and the listed-hours caveat from
[contact and hours](contact-and-hours.md).

The provisional draft has 28 sourced dish examples, five groups plus All, eight
distinct new business photographs, and a local four-photo Home viewer. Preserve
that useful depth. Focus correction on the desktop hero grid's intrinsic-height
crop and the Menu introduction/column proportions. These are fit findings for
the active correction, not a new design direction. A fresh post-publication
review must still exercise every included customer interaction and final state.
