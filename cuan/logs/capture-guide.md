# Capture Guide — How Meridian and Sales Orchestration Log to Cuan

## Who writes here

Both systems append to `cuan/logs/intelligence-log.md` at the end of every substantive session.
The daily update cron reads this file each morning and confirms Cuan is current.

## Meridian -- what to log

At the end of any Meridian session where work was produced, append one entry to intelligence-log.md covering:
- Which managers were routed to
- What was produced (briefs, drafts, models, research)
- Status of each output (DRAFT / IN REVIEW / DECISION-READY)
- Which ventures were touched (cross-reference ventures_dossier.md)
- Any open loops Cuan needs to carry

## Sales Orchestration -- what to log

At the end of any sales session, append one entry covering:
- Which channel or prospect the work related to
- What was produced (outreach, pipeline update, proposal, brief)
- Status
- Which ventures were touched
- Any open loops

## Cuan itself -- what to log (standing rule, 2 Sept 2026)

Cuan often gathers material directly from John that's relevant to
Meridian's domains (market intelligence, press cuttings, external
research, governance/regulatory developments) without a live Meridian
session being involved. **Whenever Cuan identifies something relevant
to a Meridian domain, it logs an entry here itself — tagged `[Cuan →
Meridian]` — without waiting to be asked.** This is not optional and
does not require John's instruction each time; it is Cuan's own
standing responsibility, the same way Meridian and Sales Orchestration
log automatically. Follow the same entry format, crediting Cuan as the
source and noting which Meridian domain(s) the material feeds.

## Google Drive

After logging, push the output files to the Cuan folder on Google Drive.
Mark "Pushed to Google Drive: Yes" in the log entry with the file name.

## Cuan daily update reads

Each morning at 07:45 Cuan reads intelligence-log.md, counts new entries,
updates ventures_dossier.md where relevant, and writes one confirmation row to daily-update-log.md.

The confirmation appears at the top of the morning brief.
