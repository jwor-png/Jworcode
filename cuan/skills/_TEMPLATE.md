# Common Skill Structure — template

Every individual skill instruction file must contain these sections,
in this order. Do not restate Shared Standards content here — link to
`cuan/skills/SHARED_STANDARDS.md` and rely on it being read.

## 1. Purpose and trigger
One or two sentences: what problem this solves, and what kind of
request should invoke it.

## 2. Required inputs
What the skill needs to run properly. If a required input is missing,
the skill must ask for it rather than guess.

## 3. Workflow
The actual step-by-step method, specific to this task.

## 4. Output format
What a finished result looks like structurally (not the content, the
shape).

## 5. Quality checks
The specific checks this skill runs on its own output before
returning it, on top of the standing Shared Standards checks that
apply to everything.

## 6. Handling of missing information
What this skill does, specifically, when it does not have what it
needs — not a repeat of the general Shared Standards rule, but how
that rule applies to this particular task.

## 7. Completion criteria
How to know the skill has actually finished the job, not just
produced output.

## Reference (every skill file must include this line near the top)
"This skill follows `cuan/skills/SHARED_STANDARDS.md` and the common
structure in `cuan/skills/_TEMPLATE.md`."
