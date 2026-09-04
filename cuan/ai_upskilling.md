# AI Upskilling & Understanding

John's personal record of what he is learning about AI — from Shane, from UHL's senior executive training programme, and from the Golden Generation material — kept in one place and cross-referenced against the orchestration systems it should inform: Cuan, Meridian, a future Sales orchestration, and whatever else gets built.

This file is additive. New entries go in the log at the bottom; the alignment map above them is the index.

---

## Purpose

- One place to capture learning, not three places to lose it
- Every entry tagged by source, so nothing gets treated as fact if it's really a note from a slide or a conversation
- Every entry mapped to which orchestration(s) it should feed, so learning doesn't stay stuck as personal notes when it belongs in Cuan's knowledge base or a Meridian manager

## Sources Tracked Here

| Source | What it is | Status |
|---|---|---|
| Shane McCarthy | Technical partner, Meridian co-founder — direct conversations, working sessions, architecture decisions | Ongoing |
| UHL training | The senior executive AI training programme at United Hardware Limited (see `ventures_dossier.md` — €10,000 programme, approved) | Ongoing |
| Golden Generation | The Golden Generation partner toolkit / "Other Side of Sixty" content programme (see `ventures_dossier.md`, `meridian/managers/05-ai-strategy-and-adoption.md`) | Ongoing |
| Anthropic materials | Guides, case studies, and playbooks on AI-native operating models (e.g. Claude Code product documentation) | Ongoing |

## Alignment Map — Where Learning Should Land

| Orchestration | Status | What belongs here |
|---|---|---|
| **Cuan** | Live | Anything that changes how John personally works, decides, or is briefed — feeds `cognitive_pattern.md`, `operating_spec.md`, `voice.md` |
| **Meridian** | Live | Anything client-facing or framework-level — feeds the relevant manager, most often `05-ai-strategy-and-adoption.md` |
| **Sales orchestration** | Not yet built | Flagged here and held until the system exists — same pattern as the Venture Orchestrator noted in `ventures_dossier.md` |
| **Others (as they develop)** | Future | New orchestrations get a row here when they're confirmed, not before |

Nothing in this file gets pushed into another orchestration's knowledge base automatically. Cuan surfaces the cross-reference; John (or Shane, on anything technical) decides if and where it lands, per the Shane Alignment Gate in `governance.md`.

---

## Known Reference Points Already in the Knowledge Base

Captured elsewhere in this repo and indexed here so they're not duplicated or lost:

- **Shane's four-phase AI-native migration model** — Static Foundation / Bolt-On Trap / Architecture Rebuild / Native Operation. Drafted for the UHL AI proposal. Internal only, not for UHL circulation. See `ventures_dossier.md`.
- **Golden Generation Partner Programme** — partner toolkit and onboarding, owned by the Meridian AI Strategy & Adoption manager. See `meridian/managers/05-ai-strategy-and-adoption.md`.
- **UHL AI engagement** — €10,000 senior executive training programme, approved. Two priority use cases: predictive procurement forecasting, automated product marketing for Chinese import lines. See `ventures_dossier.md`.

---

## John's own discipline — flagged gap, 4 Sept 2026

John did the Golden Generation course but has no active daily/weekly
habit keeping him current on AI since — his own words: "really doing
nothing to keep on top of it." He wants to coordinate this into his
work and habits, daily and weekly, not leave it as a one-off course.
No specific cadence decided yet — worth raising as a concrete discipline
to add to `operating_creed.md` (alongside the existing 12pm Council
check-in) once John decides what the actual habit should look like
(e.g. a regular reading slot, a standing prompt, a weekly review).

## Learning Log

Newest entry first. Format: Date | Source | Topic | Key point | Aligns to

| Date | Source | Topic | Key point | Aligns to |
|---|---|---|---|---|
| 2026-08-26 | Anthropic — *Claude Code Guide for Startups* (PDF) | "Trust, but verify" governance model | Cainex (medical billing) case: auditor review of every AI-generated code, versioned change logs, back-testing against a "golden set," and the rule "fix the principle, not the example" so corrections generalise rather than accumulate as patches. A ready-made template for responsible, defensible, verifiable AI adoption. | Meridian (`05-ai-strategy-and-adoption.md`); Cuan `governance.md` (Verification Standard) |
| 2026-08-26 | Anthropic — *Claude Code Guide for Startups* (PDF) | Five rules of AI-native operating models | From 13+ fast-growing startups (ClickHouse, Clay, Harvey, Cognition, Commure, Crosby, Heidi, Cainex, Artemis Security, Omni, and others): (1) Everyone ships — non-technical staff shipping first drafts, kept coherent via shared skills and review cadence; (2) Automate the tedium — agents own the mechanical 80% of the workflow; (3) Trust, but verify — governance and evaluation make automation safe; (4) Build for rebuilding — nothing is precious as model capability shifts; (5) Prototype, dogfood, productionise — internal tools graduate to client-facing product. Working vocabulary: CLAUDE.md, skills, hooks, evals, agent loops, worktrees. | Meridian (`05-ai-strategy-and-adoption.md`) |
| 2026-09-04 | Irish Independent — Peter Flanagan, "I studied a 'useless' philosophy degree, but AI has made it a safe career choice" | Philosophy/judgement as an AI-resistant skill | AI is excellent at automated functions but cannot decide whether something is *worth doing* in the first place — it can be designed to drive a car, do taxes, or drop a bomb, but can't be given values or common sense. Concrete evidence cited: Stefan Heck (CEO, Nauto, ex-philosopher) hires philosophy graduates for trolley-problem-style judgement calls; Sam Altman says OpenAI used "hundreds of moral philosophers" to define ChatGPT's ethical rules; Google DeepMind has hired a philosophy team; tech firms are recruiting philosophy academics directly from Oxford/Cambridge/NYU. A Federal Reserve Bank of New York dataset shows US philosophy graduates now have *lower* unemployment than computer science graduates. **Why John flagged it:** relevant to his own AI upskilling — the judgement/values layer AI can't replace is exactly the space Golden Generation, Meridian's governance framing, and Cuan's own "extends judgement, doesn't replace it" principle are built around. | Cuan (Core Principle cross-reference); Meridian (`05-ai-strategy-and-adoption.md` — governance/human-judgement framing); Golden Generation |
