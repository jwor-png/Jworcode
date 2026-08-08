# Meridian Architecture

Canonical description of what the Meridian engine is made of.

**The pack is complete.** Built with Shane, 29 July 2026. Filed by John, 7 August 2026.

| File | What it is | Status |
|---|---|---|
| `00_START_HERE.md` | The pack's own cover note and reading order. | **Canonical** |
| `01_Meridian_Map.md` / `.pdf` | Suite I. The anatomy: 7 managers, 50 skills, tiering, and the shared floor. | **Canonical** |
| `02_Meridian_Wiring.md` / `.pdf` | Suite II. How intent becomes a defensible decision. **Read the markdown: it is materially richer than the PDF and carries the Boundary, which the PDF does not.** Co-authored John Webb O'Rourke and Shane McCarthy. | **Canonical** |
| `03_How_to_Write_a_Slice.md` / `.pdf` | Suite III. The seven-step template for adding a skill, and the note on cross-cutting skills. | **Canonical** |
| `04_Six_Slices_to_Add.md` | Six further skills, written and placed, each with the exact line and its home manager. | **Canonical, not yet applied** |
| `INSTALL_upgrade_Meridian.md` | The self-upgrade instruction. Takes the engine from 50 skills to 56. | **Not yet run** |

Every document is now filed in both markdown and, where it exists, the finished PDF. **Read the markdown, show the PDFs.**

---

## THE BOUNDARY, which only appears in the markdown Wiring

> **"Meridian informs you. It never represents you or a client. A signature, a filing, a conveyance, anything a client leans on, goes to a qualified professional before you act. Meridian is the experienced team behind you. The judgement at the front is always yours."**

This is the most commercially important sentence in the entire pack and it is absent from the PDF version. It is the professional-liability firewall, and it does three things at once:

1. **It scopes the professional indemnity question.** Meridian advises, it does not act, sign, file or convey. That is a materially narrower risk profile than a firm that does, and it is the right way to present the practice to an insurer.
2. **It is the answer to "are you not just practising law or accountancy without the ticket."** Anything binding routes to a qualified professional before it is relied on, and that rule is written into the skills themselves.
3. **It should appear in every client-facing document Meridian issues**, in Meridian's own words rather than as small print.

## MERIDIAN'S FOUR JOBS

**Classify** the question. **Route** it to every manager it genuinely touches. **Consolidate** their work. **Return** it with a status and a short record of how it was checked.

## THE FLOOR, in the fuller markdown form

- **The grounding rule.** No statute, case, figure, title fact or valuation reaches you unless it was pulled from its primary source *and the passage actually supports it*. Anything from memory is never treated as fact. **Every hard fact is tagged VERIFIED, REPORTED or UNVERIFIED, and a citation that will not resolve is held, not shipped.**
- **The independent critic.** A separate agent on a stronger model re-reads the work against the original source. *"The one who makes the work and the one who checks it are never the same, so they do not share the same blind spot."*
- **A status on everything.** DRAFT, IN REVIEW, DECISION-READY, and if it is not there yet Meridian says exactly what is missing.
- **Fail closed.** Near a legal, financial or regulatory line, or below 80 per cent confidence, it holds and pulls the human in rather than guess.
- **The human gate.** On the four high-stakes managers, anything to be acted on stops. **"Meridian cannot quietly grade its own work down to skip that."**
- **The audit record.** Who produced what, from which sources, what the critic found, and the status. Every answer can show its own lineage.

> **"A tool that gives an answer is common. A tool that gives an answer and can show exactly how it reached it, and where it refused to guess, is rare... The floor is not overhead. The floor is the product."**

## ONE ARCHITECTURAL PROPERTY WORTH KNOWING

A new skill *"inherits the grounding, the independent critic, the status label and the human gate for free, just by living inside a manager."* The floor is not re-implemented per skill. That is why the engine can go from 50 to 56 with six pasted lines and no loss of rigour, and it is a genuinely strong answer to anyone who assumes the discipline is manual effort that degrades as scope grows.

### How to Write a Slice — the seven steps

1. Say it in one plain sentence. 2. Place it under the manager that already thinks that way. 3. Match the shape of the skills already there. 4. Write one line and save. 5. It is live at once, no rebuild, no code. 6. Prove it, point a quick question at it. 7. Lock it, a git commit, so it is on the record.

> *"One new line, in the same shape, and the system reads it as its own. Same as its brothers."*

### Upgrade readiness check, run 7 August 2026

- The manager files in this repository **do** carry the `## Sub-agents (the slices)` heading the upgrade targets, and the existing slices follow the house form the upgrade expects. **The six lines would paste cleanly.**
- `06-business-transformation.md` **does not** yet contain What-else scan. **This repository is John's copy, not the master engine**, where that skill has been live since 29 July.
- No duplicate names exist for any of the six. Nothing would be skipped.

**The upgrade has not been run.** The pack is written so John applies it himself, and the INSTALL file provides for Meridian doing it on his express instruction. Awaiting that instruction.

---

## THE WIRING — the four floor rules

These are the sharpest defensibility material in the entire body of work.

**Grounding rule.** No statute, figure or fact ships unless it was pulled from its primary source. *"From memory is never fact."*

**Status labels.** Draft, in review, decision-ready. Only decision-ready means it can be relied on, **and the blocker is always named.**

**Fail closed, and the human gate.** Near any line, or **below 80 per cent confidence**, it holds and pulls the human in. **The high-stakes four always stop.**

**Audit trail.** Who produced it, from which sources, what the critic found, at what confidence. **Every answer shows its lineage.**

And the line that carries the whole argument:

> **"The floor is not overhead. It is the product."**

### The flow

One brief in, stated as intent in plain language. Meridian classifies it and routes to every manager it touches. The managers **fan out, not in**, worked in parallel rather than one at a time. **A separate critic agent, running on a stronger model, re-reads the source.** One consolidated, labelled answer out.

### The worked example, which is the best sales illustration on file

> A tight cash brief on a Galway builders' merchant routes to Finance, Business Transformation and Legal at once. Each works it, the critic checks the numbers, and Meridian returns one answer: the true cash position, the two fastest wins, the directors' duties flag, and the succession talk that is coming. One brief in, one defensible answer out.

That is a Decision Brief described end to end, in a sentence an owner-manager would recognise.

---

## THE SIX SLICES — 50 to 56

| # | Skill | Home manager | What it does |
|---|---|---|---|
| 1 | **Read-this-for-me** | Legal and Governance | Contract, lease, term sheet or email dropped in. Returns what matters, what bites, what to push back on. Binding items flagged for a qualified solicitor. |
| 2 | **Meeting-prep brief** | Commercial and Deal | One grounded page before any room: who is being met, their likely position, where the leverage sits, the two or three things that could go wrong. |
| 3 | **Argue-the-other-side** | Legal and Governance *(cross-cutting)* | Red-teams Meridian's own recommendation, sets out the strongest case against it, names where it would break. |
| 4 | **What-else scan** | Business Transformation | At the close of any matter, surfaces the adjacent work the client needs next. **Built live 29 July and already running in the master engine.** |
| 5 | **Say-it-to-the-client** | AI Strategy and Adoption *(cross-cutting)* | Renders any grounded technical output as a clean plain-English page to hand straight to a client, accuracy intact, sources kept. |
| 6 | **Obligations and deadlines schedule** | Legal and Governance | Every date, statutory clock, filing and obligation into one schedule, with directors' duties and liability flags. |

Three of the six land in Legal and Governance, which is consistent with it being the heaviest manager and closest to John's own instinct as a former solicitor.

The older per-manager notes in `meridian/managers/` predate this Map. Where they differ, **the Map governs.**

---

## What the Map adds that the commercial documents did not have

Three things, and all three strengthen the Shane briefing.

**1. The shared floor, stated as architecture rather than as a habit.**

> *"Nothing reaches you unless it can show where it came from, every output is re-checked by an independent critic, and every answer carries a status (DRAFT, IN REVIEW, or DECISION-READY) so a draft is never mistaken for ready."*

The defensibility argument in the Shane briefing rests on the verification discipline. This is that discipline expressed as a designed property of the system, with an independent critic stage and a three-state status label. That is materially stronger than describing it as a practice, because a practice can lapse and an architecture cannot.

**2. Tiering, with a mandatory human gate on the high-stakes managers.**

Standard tier: Commercial and Deal, AI Strategy and Adoption, Business Transformation and Growth.

High-stakes tier, carrying a mandatory human gate before anything is acted on: Legal and Governance (named the heaviest specialist, Irish law throughout, grounding rule absolute), Finance and Restructuring, Property and Development, AI Equity and Investment (with a frontier caveat: numbers grounded hard, thesis marked as judgement).

This is a governance design, not a disclaimer. It is the single most credible answer to any question about whether a board can rely on the output.

**3. Fifty named skills.**

"Seven domains" is an assertion. Fifty named skills, each with a one-line description of what it does, is a specification. Several map directly onto commercial claims already made:

- **Equity-for-AI-capability** (Manager 7) is precisely the AI Equity Structuring product: the contribution valued, the equity it earns, the terms.
- **Term sheet drafting** (Manager 1) and **equity structure modelling** (Manager 7) are the Barber Republic work described in the engine's own vocabulary.
- **Comparable transactions** (Manager 4) carries the rule *"real comparables, each grounded, never estimated"*, which is the verification discipline visible at skill level.
- **Directors' duties** (Manager 2) is named top priority within the heaviest manager, which is exactly the governance-inside-a-decision scoping proposed for Manager 2 in the boundary work.

---

## One conflict to resolve

The Map describes **Manager 5, AI Strategy and Adoption**, as *"your forward-facing commercial manager, where the Meridian Intelligence service offer is shaped."*

The boundary work of 5 August recommends the opposite: that Manager 5 comes **off** Meridian's shopfront and stays in the engine, with AI readiness, EU AI Act compliance, governance audit and adoption roadmaps routing to Ambrion and Velocity.

Both cannot stand. The likely explanation is that the Map's description of Manager 5 dates from when Meridian was positioned as an AI advisory business, which was superseded on 31 July and again on 5 August when Meridian was confirmed as an executive intelligence practice selling the decision brief.

**Recommendation: keep all seven Manager 5 skills in the engine, and retire the description of it as the forward-facing commercial manager.** Manager 6, Business Transformation and Growth, is the better candidate for that role and the Map already calls it *"the most likely entry point for a live matter."* That is a one-line change to the Map, not a change to the engine.

**Consequence for slice 5, now resolvable.** Say-it-to-the-client is placed in Manager 5 *"because this manager already shapes client-ready material."* If Manager 5 comes off the shopfront, that reason goes with it. Document 03 gives the answer: cross-cutting skills *"are not added to a manager file; they go into the orchestrator file itself, where the rules that apply to the whole system live."* Both Say-it-to-the-client and Argue-the-other-side are named in the pack as naturally cross-cutting. **Recommendation: apply the six slices as written first, prove them, then lift those two into the orchestrator as a second, separate step.** Do not do both at once, or a failure will be hard to attribute.

*Both flagged for John's decision. Neither actioned.*
