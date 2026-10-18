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
Production and both previews remain at `7a795575` while the authorized reference-led
correction is prepared on `derek-dev`. Repository:
https://github.com/xsolutionsmd/johnny-dee-s-lounge.

## Current correction

The first release did not use an inspected live template. Following Derek's
correction, Astra reviewed the existing functions, business facts and actual media,
then inspected three real references on desktop/mobile. Joe Allen is selected for
composition; Minetta contributes only a mobile tel-link behavior missing from Joe
Allen. Exact function mapping and observations are in `features.md` and
`design-brief.md`. Claude rebuilt all four pages accordingly: white/black theme,
centered identity and balanced navigation, menu-sheet composition and one authored
type family, Instrument Sans.

Derek's latest standing instruction confirms permission to use the business assets.
The food collage and original tankard logo are selected local production images,
with provenance and page mapping in `media.md`. The temporary embed-only approach
was superseded before release. Claude completed the real-image integration and a focused photo-first refinement using supplied desktop/mobile reference captures and spacing notes.
Original files and private operational/commercial notes remain outside this repo.

## Verification and next action

The final corrective source passed npm run check (11 built files), actual desktop1440/phone375 inspection on all four pages, 320px Visit containment, local filters, mobile navigation/Escape and browser history. Both authentic assets load locally. Home photo leads directly below the masthead and all three visit actions align. Next: release by authorized protected-main PR, perform the
requested fresh Sol High LIVE desktop/mobile review (reference fidelity, actual
assets, typography and awkwardness), have Astra fix actionable findings, verify all
three environments and send final Slack URL correction. Earlier checks in
`docs/VALIDATION.md` describe the first delivery and cannot substitute for this pass.

## Remaining owner content

Current full menu/prices, confirmed daily hours and catering terms/capacity.
Six customer-mentioned dish examples and listed hours remain qualified. Phone,
Maps and official Facebook destinations are real; no order/reservation/form
submission is simulated. Asset permission is no longer a pending question.
