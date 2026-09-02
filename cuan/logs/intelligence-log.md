# Intelligence Log — Cuan

Append-only record of all work pushed from Meridian Intelligence and Sales Orchestration.
One entry per session. Format is fixed — both systems write to this file.

---

## Log Format

```
### [YYYY-MM-DD] [SOURCE] [STATUS]
**Source:** Meridian | Sales Orchestration
**Domain(s):** e.g. Commercial & Deal / AI Strategy / Finance
**Summary:** One paragraph — what was worked on, what was produced
**Outputs:** List of files, drafts, briefs, or decisions produced
**Open loops:** Anything unresolved that Cuan needs to carry forward
**Ventures touched:** Which ventures from the dossier were affected
**Pushed to Google Drive:** Yes / No / [file name]
---
```

---

<!-- ENTRIES BEGIN BELOW — newest first -->

### [2026-09-02] [Meridian] [DRAFT]
**Source:** Meridian
**Domain(s):** Commercial & Deal (Mike Molloy relationship — Childen/Uropharma); Architecture/connectivity check
**Summary:** Meridian activated via /meridian in a session where the `~/meridian/` engine folder was absent, so it ran on its embedded brief only — no substantive brief submitted, connectivity/architecture check only. Separately, this Cuan capture system (this log, the daily update table, the capture guide, the GitHub Actions workflow, and the Stop/SessionStart hooks) was designed and built so Meridian and Sales Orchestration log here automatically, without John having to instruct it each time. John also shared a WhatsApp exchange with Mike Molloy referencing "Childen" and Uropharma, in the wrong thread — this session has no prior history on Mike Molloy, and a search of `people_map.md`, `ventures_dossier.md`, and this log found nothing recorded anywhere on Mike Molloy, Childen, or Uropharma.
**Outputs:** `cuan/logs/intelligence-log.md`, `cuan/logs/daily-update-log.md`, `cuan/logs/capture-guide.md`, `.github/workflows/cuan-daily-update.yml`, `.github/scripts/cuan_daily_update.py`, `.claude/settings.json` (SessionStart + Stop hooks), `meridian/meridian-orchestrator.md` and `.claude/commands/youllneverwalkalone.md` updated with mandatory capture instructions. Google Drive "Cuan Intelligence Hub" folder created (ID 1qnFM7LWOhZo1HfiPKAgDgls9TrpAvYXG) with Intelligence Log and Daily Update Log documents seeded — full auto-sync from GitHub Actions still needs a Google service account key stored as the `GOOGLE_CREDENTIALS` secret.
**Open loops:** (1) Google Drive automated sync needs the `GOOGLE_CREDENTIALS` GitHub secret — outstanding. (2) **Mike Molloy's full relationship history, plus the Childen and Uropharma detail, needs to be logged here from whichever Meridian thread actually holds that work** — not present anywhere in Cuan yet. Per the shared WhatsApp image: Mike's goal is getting Childen and Uropharma onto a world stage — political, diplomatic, business and funding support — building on his existing work, driven by a passion for peace and geopolitical strategy connected to his Aunt Mary, combining Vatican network contacts with EU, British and American contacts. He reacted positively to John's analysis and is open to defining what he wants from the arrangement. (3) Sales Orchestration's actual location wasn't confirmed in that session — see the connection-check entry in `ventures_dossier.md` (2 Sept) which found `meridian/sales-orchestration/` already exists here with substantial content, likely resolving this rather than it being genuinely missing.
**Ventures touched:** None yet formally in `ventures_dossier.md` — Childen and Uropharma are new names, not previously tracked. UroPharma appears once before, in `chatgpt_synopsis_jul_aug_2026.md`, as a separate investment-review thread (~£3.5m raised, ~£500k sought) — worth checking whether that's the same UroPharma Mike Molloy is connected to, or a different one, rather than assuming.
**Pushed to Google Drive:** No (sync not yet wired up — see open loop 1)
---
