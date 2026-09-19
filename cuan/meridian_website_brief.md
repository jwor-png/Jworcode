# Meridian Intelligence — Website Design Brief

Shared brief between **Cuan** and the dedicated **Meridian Website** chat thread.
Cuan holds this in full; the website thread reads it, builds against it, and
writes decisions back here so nothing is lost between sessions.

Status: full site built on branch `claude/meridian-new-website-s043eq`
(2 Sept 2026) — matches the design below, circuit-M logo added to nav/
favicon (low-res, phone screenshot source, fine for small use only).
**Not deployed anywhere. No hosting or domain decision made.** See
"Launch sequencing" below — this is the current blocker, not branding.

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

## Blocker resolved — 19 Sept 2026

`Meridian_Overview_Branded.pdf` pulled directly from Google Drive (file ID
`1n65Oz44R9jg_qMM3Bch5jqEcx57b1JjB`) — downloaded clean this time, byte count
matched Drive's reported size exactly (964,731 bytes), no truncation. The
earlier corrupted-download problem was specific to the standalone `logo.png`
Drive file, not the PDF.

**Assets extracted and saved to `cuan/assets/`:**
- `Meridian_Overview_Branded.pdf` — the source document, all 3 pages.
- `meridian_logo.png` — the real logo extracted directly from the PDF's
  embedded image at full resolution (1070×960px), not the corrupted
  248×239px Drive thumbnail. Circuit-pattern "M," blue-to-teal gradient,
  "MERIDIAN" wordmark, "INTELLIGENT AI. REAL IMPACT." tagline, on a
  near-black navy background.

**Real brand palette, sampled directly from the logo pixels (not
invented/estimated):**
- Background navy: `#050F1E`
- Electric blue (left side of the M / gradient start): `#009FFE`
- Teal-green (right side of the M / gradient end, also used for section
  underlines and small-caps labels in the overview doc): `#06B499`
- White for headline/wordmark text; near-black (`#0A0A0A`-ish) body text on
  white page backgrounds in the overview document itself.

**Rebuild done, 19 Sept 2026.** Pulled the existing site build from
`claude/meridian-new-website-s043eq` (`website/index.html`, `styles.css`,
`script.js`, plus its existing asset files) into this branch's working
tree at the same `website/` path, and re-skinned it with the real
branding:
- Replaced the invented placeholder palette (paper/ink/brass) with the
  real one sampled above — `--brass` now holds the real teal
  (`#048C79` light / `#06B499` dark), added a `--blue` variable
  (`#0B7FCC` light / `#009FFE` dark) used for the hero's italic
  "complex" and available for further accent use. Dark-mode background
  changed to the real navy `#050F1E` (was a generic dark grey).
- Cropped a clean square icon (`website/assets/meridian-mark.png`, 512×512,
  navy-padded circuit-M) directly from the real logo, and regenerated
  `favicon-256.png` from it — replaces the low-res phone-screenshot
  version. Removed the unused duplicate `meridian-logo.png` asset.
- Swapped the Chairman section's fake circular "M" placeholder for the
  real mark image.
- Updated `script.js`'s canvas "spine" line colour from brass to the real
  teal RGB values.
- **Fixed a genuine layout bug found while testing, unrelated to
  branding:** the seven-domain grid left a dangling empty cell (2-column
  grid, odd count) — the 7th domain now spans full width instead.
- Verified visually via a headless-browser screenshot pass, light and
  dark mode, desktop and mobile.

**Known pre-existing issue, not fixed, flagged for a decision:** on
narrow mobile widths the top nav links overlap the wordmark — there's no
mobile menu collapse in the original build. Present before this rebrand
too; not addressed here since it's a layout fix, not a branding one.

**Not yet done:** deploy/hosting/domain decision (see Launch sequencing
below) — this rebuild only updates the local working copy on
`claude/trusting-volta-8gtmab` at `website/`, it has not been pushed to
or merged with the separate `claude/meridian-new-website-s043eq` branch.

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
"Seven Executive Intelligence Domains"). **SETTLED (John, 1 August 2026):
"Domains" is the external-facing term.** Use "Seven Executive Intelligence
Domains" consistently on the website and in any new client-facing material.
"Managers" is internal architecture language only and should not appear
externally.

---

## John's reinforcement, 9 Sept 2026 — money being spent on nothing live

John flagged this again directly: he's paying the **Hosting Ireland
invoice every month** for a website that isn't set up or live, and he
wants to complete the email and website setup properly rather than
keep paying for an unused package. No new facts, but explicitly
reinforces this is not a "someday" item — it's live spend against
nothing delivered, every month it stays unresolved.

## Launch sequencing — website + Google Workspace email, same domain (2 Sept 2026)

Both the site launch and the Google Workspace switch-over touch DNS on
**meridianintelligence.ie** (registered with Hosting Ireland, currently
pointed entirely at Hosting Ireland — mail and hosting, no Google records
present). They must be sequenced together or one breaks the other.

**Current state:**
- Google Workspace Business Starter trial started 11 June under admin
  `jwor@meridianintelligence.ie`, converted to paid ~25 June, hit a
  **payment failure 1 July never confirmed resolved.**
- Niamh tried to help set it up but got redirected into Google's "new
  signup" flow — she isn't signed in as the actual admin account.
- Separate, unrelated: a Hosting Ireland invoice (€14.70, "Cloud Lite
  Plus") for the existing hosting package is due 11 August.

**Recommended sequence — do not run these two workstreams in parallel:**
1. **Recover access to `jwor@meridianintelligence.ie`** — password reset,
   most likely via John's Gmail as the recovery address. Nothing else can
   proceed until this account is actually accessible.
2. **Fix the failed payment method** on the Workspace subscription once
   logged in, and add Shane as the second user.
3. **Decide where the website will actually be hosted** before touching
   any DNS — the site currently exists only in the GitHub repo, unhosted.
   Needs a hosting decision (e.g. Vercel/Netlify/Hosting Ireland itself)
   before step 4 can be planned concretely.
4. **Update DNS at Hosting Ireland once, as a single coordinated change**
   covering: MX/SPF/DKIM records pointed at Google (for mail), and
   whatever A/CNAME records the chosen host needs for the site (root
   domain and/or a subdomain — e.g. does the site sit on the root domain
   or on `www`, and does that clash with where mail expects to land).
   Doing mail and site DNS changes separately, on different days, is what
   risks one breaking the other — same change window, reviewed together.
5. **Pay the outstanding Hosting Ireland invoice (€14.70, due 11 Aug)**
   regardless of the above — it's for the existing hosting package and
   unrelated to the Workspace/DNS decision, no reason to let it lapse.

**Needs John's sign-off before anything is actioned:**
- Confirming `jwor@meridianintelligence.ie` recovery goes to his Gmail
  (verify that's still the correct recovery address before relying on it).
- The actual hosting choice for the site (step 3) — this is a real
  decision, not just a technical default.
- Final go-ahead on the single DNS change window (step 4), since a
  mistake here risks live email going down, not just the website.

**Not yet resolved — flagged rather than assumed:**
- Whether the site should sit on the root domain or a subdomain relative
  to where mail needs to route — depends on the hosting choice in step 3.
- No original high-resolution Meridian logo file exists yet — the
  low-res phone-screenshot version in the site nav/favicon is fine for
  now but will need replacing before any serious print/large-format use.

## Open decisions for John

1. Real logo and brand palette — blocked pending direct upload.
2. Single landing page, or multiple pages (Home / Domains / About / Contact)?
3. Audience — prospective clients only, or investors too?
4. ~~"Domains" vs "Managers"~~ — SETTLED, use **Domains** externally.
5. Whether to follow Primary Studio's lead on stating fees openly. Meridian's
   fee structure was still being located as of late July.
