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

## Google Drive

After logging, push the output files to the Cuan folder on Google Drive.
Mark "Pushed to Google Drive: Yes" in the log entry with the file name.

## Cuan daily update reads

Each morning at 07:45 Cuan reads intelligence-log.md, counts new entries,
updates ventures_dossier.md where relevant, and writes one confirmation row to daily-update-log.md.

The confirmation appears at the top of the morning brief.
