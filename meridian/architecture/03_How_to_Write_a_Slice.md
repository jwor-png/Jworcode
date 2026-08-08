# How to Write a Slice
### The template for making your engine stronger yourself

A "slice" is a skill. Adding one is how you make Meridian stronger. It is genuinely a one-line job, and once you have done it once you have it for life. Here is the whole craft.

---

## The seven steps

1. **Say it in one plain sentence.** *"At the end of any job, I want Meridian to tell me what other work that client now needs."* That sentence is the starting point. No special words, no code.
2. **Place it.** Decide which of your seven managers already thinks that way. A skill about a contract goes to Legal. A skill about a valuation goes to Finance. A skill about finding more work in a business goes to Business Transformation. You are putting the new skill next to the manager it belongs with.
3. **Look at how the skills there are already written.** Open that manager's file and read the list under `## Sub-agents (the slices)`. Every skill is written the same way. You are going to match it exactly, so the new one is **the same as its brothers**.
4. **Write one line, in that shape, and save.** That is the actual add.
5. **It is live immediately.** No rebuild, no installing, no waiting. The next time you wake Meridian, the skill is there.
6. **Prove it.** Point a quick question at it and watch it use the new skill.
7. **Lock it.** If you keep your engine in git, commit the change so it is recorded and reversible.

The only real skill is steps 1 and 2. Everything else is mechanical.

---

## The shape every slice takes

Open the manager file (for example `meridian/managers/06-business-transformation.md`), find this section:

```
## Sub-agents (the slices)
- **Process audit** — maps how the business actually runs and where it leaks time, cost or value.
- **Revenue gap analysis** — finds the revenue being left on the table: pricing, underused assets, missed lines.
- ... (the rest of the skills)
```

Add your new line to the bottom of that list. The shape is always the same:

```
- **Skill name** — one plain line saying what it does, and where it hands off if it touches another manager.
```

That is it. Bold short name, a dash, one line. Same clothes as its brothers.

### A fill-in-the-blanks template

```
- **[Name it in two or three words]** — [what it does in one line], [and if it touches money, law, property or a binding term, say: routing the binding part to Finance / Legal / Property before it is relied on].
```

The second half only matters when the skill crosses into another manager's ground. Meridian's floor and boundary apply to your new skill automatically. You do not write any of that. It inherits the grounding, the independent critic, the status label and the human gate for free, just by living inside a manager.

---

## A worked example (this one is real)

The sentence: *"At the end of any job, tell me what other work that client now needs."*

Placed under **Business Transformation & Growth**, because that is the manager that finds more value in a business. Written to match its brothers:

```
- **What-else scan** — at the close of any matter, surfaces the adjacent work, services and follow-on opportunities the client now needs next, so every piece of work opens the next one, and routes any real deal, structure or funding need to Commercial, Legal or Finance.
```

Saved. Live. That skill is already in the master engine, added live on 29 July. It is the first of the six in the next document, and it shows you exactly what a finished slice looks like.

---

## One step up from a slice, for later

A slice lives under one manager. Some skills you will want are **cross-cutting**: you want them available everywhere, not just under one manager (for example, "argue the other side of any recommendation"). Those are not added to a manager file; they go into the orchestrator file itself, where the rules that apply to the whole system live. Same idea, one level up. Start with slices. When you want a skill that should apply to everything, that is the next thing to learn, and it is a five-minute conversation with Meridian when you get there.
