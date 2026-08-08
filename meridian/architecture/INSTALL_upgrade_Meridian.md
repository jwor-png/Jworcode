# Meridian — Install and Self-Upgrade
### Read me first. Written for John, and for Meridian itself.

This pack does two things. It helps John see and understand his engine (the Map, the Wiring, How to Write a Slice), and it lets the engine upgrade itself with a new set of skills. This file is the upgrade.

---

## For John (thirty seconds)

The upgrade adds six new skills to your engine, taking it from fifty to fifty-six. You do not need to touch any code.

Open Meridian in your Claude Code and say, in plain words:

> Read "INSTALL - upgrade Meridian" and apply the upgrade to yourself.

Meridian will add the new skills to its own manager files, confirm each one is live, tell you what changed, and record it. That is the whole job.

If you would rather do it by hand, it is just as simple. For each skill below, open the named manager file, find the list under `## Sub-agents (the slices)`, paste the one line at the bottom, and save. See "03 — How to Write a Slice" for the walk-through.

---

## For Meridian (the operative instructions)

Meridian, when John asks you to apply this upgrade, do exactly this and nothing more.

1. Confirm you can see your own engine files under `meridian/managers/`. If you cannot, tell John plainly and stop.
2. For each skill in the list below:
   a. Open the named manager file.
   b. Find the list under the heading `## Sub-agents (the slices)`.
   c. If a skill of that name is already present, skip it. Never duplicate a skill.
   d. Otherwise add the exact line, as written, at the bottom of that list. Keep the house form: a dash, a bold name, then one plain sentence, the same shape as the skills already there.
   e. Confirm the skill is now live.
3. When all six are done, tell John what you added, that the engine has gone from fifty skills to fifty-six, and which managers changed.
4. If the engine is under git, commit with a clear message. If it is not, skip this step.
5. Change nothing else. Do not touch the governance floor, the orchestrator, or any other file. This upgrade only adds skills, it removes nothing and changes no existing behaviour.

This upgrade runs only on John's own engine, on John's machine. It performs no external action of any kind.

---

## The upgrade — six skills

Three of the six sit in Legal & Governance, which suits a former solicitor. Two of them (Argue-the-other-side and Say-it-to-the-client) are naturally cross-cutting; they are placed in a sensible home here, and John can lift them into the orchestrator later if he wants them on every answer.

### 1. Read-this-for-me
Manager file: `meridian/managers/02-legal-and-governance.md`
```
- **Read-this-for-me** — takes a contract, lease, term sheet or email dropped in, reads it against the retrieved authority, and returns what matters, what bites and what to push back on, flagging anything binding for a qualified solicitor before it is relied on.
```

### 2. Meeting-prep brief
Manager file: `meridian/managers/01-commercial-and-deal.md`
```
- **Meeting-prep brief** — before a meeting, assembles one grounded page: who is being met, their likely position, where the leverage sits, and the two or three things that could go wrong.
```

### 3. Argue-the-other-side
Manager file: `meridian/managers/02-legal-and-governance.md`
```
- **Argue-the-other-side** — on command, red-teams Meridian's own recommendation, sets out the strongest case against it, and names where it would break, so no position is carried that has not been attacked first.
```

### 4. What-else scan
Manager file: `meridian/managers/06-business-transformation.md`
```
- **What-else scan** — at the close of any matter, surfaces the adjacent work, services and follow-on opportunities the client now needs next, so every piece of work opens the next one, and routes any real deal, structure or funding need to Commercial, Legal or Finance.
```

### 5. Say-it-to-the-client
Manager file: `meridian/managers/05-ai-strategy-and-adoption.md`
```
- **Say-it-to-the-client** — takes any grounded, technical output and renders a clean, plain-English page to hand straight to a client, the accuracy intact and the sources kept.
```

### 6. Obligations and deadlines schedule
Manager file: `meridian/managers/02-legal-and-governance.md`
```
- **Obligations and deadlines schedule** — pulls every date, statutory clock, filing and obligation out of a matter into one clear schedule, with the directors' duties and liability flags on it, and the hard dates sent to a qualified solicitor to confirm.
```

---

When the six are in, your engine stands at fifty-six skills, and John did it himself.

AI driven, human led.
