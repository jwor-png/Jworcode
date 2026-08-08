# ISO/IEC 42001 SELF-ASSESSMENT

## Meridian Intelligence, assessed against the AI management system standard

**Client:** Meridian Intelligence. **Decision question:** *what would it take for Meridian to hold a recognised third-party standard, and does any of it need to happen before the practice trades?*

**Status: IN REVIEW. Not DECISION-READY.**

**The blocker, named as the gate requires.** ISO/IEC 42001:2023 is a paid standard and its normative text has not been retrieved. This assessment is made against the **published structure** of Annex A, being 38 controls across nine objectives A.2 to A.10, and against secondary descriptions of what those objectives cover. It is therefore an assessment at objective level, not at control level. **A control-by-control assessment requires the purchased standard and this document should not be represented to any third party as one.**

*Domains engaged: AI Strategy and Adoption (lead), Legal and Governance, Business Transformation and Growth. Cross-cutting: Evidence gap before advice, Argue-the-other-side, Change-the-answer test.*

---

## EVIDENCE GAP BEFORE ADVICE

Stated before the reasoning, as the floor now requires.

1. **The normative text has not been read.** Objective-level assessment only.
2. **No certification body has been approached.** Cost and duration for a practice of this size are unknown and are not estimated below.
3. **Whether a sole-practitioner practice can certify at all** is unverified. Some standards assume organisational separation of duties that one person cannot provide.
4. **The floor has one day of operating history.** Design maturity and evidential maturity are different things, and that distinction runs through everything below.

---

## THE NINE OBJECTIVES, ASSESSED

| # | Objective | Status | Basis |
|---|---|---|---|
| A.2 | **AI policy** | **Partial** | `meridian-orchestrator.md` functions as an AI policy in substance: purpose, scope, governance floor, boundary, operating modes. It is not framed as a policy with an owner, an approval and a review cycle. |
| A.3 | **Internal organisation** | **Partial, with an inherent limit** | Roles are defined and the human gate is now a named person with recorded attestation. But John is producer, reviewer, gate and owner. **Segregation of duties is provided by the machine critic, not by a second person.** That is a real limitation and it should be declared rather than dressed up. |
| A.4 | **Resources** | **Substantially met in design** | The Map documents the domains and skills. The version and reproduction record added today captures models, sources, skills invoked and gate identity. |
| A.5 | **AI impact assessment** | **Gap** | Meridian has no assessment of the impact of its own system on the individuals and organisations affected by its outputs. This is a genuine absence, not a documentation shortfall. |
| A.6 | **AI system lifecycle** | **Substantially met in design** | `How to Write a Slice` is a documented lifecycle process. Capability acceptance testing added today is the verification stage. Git is the change control and the version spine. **Missing: retirement.** There is no rule for withdrawing a skill that stops behaving, and no in-operation monitoring. |
| A.7 | **Data for AI** | **Partial, and narrower than it looks** | The grounding rule is provenance discipline for evidence, and information governance for client material went in today. **Scope note that helps: Meridian trains nothing.** It retrieves and reasons. A large part of this objective concerns training data and does not apply, which should be stated as a scope reduction rather than left ambiguous. |
| A.8 | **Information for interested parties** | **Strongest area** | The boundary, the three status labels, VERIFIED / REPORTED / UNVERIFIED tagging, and the two-page client explainer are precisely this objective. A client is told what the system is, what it is not, what it warrants and where it refuses. |
| A.9 | **Use of AI systems** | **Substantially met in design** | Fail-closed, mandatory human gates on four domains, operating modes matched to stakes, the ten-point release gate, and the rule that the engine cannot grade its own work down to skip a gate. |
| A.10 | **Third-party relationships** | **Gap, and it is a business risk before it is a compliance one** | Meridian depends entirely on third-party model providers. Nothing documents that dependency, the terms it runs on, what happens if a provider changes, restricts or withdraws a model, or what the fallback is. **This week's own market intelligence recorded a live instance: export controls were placed on a frontier model provider and later lifted.** A practice selling continuity of judgment has no documented answer to that. |

**Score: four substantially met in design, three partial, two gaps.**

---

## THE DISTINCTION THAT MATTERS MOST

**Met in design is not met in evidence, and certification tests the second.**

A management system standard is not awarded for having good rules. It is awarded for demonstrating that the rules operated, over a period, with records, internal audit and management review to show it. Meridian's floor has operated for one day. Even the four strong objectives could not survive an audit today, not because the controls are weak but because there is nothing yet to sample.

**That is not a reason to delay. It is the reason to start recording from the first engagement rather than the day certification is decided on.**

---

## WHAT IT WOULD COST, IN THREE BANDS

**Free, and worth doing inside half a day.** Four documents, all writing, no external spend.

1. **Reframe the orchestrator floor as an AI policy** with an owner, a date, an approval and an annual review. The content exists. It needs a wrapper. *(closes A.2)*
2. **An AI impact assessment for Meridian itself.** Who is affected by a Meridian output, how, what could go wrong, what the mitigation is. One document, reviewed annually. *(closes A.5)*
3. **A third-party dependency register.** Which models, from whom, on what terms, what the concentration risk is, what the fallback is if one becomes unavailable. *(closes A.10, and answers a real commercial question)*
4. **A retirement rule.** How a skill is withdrawn or suspended when it stops behaving, and who decides. Three lines in the orchestrator. *(closes the A.6 gap)*

**Cheap, and it accrues rather than costs.** Keep the records from engagement one: the audit record per matter, corrections made, claims held, critic overturns, gate decisions. This is the evidence base a certification would sample, and it costs nothing except the discipline of not skipping it when busy.

**Real money, and it waits.** Purchase of the standard, a gap analysis against the normative text, an internal auditor, a certification body, the audit itself and annual surveillance. **No figures are given here because none have been verified.** Revisit when there is fee income and six to twelve months of operating records.

---

## ARGUE-THE-OTHER-SIDE

The strongest case against any of this, stated properly.

> Meridian has not issued an invoice on the new price list. A certificate is a credential for a practice with clients, and this practice has none yet. Every hour spent on management-system documentation is an hour not spent on Primeline, Vinny Leonard or DSB Accountants. Worse, an unmarketed practice with an impressive compliance file is a recognisable failure pattern: preparation substituting for exposure. The reviewer's warning was capability outrunning assurance. This risks the reverse.

**That case is largely right, and it shapes the recommendation.** It is why only the four free items are recommended now, why they are capped at half a day, and why the certification track is explicitly deferred rather than scheduled. It is not a reason to do nothing: the third-party dependency register in particular is a commercial answer, not a compliance one, and Meridian should know it whether or not it ever certifies.

---

## RECOMMENDATION

**Nothing in ISO 42001 blocks Meridian trading, and nothing here should be allowed to delay it.**

1. **Do the four free documents.** Half a day, closes both gaps and the weakest partial, and they are useful in their own right.
2. **Keep the records from the first engagement.** That is the whole evidence strategy and it is free.
3. **Defer certification** until there is fee income and six to twelve months of operating history. Then get a real quotation rather than an assumption.
4. **Do not claim ISO 42001 alignment publicly** until at least the four documents exist and preferably not until the standard has been read. The floor forbids it, and claiming a standard one has not read is precisely the failure the grounding rule exists to catch.
5. **Say what is true instead**, which is strong enough on its own: *Meridian operates a documented governance floor, self-assessed against ISO/IEC 42001, with the gaps identified and a route to certification.* That sentence is defensible today. "Certified" is not.

---

## CHANGE-THE-ANSWER TEST

**Current recommendation:** four free documents now, certification deferred.

**It changes if:**

- **A client, insurer or procurement process makes certification a condition of engagement.** Then it moves from deferred to required, and the cost stops being optional. Most likely to arise with a public-sector or regulated client.
- **Ambrion decides to sell ISO 42001 readiness as a product.** That is a natural tier alongside its EU AI Act compliance offering, and it changes the economics completely, because the learning becomes billable rather than overhead and Meridian becomes the reference implementation.
- **A model provider dependency actually bites.** If a provider withdraws, restricts or materially changes a model mid-engagement, A.10 stops being a compliance gap and becomes a live continuity failure in front of a client.

**Unknowns capable of changing it:** whether a sole-practitioner practice can certify at all, and what a certification body would actually charge a business this size.

**What should be checked next:** one conversation with a certification body, for eligibility and an indicative cost. That is a phone call, not a project, and it converts the two largest unknowns into facts.

---

*Meridian Intelligence · ISO/IEC 42001 self-assessment · 7 August 2026 · Private and confidential. **Status: IN REVIEW.** Assessed at objective level against the published Annex A structure, not against the normative text, which has not been retrieved. Annex A structure verified from ISO and secondary sources, August 2026. Not to be represented to any third party as a control-level assessment or as evidence of alignment.*

**Sources:** [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) · [ISO 42001 explained](https://www.iso.org/home/insights-news/resources/iso-42001-explained-what-it-is.html) · [BSI](https://www.bsigroup.com/en-US/products-and-services/standards/iso-42001-ai-management-system/)
