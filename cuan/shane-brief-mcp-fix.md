# Brief for Shane -- Cuan Infrastructure Fix
**From:** John
**Priority:** High -- blocks Cuan reading training PDFs and Drive documents
**Date:** 25 July 2026

---

## What Cuan currently can and cannot do

**Working:**
- Reads John's Gmail (jwebborourke@gmail.com) -- searches threads, reads emails

**Broken:**
- Cannot read Google Drive files (PDFs, slides, Word docs) -- blocked at authentication level
- Cannot read John's Velocity AI inbox (john@velocityai.ie)
- Cannot read John's Ambrion AI inbox (jwor@ambrion.ai)

---

## Session note, 2 September 2026 (AHL Plc session)

A separate Cuan session had Gmail **read-only** and Drive **closed
entirely** — every deliverable that session produced (the August
Chairman's invoice, the drafted reply to Ray Smyth, the 22 April board
minutes) had to be handed back to John to attach and send by hand,
rather than sent directly. John's own framing: "Opening those two
connectors turns each of those from a conversation into an instruction.
It is a settings job, not a technical one." Worth doing when not against
a deadline — same underlying fix as below, just confirming the gap is
still live as of 2 Sept and costing real back-and-forth on ordinary
tasks, not just blocking Drive document reads.

## Where the fix happens

This has nothing to do with Gmail the app or Google Drive the app. It happens inside the **Claude Code configuration** -- the system settings that control what Cuan can connect to.

Think of it like this: each connection (Gmail, Drive, etc.) needs a one-time permission granted at setup. For Google Drive, that permission was either never completed or has expired. For the Velocity and Ambrion inboxes, those connections were never set up.

**You do not need to change anything in Gmail or in Google Drive. Everything is done in the Claude Code MCP settings.**

---

## Fix 1 -- Google Drive (Priority: Do this first)

**Problem:** The Drive MCP OAuth token is broken or expired.

**What you do:**
1. Open the Claude Code project settings for the Cuan project
2. Find the Google Drive MCP server entry
3. Re-run the OAuth authorization -- this opens a browser window
4. John logs in with his Google account and clicks Allow
5. Done -- Cuan can now read PDFs, slides, and Word docs from Google Drive

**Why this matters:** Without this, Cuan cannot read any PDF attachments or training slides. Every document has to be manually screenshotted or retyped. Once fixed, Cuan reads everything directly.

---

## Fix 2 -- Connect Additional Email Accounts

**Problem:** Cuan can only see one of John's three Gmail inboxes.

**John's email accounts to connect:**
- jwebborourke@gmail.com -- personal Gmail (ALREADY CONNECTED)
- john@velocityai.ie -- Velocity AI (NOT connected)
- jwor@ambrion.ai -- Ambrion AI (NOT connected)
- [Any other Google/Gmail accounts John confirms]

**What you do for each additional account:**
1. In Claude Code project settings, add a new Gmail MCP server instance
2. Set it to authenticate to that specific Google account
3. Run the OAuth authorization -- browser window opens
4. John logs in with THAT account and clicks Allow
5. Repeat for each account

**Note on iCloud (jwebborourke@icloud.com):** This is Apple, not Google. Easiest fix is to set iCloud to auto-forward all mail to jwebborourke@gmail.com -- takes 5 minutes in iCloud settings. No MCP setup needed.

---

## What Cuan looks like when all three fixes are done

- Searches all three Gmail inboxes simultaneously in every session
- Reads any PDF, PowerPoint, or Word doc from Google Drive
- No forwarding emails manually
- No screenshotting slides
- Full picture available every session

---

## Time required

Drive fix: 10 minutes
Each additional email account: 10 minutes each
Total for everything: approximately 40 minutes

---

*Prepared by Cuan -- John's personal intelligence system*
