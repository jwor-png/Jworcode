# Meridian Intelligence — Website Design Brief

Shared brief between **Cuan** and the dedicated **Meridian Website** chat thread.
Cuan holds this in full; the website thread reads it, builds against it, and
writes decisions back here so nothing is lost between sessions.

Status: initial prototype built 1 August 2026. Awaiting real logo/branding.

---

## What exists already

A working HTML prototype has been built and published as an artifact:
**https://claude.ai/code/artifact/f5861093-d562-4c75-ba97-6d04ec811956**

Source file (this machine's scratchpad, may not persist):
`meridian-intelligence.html`

That prototype is a single-page site, fully responsive, light and dark mode,
no external dependencies. It is a starting point and a spec to hand to
Lovable, not a finished product.

---

## Outstanding blocker — real branding

The prototype uses a **placeholder palette I invented**, not Meridian's actual
brand. John has confirmed real branding exists on the Meridian Overview
document.

- `logo.png` exists in Google Drive (folder `Gmail Attachments`, file ID
  `1-tClgslPAhxM4_etHl8wayYn00BesIVv`, 248x239px) but **downloads corrupted /
  truncated via the Drive API** — decodes partially then breaks. Could not be
  used.
- `Meridian_Overview_Branded.pdf` (Drive ID `1n65Oz44R9jg_qMM3Bch5jqEcx57b1JjB`)
  contains the real branding and is the better source.
- **Next step:** John to upload the logo or branded overview PDF directly into
  the website chat thread (direct upload works where Drive download failed),
  then replace the placeholder palette and drop in the real mark.

---

## Design direction (agreed)

Reference sites John reviewed and liked the direction of — all boutique,
principal-led advisories rather than big AI vendors:
- **Trifecta** (NY growth studio) — editorial feel, elegant serif, navigation
  styled like a magazine contents page.
- **Primary Studio** — elegance plus pricing transparency (states a flat fee
  openly).
- **Josh Kremer Consulting** — deliberately minimalist, heavy white space,
  fast to skim.

Common principles carried into the build:
- State who you help and how, above the fold.
- **Name the principal** (John, as Chairman) — prospects should see a named
  person, not a faceless firm.
- Keep visual noise low so the seven domains and the expertise are what stand
  out. This matches John's stated preference elsewhere for white background and
  minimal ink.

---

## Concept behind the prototype

Built around the literal meaning of *meridian* — a fixed line of reference:
- A thin brass "meridian line" runs down the spine of the page with tick marks,
  like a longitude line on a navigational chart (drawn on canvas, theme-aware).
- A coordinate line in the hero: `53.4239° N · 8.4854° W · EST. 2026`.
- The seven domains numbered 01–07 like manifest entries — honest here, because
  Meridian genuinely is built around exactly seven named domains.

---

## Placeholder tokens (TO BE REPLACED with real brand)

Light mode: paper `#FAFAF8`, ink `#14181F`, ink-soft `#4A5160`,
brass accent `#A6791F`, line `#D8D9D4`, card `#FFFFFF`.
Dark mode: paper `#14171C`, ink `#EAE8E1`, ink-soft `#9BA1AC`,
brass `#C79A3F`, line `#2A2E36`, card `#1B1F26`.

Type: Georgia/Iowan Old Style serif for display (quiet authority, chambers
feel); system sans for body; monospace for coordinates and numbering.

---

## Page structure built

1. **Sticky nav** — wordmark, links to Domains / Approach / Chairman / Contact.
2. **Hero** — eyebrow "Executive Intelligence Advisory", headline "A fixed
   point for *complex* decisions.", lede, coordinate line.
3. **Thesis** — "Every business eventually faces a decision no dashboard can
   make for it." Two-column, sets up the seven-domains-one-accountability idea.
4. **Seven Executive Intelligence Domains** — numbered grid, each with the
   agreed one-line description (matching the pocket card and overview doc).
5. **How an engagement runs** — four stages: Entry / Assign / Advise / Stand By.
6. **Principal** — John Webb O'Rourke, Chairman & Founder. Four decades of
   commercial pattern recognition; chairs every engagement personally.
7. **Contact** — "Start with the decision in front of you." CTA mails
   jwor@meridianintelligence.ie.
8. **Footer** — "SEVEN DOMAINS · ONE POINT OF ACCOUNTABILITY".

---

## Source content for copy

All domain descriptions and positioning language should stay consistent with:
- `Meridian_Overview_Branded.pdf` (Drive) — the fullest version, includes the
  sector lens (agribusiness/food/retail/co-op, healthcare/primary care/dental,
  property/construction/hospitality, hardware/builders' merchants) and worked
  examples of domains combining on a real decision.
- `Meridian_One_Pager.pdf` (Drive) — shorter version, "seven managers" framing.
- `cuan/ventures_dossier.md` — Meridian section, partnership structure,
  confidentiality rules.

Note the two documents use slightly different language ("Seven Managers" vs
"Seven Executive Intelligence Domains"). The website prototype uses **Domains**.
Confirm with John which is the settled external-facing term.

---

## Open decisions for John

1. Real logo and brand palette — blocked pending direct upload.
2. Single landing page, or multiple pages (Home / Domains / About / Contact)?
3. Audience — prospective clients only, or investors too?
4. "Domains" vs "Managers" as the settled public term.
5. Whether to follow Primary Studio's lead on stating fees openly. Meridian's
   fee structure was still being located as of late July.
