# Barber Republic — Brand Specification

Source: Barber Republic Master Asset Guide (Collective Matrix, Round 3
Concept 3, QA verified). Shared by John, 8 Sept 2026. This file is a
specification only — the logo and wordmark artwork must be taken from
the supplied vector masters. **Do not regenerate, redraw or retype
them.**

---

## 1. Identity

| Item | Value |
|---|---|
| Name | Barber Republic |
| Mark | Collective Matrix |
| Wordmark | BARBER / REPUBLIC, two lines, letterspaced |
| Master tagline | Intelligence that Builds the Industry |
| Core idea | Independent individuals forming a stronger intelligent network |

**Locked:** mark geometry, wordmark geometry and proportions, spacing,
tagline wording.
**Adaptable:** orientation, background, monochrome treatment, optical
scale.

## 2. Colour tokens

```css
:root {
  --br-near-black:   #0E0E0D;  /* primary background */
  --br-bronze:       #DEB57E;  /* primary accent, mark */
  --br-dark-copper:  #B87A43;  /* secondary accent */
  --br-light-bronze: #F0C98E;  /* highlight */
  --br-warm-ivory:   #F2EFE9;  /* light background */
  --br-white:        #FFFFFF;
}
```

Palette discipline: premium restraint, high contrast. No unrelated
colours, no glows, no drop shadows, no barber-pole or barber-cliche
imagery.

## 3. Clear space and minimum sizes

- Clear space: at least one central square of the matrix on all sides.
  Use more in premium applications.
- Standalone mark: 24px minimum outside favicons.
- Wordmark: 140px wide minimum.
- Tagline lockup: 320px wide minimum.
- Below 24px, use the dedicated favicon exports only.

## 4. Approved lockups

1. Stacked — mark above wordmark. Default for square and portrait space.
2. Horizontal — mark left, wordmark right.
3. Horizontal + tagline — as above with the tagline beneath the wordmark.

Rule: use the smallest system that communicates the brand clearly.

## 5. App icons

| Variant | Background | Mark |
|---|---|---|
| Primary dark | Near-black | Bronze |
| Light alt | Warm ivory | Dark copper |
| Copper alt | Dark copper | Near-black |

The mark fills roughly 78% of the usable tile. Do not shrink it to a
small floating element. Render from vector at oversized resolution,
then downsample. Leave OS masking to the platform.

## 6. Favicons

Exports at 16, 32, 48, 64, 128, up to 512px, plus ICO and web manifest.
Supersample from vector, then downsample for antialias clarity. No
raster tracing.

## 7. Non-negotiable rules

- Do not redraw or regenerate the Collective Matrix.
- Do not replace the vector wordmark with typed text or another typeface.
- Do not stretch, skew, rotate or distort the mark.
- Do not reduce app icons or favicons to a tiny floating element.
- Do not introduce unrelated colours, glows, shadows or barber cliches.
- Do not use any retired concept line as the master tagline.
- No raster tracing in production artwork.

## 8. Asset folder map

```
00_SOURCE_OF_TRUTH   Approved references, README, inventory
01_CORE_MASTERS      Vector mark + vector wordmark + hi-res PNG   <-- required for build
02_PRIMARY_LOCKUPS   Stacked, horizontal, tagline systems
03_APP_ICONS         Native square and adaptive exports
04_FAVICONS          16-512px exports, ICO and manifest
05_SOCIAL_AVATARS    Dark and light square profile assets
06_GUIDE             Production guide
07_VERIFICATION      Source reference and clean vector checks
08_QA                QA report and contact sheets
```

**Status: only this spec has been supplied — the actual vector master
files (01_CORE_MASTERS) have not been shared into this session.**
Documents built since (8 Sept 2026, Johnny pricing note) use the
colour tokens, letterspaced BARBER/REPUBLIC wordmark as styled text,
and the correct tagline, with the Collective Matrix mark itself left
as an explicit placeholder pending the real vector file — per rule 1
above, it must not be redrawn or approximated.

## 9. Open items

- Typography is not specified in the master asset guide. The wordmark
  is a custom vector master, so a UI typeface still needs to be chosen
  and approved before any interface build. Documents built without the
  vector master use a standard serif/sans as a stand-in.
- Name clearance (Companies House, UK trademark, domains) has not been
  confirmed.

**Note:** this identity system (Collective Matrix mark, near-black/
bronze palette, "Intelligence that Builds the Industry" tagline)
supersedes the three earlier logo concepts recovered from git history
(`logo_concept_1_minimalist.png`, `_2_elegant.png`, `_3_techforward.png`,
commit `b02fab7`) — none of those three match this spec and none
should be used going forward.
