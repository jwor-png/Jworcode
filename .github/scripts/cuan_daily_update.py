"""
Cuan daily update script.
Reads intelligence-log.md, counts entries from the last 24 hours,
updates daily-update-log.md with a confirmation row.
Runs inside GitHub Actions — no session dependency.
"""

import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

LOG = Path("cuan/logs/intelligence-log.md")
DAILY = Path("cuan/logs/daily-update-log.md")
DOSSIER = Path("cuan/ventures_dossier.md")

TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
YESTERDAY = (datetime.now(timezone.utc) - timedelta(hours=24)).strftime("%Y-%m-%d")


def count_entries(text, source_keyword, since_date):
    """Count log entries for a given source keyword added since since_date."""
    # Entries are headed: ### [YYYY-MM-DD] [SOURCE] [STATUS]
    pattern = re.compile(
        r"^### \[(\d{4}-\d{2}-\d{2})\].*" + re.escape(source_keyword),
        re.MULTILINE | re.IGNORECASE,
    )
    matches = pattern.findall(text)
    return sum(1 for date in matches if date >= since_date)


def extract_ventures(text, since_date):
    """Pull venture names mentioned in entries since since_date."""
    ventures = set()
    # Find entries since yesterday
    entry_pattern = re.compile(
        r"### \[(\d{4}-\d{2}-\d{2})\].*?(?=### \[|\Z)", re.DOTALL
    )
    for match in entry_pattern.finditer(text):
        entry_date = match.group(1)
        if entry_date >= since_date:
            block = match.group(0)
            venture_line = re.search(r"\*\*Ventures touched:\*\*\s*(.+)", block)
            if venture_line:
                for v in venture_line.group(1).split(","):
                    ventures.add(v.strip())
    return sorted(ventures) if ventures else ["None"]


def main():
    log_text = LOG.read_text() if LOG.exists() else ""

    meridian_count = count_entries(log_text, "Meridian", YESTERDAY)
    sales_count = count_entries(log_text, "Sales Orchestration", YESTERDAY)
    ventures = extract_ventures(log_text, YESTERDAY)
    ventures_str = ", ".join(ventures)

    status = "CONFIRMED" if (meridian_count + sales_count) > 0 else "NO NEW ENTRIES"

    new_row = (
        f"| {TODAY} | {meridian_count} | {sales_count} "
        f"| {ventures_str} | GitHub current | {status} |"
    )

    # Append row to daily-update-log.md
    daily_text = DAILY.read_text() if DAILY.exists() else ""
    # Insert after the table header line
    if "Awaiting first run" in daily_text:
        daily_text = daily_text.replace(
            "| — | — | — | — | — | Awaiting first run |", new_row
        )
    else:
        # Find end of table header and insert
        header_marker = "| Status |"
        insert_after = daily_text.find(header_marker)
        if insert_after != -1:
            end_of_line = daily_text.find("\n", insert_after) + 1
            daily_text = daily_text[:end_of_line] + new_row + "\n" + daily_text[end_of_line:]
        else:
            daily_text += "\n" + new_row

    DAILY.write_text(daily_text)

    print(
        f"Cuan updated {TODAY} -- "
        f"Meridian: {meridian_count} entries, "
        f"Sales: {sales_count} entries, "
        f"Ventures touched: {ventures_str}. "
        f"Status: {status}."
    )


if __name__ == "__main__":
    main()
