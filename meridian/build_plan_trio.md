# Meridian -- Build Plan: The Trio (Commercial Wrapper, Sprint 1)
*From Shane, off the phone call with John, 30 June 2026. Shane's proposed first commercial build for Meridian. Reviewed and signed off by John. DRAFT pending John's two answers below.*

---

## The frame: one system, not three gadgets

The three pieces feed each other. Separately they are tools. Together they are a funnel: capture demand, convert it to a paid deliverable, multiply the distribution. Every piece is mostly a re-skin and wire-up of things that already exist (the ingestion-form engine, the document production, the seven managers, the governance floor). That is the only reason this is days, not months.

---

## Piece 1 -- The Diagnostic (the front door)
**Working name: Meridian Exposure Check.**

A single branded web page. An SME owner answers 10 to 15 questions about how they use AI, what client data it touches, what decisions it automates, their sector. On submit it returns an indicative read: which EU AI Act risk tier they likely sit in, where they are exposed, a readiness score, and a "here is what to do next" that routes the lead straight to John.

- **Why it makes money:** top of the funnel for the one demand that is live and panicked now, AI Act exposure. John or a partner can send it out tomorrow to generate warm, pre-qualified leads. It doubles as the structured intake feeding Piece 2.
- **Reuse / speed:** the ingestion-form engine is already built. This is a re-skin, a new question set, a scoring rule. One to two days.
- **Guardrail:** it is decision-support, not legal advice, and every output says so. In a legal-adjacent product that honesty is the credibility, and it keeps John on the right side of the boundary.

## Piece 2 -- The Brief Engine (the product John actually sells)
**Working name: Meridian Brief Engine.**

A repeatable pipeline. Takes the diagnostic intake (or a short brief John types) and runs the real Meridian chain: Manager 5 pulls the AI Act obligations grounded to EUR-Lex, Manager 2 holds the legal line, the cross-model critic checks it, the governance floor clears it. Out comes a finished, branded, decision-ready document, PDF and Word, with the verification and audit record attached as part of the deliverable.

- **Why it makes money:** this is the SKU. A fixed-fee compliance brief or readiness report, sold at advisory value, near-zero marginal cost after the first. The attached audit trail is the premium, what lets John charge for proof rather than opinion.
- **Reuse / speed:** managers, grounding retrieval, critic and document production all exist. Build the fixed template, the brand wrap, and the command that chains it reliably. Two to four days.
- **The compounding bit:** architect it so the same engine, with a different question set and source set, also produces a due-diligence report or a growth roadmap. Build the AI Act instance first (demand is live), then mutate the same engine to the next SKU. Prove one blueprint, then widen.

## Piece 3 -- The Partner Pack (the multiplier)
**Working name: Meridian Partner Pack.**

A white-labellable kit that wraps Pieces 1 and 2 so a trusted accountant, solicitor or consultant runs it under their own brand: their-branded diagnostic, a one-page explainer, a sample brief, a clean way to send a client through and get a co-branded output back. John takes a referral or licence cut.

- **Why it makes money:** the leverage play. Distribution through other people's client books, revenue beyond John's own hours. The difference between John billing his time and John earning while he sleeps.
- **Reuse / speed:** mostly packaging and a light re-brand over 1 and 2, plus a one-pager and partner-onboarding doc. Manager 5 already has the partner-onboarding slice specced. Two to three days.
- **Honest caveat:** this only earns after 1 and 2 are proven on one real paying client. Build it third. Selling leverage on an unproven product burns the partner relationship, which is the asset.

---

## Why these three (not a scattered set)

Three orphan tools (one AI Act tool, one due-diligence tool, one board-pack tool) do not compound. Three stages of one funnel do. The Diagnostic fills the pipe, the Brief Engine converts it to a defensible paid artefact, the Partner Pack widens the mouth of the pipe. Because the Brief Engine is built to mutate, the due-diligence and growth-roadmap products come almost for free later, off the same spine.

## Sequencing

Build **Piece 2 and Piece 1 together as the first sprint (a few days):** the product and its front door, both mostly wiring existing assets. Prove it by putting one real AI Act brief through the full floor to decision-ready. Once that one sale lands, build Piece 3 to scale. That order means John has something to sell within days, not a kit to give away before the thing is proven.

---

## TWO DECISIONS SHANE NEEDS FROM JOHN (before he builds)

> "Every one of these goes out in a real name and I will not stand up a multi-day build on a guess."

1. **Whose brand?** ANSWERED by John, 30 June 2026: the trio goes out under the **Meridian Intelligence** brand, fronted by John personally. (Ambrion and Velocity are jointly John and Shane, but this build is Meridian.)
2. **Greenlight and start point.** STILL OPEN. Start with the **Brief Engine** (the revenue core) or the **Diagnostic** (the visible front door)? John to give Shane the word.

**Shane's closing question: "Which one do we light up first?"**

---

## Note for John (Cuan)
The brand decision in question 1 is the same decision as the portfolio overlap flagged in `cuan/business_architecture.md`. Answering "whose brand is the front door" here also starts to answer who owns the front door across Meridian, Ambrion and Velocity. The two are the same question. Worth deciding once, deliberately, with Shane.
