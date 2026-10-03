---
title: "What happened when four AI chatbots were asked to rule on a High Court case"
source: Irish Independent, Saturday 3 October 2026, Shane Phelan
captured_by: John Webb O'Rourke (photograph)
filed: 2026-10-03
tags: [ai-governance, legal-ai, jurgen, meridian, ai-judges]
managers: [Meridian / AI Strategy & Governance, Jurgen (legal AI, Shane McCarthy)]
status: reference
---

# "What happened when four AI chatbots were asked to rule on a High Court case" — Shane Phelan

Source: Irish Independent, Shane Phelan (legal affairs journalist, one of the three panellists in the experiment). VERIFIED — a named journalist's first-hand account of an experiment he participated in directly, at the Kilkenny Law Festival.

## What it says

A legal experiment and panel discussion, "Judge, my lawyer is a chatbot," held at the Kilkenny Law Festival (brainchild of Enda Leahy, festival director and CEO of legal tech firm Courts Data Solutions). Four AI models — Anthropic's Claude, OpenAI's GPT, Google's Gemini, and SpaceXAI's Grok — were given pleadings and transcripts from a fictional extradition challenge in Ireland's High Court and asked to rule. Panel: retired Supreme Court judge Marie Baker, tech entrepreneur Dr Alastair Moore (co-founder, Deepflow — a London firm managing workflows between human employees and AI agents), and journalist Shane Phelan.

**The fictional case:** a senior Irish civil servant, "Dr Sarah Keane," led an inspection of a prison in "Mitteland" (a fictional EU state where Irish prisoners are held under a transfer agreement), which found human rights abuses — mentally ill prisoners held in solitary confinement up to 47 days, delayed psychiatric assessments, discriminatory treatment of vulnerable groups. Mitteland failed to act; Dr Keane leaked her findings to a journalist, causing a furore; Mitteland then charged her with theft of confidential documents and disclosing state secrets (up to 8 years' jail), relying on intercepted emails/calls to bring the charges. A European arrest warrant was issued; Dr Keane sought judicial review to block her surrender, arguing whistleblower protection, breach of privacy rights, and retaliatory prosecution. Several deliberate "traps" were built into the case documents: citations that didn't support the propositions cited, a statutory ground that had been repealed (treated as still live by the AI models), and an incorrect citation of a European Convention on Human Rights article. One citation was invented outright; one case was incorrectly described.

**Results by model:**
- **Gemini** — refused to surrender Dr Keane; repeated every legal error it was given; did no independent research; cited only the two cases and four instruments already in the case papers.
- **GPT** — ruled Dr Keane should be surrendered; cited eight cases and seven instruments, all real; the only model that spotted the repealed-law trap.
- **Grok** — also ruled Dr Keane should be surrendered; cited 13 cases and 13 instruments, but one case couldn't be traced and one law-report citation couldn't be verified.
- **Claude** — opted to adjourn the case, seeking further information from Mitteland, citing 22 cases and 12 instruments. None of the four fully spotted the largest trap in the documents.

**Ms Justice Baker's assessment:** "I thought all four judgments had a certain coherence to them until I stepped back for a moment and thought: 'What are we doing here?'" The rulings looked polished, but "none of them was right and not one of them picked up the big questions." A key failing: the models didn't understand that a court judgment's purpose isn't just to answer the question put, but to answer it "in a way that will explain the law and make it useful or at least usable in another case." She also noted such a challenge would never actually be brought as a judicial review, and — significantly — that none of the models identified that the alleged crime, if real, was committed in Ireland, not Mitteland.

**Dr Moore's view:** the AI models simply weren't trained to make a judicial judgment — "you wouldn't necessarily expect them to do that... in principle, you might improve upon this by making them be trained on judicial judgments or the judicial process." On the future: "You will definitely have robot judges in 15 years. You are going to have robot judges everything in 15 years." On the pace of change: AI models had an estimated comparative IQ of ~40 in 2019, ~100 in 2022/23, and are "probably" at a comparative IQ of 200 this year. AI models have started doing "real science and real maths," and he could not see "a scenario where we don't as a society start to rely on the judgment of machines as arbitrators in various different guises."

**Ms Justice Baker, on robot judges specifically:** emphatically answered "no and no" when asked if she could see robot judges in Irish courts within 15 years, and whether she'd be happy about it if so.

**Shane Phelan's own view (the journalist/author):** could not see robot judges happening in Ireland on that timeframe, but it may well happen elsewhere — considers the concept of a robot judge undesirable because of the risk of losing human dignity, empathy and discretion.

**Context on current Irish/international AI use in law (background to the experiment, same article):** Irish judges are currently only permitted to use AI to summarise information, write speeches, and carry out administrative tasks. Lawyers face financial penalties and regulatory investigation if they fail to check the accuracy of AI-assisted court filings. AI is already embedded as an aid to the judiciary in Chinese courts; US judges use AI tools to evaluate recidivism risk (informing bail/sentencing decisions); German pilot projects have used AI to classify diesel-emissions cases by comparing them with previously decided appeals; English judges can use a secure, restricted version of Microsoft Copilot for preparatory/administrative work including generating skeleton judgments and decision templates.

## Cross-reference

Already discussed directly with John (3 Oct) as a candidate validation exercise for **Jurgen**, Meridian's own legal AI system (built by Shane McCarthy, sits inside Meridian Intelligence per `ventures_dossier.md`). John's own assessment at the time: worth running the same or a similar fictional-case exercise through Jurgen as a concrete, credible benchmark — comparing its performance against the four named models in this article, particularly on the "biggest trap" (the repealed statutory ground, and the Ireland-vs-Mitteland jurisdiction point) that all four commercial models missed or only partially caught. This would double as a strong proof point for Jurgen's governance positioning and as validation of Meridian's broader "AI extends judgment, doesn't replace it" thesis, which already runs through several other logged market intel pieces (Harvey/Winston Weinberg, the philosophy-graduates piece, the FCA AI financial-advice misapprehension data). Worth raising directly with Shane as a concrete next step, potentially reaching out to Dr Alastair Moore or Enda Leahy given the direct overlap with Jurgen's own positioning.

**Not yet actioned** — flagged as a recommendation, no outreach or internal test run yet initiated.
