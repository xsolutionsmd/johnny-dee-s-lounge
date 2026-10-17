# Design brief

Speed-first build, 2026-10-17. Frontend by Claude Opus 5.5 (design sub-agent).

## Visitor job and primary action

Find the neighborhood lounge, see a few sourced dishes, call (tel:+14106657000) for
today's menu or catering, and get directions to 1705 Amuskai Rd, Parkville, MD 21234.
Primary action: call. Secondary: directions.

## Content plan

Four separate documents, never homepage sections:

| Page | Visitor question | Content |
|---|---|---|
| `/` | What is this place? | Wordmark hero, call and directions; concise about; four-dish taste of the menu; catering band; visit cards |
| `/menu/` | What do they serve? | Seafood and Classics groups of six customer-mentioned dish names (offerings.md); filter markup; one note to call for soups, specials and the full menu |
| `/catering/` | Can I hold an event? | Catering hall (Facebook source); what to have in mind before calling; phone card. No capacity, packages, prices or booking |
| `/visit/` | When and where? | Address and directions, phone, listed hours with one confirm-by-phone note, Facebook link |

No prices, ingredients, reviews, ratings, founding year, capacity, ordering or reservations.

## Template site

Speed-first exception from the owner: no broad reference hunt and no REA. The
direction draws on the premium supper-club and steakhouse genre (dark room, brass
detail, editorial serif menu cards), adapted for structure and tone only. Nothing was
copied: no branding, text, imagery or code.

## Visual direction

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

- 2026-10-17 owner: a real multipage site in which every nav tab is a distinct URL,
  never a #section. Shared header/footer, aria-current active state, mobile disclosure nav.
- 2026-10-17: media rights unconfirmed. No stock or generated food presented as the
  business's, and no copying or hotlinking of public photos. Swap in cleared assets
  when main supplies them.

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
