---
name: briefing-correspondence
description: Turn John's dictation, notes or screenshots into clear emails, WhatsApps, letters and briefings. Use when John asks to draft, reply to, or send a message, letter, or briefing note, or shares raw notes/screenshots and wants them turned into finished correspondence.
---

This skill follows `cuan/skills/SHARED_STANDARDS.md` and the common
structure in `cuan/skills/_TEMPLATE.md`. Read `SHARED_STANDARDS.md`
before producing any output under this skill.

## 1. Purpose and trigger
Turns John's raw input (dictated voice-to-text, handwritten notes,
screenshots, a half-formed instruction) into finished correspondence
that preserves his actual meaning, in grounded boardroom English,
without inventing facts, commitments, or detail he didn't provide.
Trigger on any request to draft or send an email, WhatsApp, letter, or
briefing note.

## 2. Required inputs
- The raw material (dictation, notes, screenshot content).
- The recipient and channel (email, WhatsApp, formal letter).
- Enough context to know the relationship/register (board member,
  family, supplier, regulator, etc.) — if this is not clear from
  context already established in this session or in Cuan's files, ask.
- Any prior correspondence in the same thread, if replying.

## 3. Workflow
1. Read the raw material fully before drafting anything. Do not start
   composing from a partial read.
2. Identify what John actually wants said, distinct from how he said
   it out loud (voice-to-text often garbles names/numbers — check
   these against Cuan's existing files rather than transcribing a
   likely mis-hearing as fact).
3. Draft in the register appropriate to the recipient (see Shared
   Standards: a shareholder letter, a WhatsApp to family, and a board
   briefing are not the same voice).
4. Include only commitments, dates, and facts John actually stated or
   that are independently confirmed elsewhere in Cuan's files. Never
   add a plausible-sounding detail to make the draft read more
   complete.
5. If replying to an existing thread, thread the reply correctly and
   preserve the original context rather than restating it from
   scratch.
6. Present the draft for John's review before sending, unless he has
   explicitly said to send it directly.

## 4. Output format
The finished draft itself, in the correct format for its channel
(plain text for WhatsApp/email body, formal letterhead style if it's a
letter), followed by a one-line note of anything flagged as uncertain
or assumed, if applicable.

## 5. Quality checks
- No em dashes.
- No invented names, dates, figures, or commitments.
- Every fact in the draft traces back to something John said in this
  conversation or something already confirmed in Cuan's files, not to
  a plausible inference.
- Tone matches the actual relationship, not a generic "professional"
  default.
- Read the draft back once as the recipient would read it, checking it
  doesn't imply anything John didn't actually say.

## 6. Handling of missing information
If the raw material doesn't make clear who the recipient is, what
outcome John wants, or contains a name/detail that can't be confirmed,
stop and ask rather than guessing. A wrong guess sent to a real
recipient is a much worse outcome than a short clarifying question.

## 7. Completion criteria
The draft is ready when it says exactly what John meant, contains
nothing he didn't say or that isn't independently confirmed, and is in
the correct register and format for the recipient and channel. It is
not complete just because it reads smoothly.
