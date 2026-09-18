---
name: verified-research
description: Check material claims against current sources before John relies on or circulates them. Separates verified facts, reported claims, assumptions and unknowns; identifies the strongest counterargument and what evidence would change the conclusion. Use before any analysis, article summary, or claim is treated as settled fact or shared onward.
---

This skill follows `cuan/skills/SHARED_STANDARDS.md` and the common
structure in `cuan/skills/_TEMPLATE.md`. Read `SHARED_STANDARDS.md`
before producing any output under this skill.

## 1. Purpose and trigger
Applies a deeper verification method on top of the standing evidence
rules in Shared Standards, for material that John intends to rely on,
act on, or circulate to somebody else. Trigger whenever a claim's
accuracy actually matters to a decision, not for routine knowledge-base
filing of low-stakes material.

## 2. Required inputs
- The claim(s) or material to be checked.
- What John intends to do with it (act on it personally, brief someone
  else, cite it externally) — this changes how rigorous the check
  needs to be.
- Access to primary sources where possible; where a source cannot be
  reached (paywall, blocked domain, no web access), that limitation
  must be stated, not silently skipped.

## 3. Workflow
1. Separate the material into individual factual claims rather than
   assessing it as one undifferentiated block.
2. For each claim, classify it:
   - **VERIFIED** — confirmed directly against a primary or highly
     credible source, checked in this pass, not assumed from memory.
   - **REPORTED** — attributed to a named, identifiable source, but not
     independently checked against the primary material.
   - **UNVERIFIED** — single unconfirmed source, anonymous source, or
     an inference/guess being presented as fact.
   - **COULD NOT VERIFY** — a genuine attempt was made (source sought)
     but blocked (paywall, egress block, source no longer available) —
     distinct from UNVERIFIED, since here a check was actually
     attempted and failed, not skipped.
3. Where two credible sources conflict, present both positions and
   their sourcing plainly, side by side. Do not silently pick the one
   that sounds more authoritative or more convenient.
4. Identify the single strongest counterargument to the material's own
   conclusion, even if John (or the source) would prefer it not be
   raised.
5. State explicitly what new evidence would change the conclusion —
   this is often the most useful line in the whole output, since it
   tells John what to watch for.
6. If the material's stakes are high (a decision, a public claim, a
   number going into a document someone else will rely on), recommend
   a specific next verification step rather than stopping at "this is
   unverified."

## 4. Output format
A short structured note: claim-by-claim tags (VERIFIED/REPORTED/
UNVERIFIED/COULD NOT VERIFY), the strongest counterargument, what would
change the conclusion, and a plain-language bottom line John can act
on without needing to parse the tags himself.

## 5. Quality checks
- Every tag is justified by a specific, named source, not a vibe.
- Conflicting sources are shown, not resolved by silent selection.
- The counterargument is the strongest real one, not a straw man
  included to look balanced.
- Nothing is claimed as VERIFIED that was actually checked from
  secondary reporting rather than the primary source itself.

## 6. Handling of missing information
If a primary source cannot be reached, say so plainly (COULD NOT
VERIFY) rather than either skipping the claim silently or downgrading
it to UNVERIFIED as if no attempt was made — the distinction matters
for John's own risk judgement.

## 7. Completion criteria
Done when every material claim has an honest tag, any conflict between
sources is visible rather than resolved by guesswork, and John has
enough to decide for himself whether the material is solid enough to
act on or circulate.
