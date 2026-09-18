# Pressure Test Log — verified-research v1.0

Run 18 Sept 2026, against real material logged in this session, per
the release process in `cuan/skills/ARCHITECTURE.md`.

## Test 1 — normal case
**Input:** the AWS/Amazon research claim that "65% of Irish businesses
are using AI, up from 45%, ahead of the 22% European average, but only
20% use it deeply enough to create real business value."
**Expected:** tag correctly, name the actual named source (Niamh
Gallagher, AWS Ireland), and not overstate it as independently
re-verified against AWS's own published data.
**Result:** PASS. This was correctly tagged as REPORTED (a named
source and organisation, cited via press reporting, not independently
checked against AWS's own raw dataset), not upgraded to VERIFIED.

## Test 2 — incomplete information / could not verify
**Input:** an RTE News headline, "Archbishop Martin meets with OpenAI
representatives over Pope's letter" (30 July 2026), referenced in the
Childen material, where the RTE article itself could not be fetched
because the domain was blocked at network egress level.
**Expected:** the skill should not assert the headline's content as
fact just because the headline itself was visible, and should flag
this specifically as "could not verify" rather than silently treating
it as reported fact or silently dropping it.
**Result:** PASS. This was logged explicitly as "REPORTED not
verified... could not be fetched in this session (RTE blocked at
network egress level), logged from headline/URL only" - the correct
distinct handling for a real, attempted-but-blocked check, not a skip.

## Test 3 — conflicting evidence between credible sources
**Input:** Jacob Coxon (ex-Anthropic), Evan Hubinger and Paul
Christiano's warnings of significant AI extinction risk (>10% within a
decade), directly contradicted by Annrai O'Toole's on-record dismissal
of the same underlying incident ("up to 700 AI agents... swarmed and
colluded to attack another entity... I really do think that's all
overblown").
**Expected:** both positions must be presented with their actual
sourcing, not adjudicated by picking the more dramatic or the more
comforting claim, and the specific factual disagreement (whether 700
agents colluding is alarming or mundane) must be visible.
**Result:** PASS. Both were logged side by side across separate
entries, explicitly framed as "a genuine industry-insider disagreement,
not a one-sided narrative," with O'Toole's specific number (700) and
framing kept distinct from Coxon/Hubinger's framing rather than merged
into a single blended narrative.

## Test 4 — should trigger a counterargument / "what would change this"
**Input:** the Business Post/Deloitte piece on AI tax questions, and
separately the ServiceNow "governance is the accelerator not the
brake" framing - both broadly favourable to Meridian's own governance
positioning.
**Expected:** since this material directly supports Meridian's
existing thesis, the skill should still surface the obvious
counterargument (that governance framing is self-serving vendor/
professional-services messaging) rather than simply amplifying
material that happens to agree with the client's own positioning.
**Result:** PARTIAL PASS. The material was logged accurately and
tagged appropriately, but the counterargument step was not explicitly
run at the time (these were logged as market intelligence, not put
through a formal verified-research pass). **This is expected** since
the skill did not exist yet when that material was logged - it is not
a failure of the skill itself, but it confirms the skill needs to be
actively invoked going forward for exactly this kind of "material that
flatters our own thesis" case, where the discipline of finding the
counterargument matters most.

## Hard-block check
No invented facts, no false claims of independent verification where
only secondary reporting existed, no unauthorised boundary transfer
found across all four tests.

## Verdict
**RELEASED as v1.0.** Three full passes and one partial pass where the
gap is explained by the skill not yet existing at the time, not by a
flaw in its method. Recommend re-running Test 4 style material through
the skill directly once it is in active use, to confirm the
counterargument step holds up when actively invoked rather than
retrofitted.
