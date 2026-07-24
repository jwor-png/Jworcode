# Cuan Daily Morning Sync Protocol

*Adopted 24 July 2026, agreed by John and Shane. Runs at the start of every Cuan session, and whenever John says "morning sync" or turns the system on. Purpose: John should never have to tell Cuan what he or the other orchestrations did. Cuan trawls, picks it up, and reports.*

## Run these every session start (after gratitude, before the task list)

### Step 1 — Cross-session / repo sync
- `git fetch --all` then review commits across ALL branches since the last sync (other Claude sessions: Meridian/Jworcode Default, sales orchestration, any others).
- Read any new committed work (briefs, captures, analyses) so Cuan is aware of it here.
- **Known gap:** the other sessions only surface work they COMMIT AND PUSH. If Cuan sees a reference to work "done in Meridian/sales" that is not in the repo, tell John it is not synced and ask that session to commit and push, or to paste it.

### Step 2 — Gmail trawl (in-session; Gmail auth is only reliable when John is live)
- Search `in:sent newer_than:1d` and the inbox for overnight/morning activity.
- Pick up what John has already actioned himself and what has arrived, across the live fronts:
  - **UHL** (audit, board, training, members)
  - **AHL** (fire cert, AGM, premises sale, shareholders, product matters)
  - **MiDentalCare liquidation** (liquidator Butler & Co, Sremium/Sean O'Dwyer, CapitalFlow, employee claims)
  - **Meridian / Ambrion / sales** (prospects, commissions, LinkedIn)
  - **Julianstown / Old Mill** (planning, design team, owners)
  - **Barber Republic / ODIN** (Edward Lawton, Coxe, Shane's items)
  - **Tangible, personal/legacy** (B1 forms, motor tax, family)

### Step 3 — Report to John (creed-ordered)
- One tight morning brief: what is NEW since yesterday, what John already moved, what needs his action today, ordered by the Operating Creed with revenue first.
- Apply the Council filter to Creed 1 items: "does this make money entering the business more likely in the near term?"
- Update `cuan/captures/master_list_<date>.md` with anything new; nothing lives only in John's head.

## Scheduling note
- The reliable trigger is session start (Gmail auth present). A fully headless/cron run can do Step 1 (git) but may NOT have Gmail access, so Step 2 needs John live. Any scheduled morning nudge is therefore a prompt to run the full sync in-session, not a silent background trawl.
