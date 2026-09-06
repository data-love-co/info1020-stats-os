---
name: student-bootstrap
description: >
  Sets up an INFO 1020 student in the Stats OS: detects the OS, creates the CLAUDE.md link, checks
  that Python is available, asks which module they are on and which AI tool they are using, writes
  0_User/, and points them at the module brief. Triggers on "get me started", "set me up", "I'm
  new here", "first time", or any sign of first-time setup. Nothing to install and no model key.
---

# student-bootstrap: get me started

You are setting up a business undergraduate who may never have opened a terminal. Do one step,
confirm it worked, move on. Explain each step in one plain sentence first. Never make anyone feel
behind for asking what a repo is.

## Step 0: link CLAUDE.md and detect the OS

Detect the OS (`uname -s` gives Darwin or Linux; `$env:OS` gives Windows_NT), say what you found,
then make sure `CLAUDE.md` exists at the repo root. If not:

```
node 0_System/bootstrap/setup.mjs
```

If Node is missing, follow `reference/os-setup.md` (the file is a copy of `AGENTS.md`; it can be
created by hand). Confirm the folder is **not** inside OneDrive, Google Drive, Documents, or
Desktop on a synced machine; if it is, explain in two sentences why that corrupts git and offer to
help move it to `C:\Users\<name>\info1020` or `~/info1020`.

## Step 1: confirm the tool

Ask which they are using: Claude Code, GitHub Copilot agent mode in VS Code, or something else.
All of them work here. If they are on a chat-only tool (Copilot on the web, ChatGPT, Gemini,
Claude on the web), say that every AI Block also exists as a paste-ready prompt in
`4_Library/portable-prompts/Portable-Prompts.md` and that nothing in the course requires more.

If they do not have any tool yet, point to `4_Library/tools/Get-GitHub-Copilot-Free.md`. Copilot
Free takes five minutes; the student plan takes a few days to verify.

## Step 2: check Python (optional)

`python --version` or `python3 --version`. Python 3 is used by the skills to compute for real and
by `0_System/scripts/check-values.py`. If it is missing, say so, give the install link for their
OS, and continue; nothing in the setup is blocked by it.

## Step 3: which module

Ask which module they are on (1 to 7, or the project). Open `1_Modules/<module>/README.md` and
read them the "You build" line and the verification target. Then check that the data file named
there exists in `4_Library/sample-data/`.

## Step 4: write 0_User/

Create `0_User/student.md` with three lines: first name (or "prefer not to say"), the module, and
the tool. Nothing else. No student ID, no email. Say what you wrote.

## Step 5: the four rules, once

Say them in one line and do not lecture: verify, cite, add value, never on quizzes or exams. Then:
"Say **run AI Block N** when you are ready."

## What you never do here

Type formulas into their Excel workbook, open a quiz, or write a manager sentence.
