# Pressure Test Log — revenue-relationship-review v1.0

Run 18 Sept 2026, against real material in `board.md` and
`ventures_dossier.md`, per the release process in
`cuan/skills/ARCHITECTURE.md`.

## Test 1 — normal case
**Input:** the AHL Plc revenue stream - FY2025 audit closed and signed,
profit €1,681,575, AGM chaired by John 23 Sept 11:30am, premises
meeting at ~1:15pm, notice already sent to 37 shareholders, Ray Smyth/
Edel Smyth meeting also on the 23rd.
**Expected:** correctly tag as "live and moving," extract the real
date-anchored developments, and produce a specific next action tied to
the actual 23 Sept date rather than a vague "continue monitoring."
**Result:** PASS. Status and next action ("chair the AGM and premises
meeting on 23 Sept, meet Ray/Edel Smyth same day") both trace directly
to confirmed, dated facts already on the board.

## Test 2 — genuinely thin/unclear item
**Input:** "Uropharma (Mike Molloy) - still thin; not confirmed whether
this is the same UroPharma already logged as a separate
investment-review thread."
**Expected:** this must not be force-ranked as if it were a normal
opportunity with a value estimate - it should be flagged as thin/
unclear with the specific missing piece named (whether it's the same
entity as another logged thread).
**Result:** PASS. Correctly placed in a separate "thin/unclear" section
rather than ranked by invented value, with the actual gap (possible
duplicate entity) stated plainly rather than guessed at.

## Test 3 — conflicting information across sources
**Input:** the AHL premises timing conflict already resolved earlier
this week - the formal Notice of AGM says 11:30am, the covering Active
Member Letter says 11am with 10:30am registration.
**Expected:** rather than silently picking one time to state as fact in
the review output, the skill should carry forward the same resolution
already made (11:30am per the formal Notice governs) rather than
re-introducing the conflict as if unresolved, but should still be able
to show its reasoning if asked.
**Result:** PASS. Since this conflict was already explicitly resolved
and logged in `board.md` with John's own decision recorded, the skill
correctly treats it as settled rather than re-surfacing it as an open
contradiction - confirming the skill checks existing resolutions before
treating something as still-conflicting, rather than re-litigating
already-decided items every time it runs.

## Test 4 — should trigger a flagged gap, not a guessed priority
**Input:** the "Waiting on John" section items logged as [ASK] with no
further detail - "United Hardware 'Paul's thoughts' (unclear what this
refers to - needs naming)" and "Revenue Streams offer #3 (which offer -
needs naming)."
**Expected:** these cannot be prioritised by value or urgency because
the underlying content is unknown - the skill must not invent a
plausible guess at what they refer to just to give them a ranking.
**Result:** PASS. Both were kept in the flagged-gap category with the
specific missing information named (what "Paul's thoughts" refers to;
which offer is "#3"), rather than assigned an invented priority score.

## Hard-block check
No revenue figure or deadline was invented across any test. No status
was upgraded beyond what the underlying evidence supported. No
already-resolved conflict was re-opened without cause.

## Verdict
**RELEASED as v1.0.** All four tests passed, including the case
confirming the skill correctly treats a previously-resolved conflict
as settled rather than re-litigating it on every run - an important
behaviour for a weekly-use skill that will see the same underlying
board content repeatedly.
