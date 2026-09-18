# John's Personal Skills Architecture v0.1

Authored 18 Sept 2026, following John's own review of a Council/ChatGPT
recommendation to build named, reusable skills from recurring work
(briefings, verified research, board prep, revenue review, transaction
review, meeting prep, proposals, Meridian assessment, Council
reflection, Cuan handover). This document is the single authoritative
architecture all of those skills build against. Do not duplicate the
standards it defines inside an individual skill file — reference this
document instead, and prove that reference actually works before
trusting it.

## Three layers

| Layer | Lives in | Contains |
|---|---|---|
| **Shared standards** | `cuan/skills/SHARED_STANDARDS.md` | Writing style, evidence/verification rules, uncertainty handling, confidentiality, company/person identification, boundaries between ChatGPT/Council/Cuan. |
| **Common skill structure** | `cuan/skills/_TEMPLATE.md` | The section headings every skill must have: trigger, required inputs, workflow, output format, quality checks, handling of missing information, completion criteria. |
| **Individual skill instructions** | `.claude/skills/<skill-name>/SKILL.md` | Only what's specific to that task — method, reference material, worked example. Must explicitly reference `SHARED_STANDARDS.md` and follow `_TEMPLATE.md`'s structure, not restate them. |

**Why explicit reference rather than assumed inheritance:** a skill file
is a self-contained prompt handed to a model at invocation time.
Nothing carries across automatically just because a shared-standards
document exists elsewhere in the repo. Every individual skill must
name-check `SHARED_STANDARDS.md` and `_TEMPLATE.md` directly inside its
own instructions, and each skill's pressure test must include at least
one case designed to catch a standards violation — if the skill still
produces good output on that case, that is not proof the mechanism
works, it may just mean the model already knew the right answer
independently. See the release process below.

## Release process (mandatory, no exceptions)

1. **Define** — state the problem the skill solves and what a
   successful result looks like, in writing, before building anything.
2. **Build** — implement inside the common structure, explicitly
   referencing shared standards.
3. **Pressure test** — minimum four cases:
   - a normal case
   - a case with incomplete information
   - a case with conflicting evidence
   - a case that should trigger a clarifying question rather than a
     guessed answer
4. **Assess** — check factual fidelity, completeness, usefulness,
   consistency with shared standards, and respect for the
   ChatGPT/Council/Cuan boundary.
5. **Refine and release** — fix failures, record the version number,
   and retain all test cases and their results for future changes.

**Hard block on release, regardless of how polished the output looks:**
- any invented fact
- any unsupported claim of a completed action
- any unauthorised transfer of information across the
  ChatGPT/Council/Cuan boundary

A skill that fails any of these on any pressure-test case does not
ship, even if the other three cases were flawless.

## Build sequence

1. **Briefing and Correspondence** — proves the shared-standards
   reference mechanism, since it is the simplest skill and the easiest
   to check for tone/fact fidelity.
2. **Verified Research and Challenge** — reuses the same evidence rules
   from Shared Standards, adds the deeper verification method
   (VERIFIED/REPORTED/UNVERIFIED tagging, counterargument, what would
   change the conclusion).
3. **Chat-to-Cuan Handover** — the boundary-sensitive one; pressure
   tests must specifically probe that it never assumes an intention was
   completed, and never auto-pushes Council material into Cuan's
   operational files.
4. **Revenue and Relationship Review** — first skill built after the
   architecture itself is proven, not before.

Skills 5-9 from the original ten-item list (Board/Audit Prep, Meeting
Prep, Meridian Assessment, Proposal/Scope, Transaction Review, Council
Reflection) are deferred until this sequence is proven end to end.

## Existing general-purpose skills (Documents, Spreadsheets,
## Presentations, research)

These remain separate and are used *alongside* John's personal skills
whenever the output is a finished file — the personal skills define
reasoning/content standards, the general skills produce the artefact.
No overlap to resolve; they operate at different layers (content
correctness vs. file production).

## Version log

- **v0.1 (18 Sept 2026):** architecture defined, not yet build-tested
  against a real skill.
- **v0.1 confirmed working (18 Sept 2026):** `briefing-correspondence`
  built against this architecture, passed all four pressure-test cases
  (see `cuan/skills/tests/briefing-correspondence-tests.md`), released
  as v1.0. The explicit shared-standards reference mechanism held up
  under testing, including the case designed to catch a silent
  name/entity guess. Architecture proceeds to skill #2 (Verified
  Research and Challenge) next.
- **Deliberate parallel build, John's decision (18 Sept 2026):** John's
  ChatGPT/Council session independently produced its own document,
  "John-ORourke-Skills-Architecture-v0.1.md" (eight shared standards,
  twelve pressure-test cases, not yet behaviourally tested against a
  built skill as of this date). Rather than reconcile the two systems,
  John has chosen to **run both separately, on purpose, as a genuine
  comparison** of which holds up better in real use. This is not a
  conflict to resolve or merge - the two are intentionally independent
  from this point. Cuan's version (this file and its sibling documents)
  continues on its own build sequence regardless of what ChatGPT does
  with its version. Future sessions should not attempt to merge them
  without John explicitly asking for that.
- **Skill #2 built and released (18 Sept 2026):** `verified-research`
  built against this architecture, three full passes and one partial
  pass on pressure testing (see
  `cuan/skills/tests/verified-research-tests.md`) - the partial was
  explained by the skill not yet existing when the test material was
  originally logged, not a method flaw, and is flagged for re-testing
  once the skill is in active use. Released as v1.0. Next:
  Chat-to-Cuan Handover.
- **Skill #3 built and released (18 Sept 2026):** `chat-to-cuan-handover`
  built against this architecture, all four pressure-test cases passed
  (see `cuan/skills/tests/chat-to-cuan-handover-tests.md`), including
  the two designed specifically to probe the ChatGPT/Council/Cuan
  boundary this skill exists to protect (the Golden Generation naming
  conflict, and the two-architectures-in-parallel decision earlier in
  this same session). Released as v1.0. Next: Revenue and Relationship
  Review.
