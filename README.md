# INFO 1020 Stats OS

The AI workspace for **INFO 1020: Analytics II** at the Daniels College of Business, University of
Denver. You use it during the AI Block that closes every module, and you keep it after the course
ends.

> ### [Read the student guide first](https://data-love-co.github.io/info1020-stats-os/)
> Before class, the four rules, the seven AI Blocks, which tool you need, the prompts you can
> paste, and plain-language definitions. Works on your phone. Nothing to install.

It is an **agentic operating system**: a folder of markdown files, conventions, and skills that an
AI agent reads and works in. You bring the module's data and the numbers you already computed in
Excel. The agent builds something small and working: a base-rate explainer, a demand simulator, a
confidence-interval calculator, a hypothesis-test readout. You verify the build against your own
workbook, cite the tool, and write the manager sentence yourself.

Four rules, every time: **verify, cite, add value, never on quizzes or exams.**

## Quickstart

You do not need to install anything to do the AI Blocks. Pick the path that matches the tool you
have.

### Path A: a chat tool (Copilot on the web, Claude, ChatGPT, Gemini)

1. Open **[Portable-Prompts.md](4_Library/portable-prompts/Portable-Prompts.md)**.
2. Copy the prompt for your module. Upload or paste the module's data file from
   **[sample-data](4_Library/sample-data/)** when the prompt asks for it.
3. Compare the output with your workbook using the targets in
   **[sample-data/README.md](4_Library/sample-data/README.md)**, then paste prompt, output,
   verification, and citation into the So-What tab.

GitHub Copilot is free for verified students:
**[Get-GitHub-Copilot-Free.md](4_Library/tools/Get-GitHub-Copilot-Free.md)**.

### Path B: an agent that can read this folder (Claude Code, Copilot agent mode in VS Code)

1. Ask your agent to fetch the workspace. Copy this in:

   > Clone https://github.com/data-love-co/info1020-stats-os into a folder called `info1020`
   > directly inside my user folder, then open it and follow the setup.

   Put it straight in your user folder (`C:\Users\<you>\info1020` on Windows, `~/info1020` on
   Mac), **not** in Documents, Desktop, OneDrive, or Google Drive. Synced folders corrupt the
   hidden `.git` folder.

2. Say **"get me started."** The bootstrap detects your OS, creates the `CLAUDE.md` link, and asks
   which module you are on.
3. Say **"run AI Block 3"** (or whichever module). The skill builds the tool, runs the course data
   through it, and hands you the verification and citation block for your workbook.

## What is here

```
1_Modules/          One folder per module: the AI Block brief, the verification targets, the paste template
4_Library/method/   One method sheet per module, plus rounding, the manager sentence, and the AI rules
4_Library/sample-data/   Every course dataset, with the key values each one should produce
4_Library/portable-prompts/   The seven AI Blocks as paste-ready prompts
4_Library/tools/    Which tool does what, and how to get Copilot free
3_Project/          The course project: parts 1 to 3, the video, and the templates you fill by hand
.agents/skills/     The skills an agent runs (one per AI Block, plus bootstrap, project, and utilities)
docs/               The student guide website
```

Full conventions for agents are in **[AGENTS.md](AGENTS.md)**.

## The seven AI Blocks

| Module | You build | You verify against |
|---|---|---|
| 1 Probability | A base-rate explainer for the fraud-flag problem | P(fraud given flag) = .27 |
| 2 Distributions | A Poisson walk-in simulator and a staffing call | P(more than 15) = .19 |
| 3 Sampling and CIs | A confidence-interval calculator that writes its own sentence | $3,234.45 to $3,563.35 |
| 4 One-sample test | A seven-step hypothesis-test readout | t = 1.90, p = .038 |
| 5 Two-sample test | An A/B test readout with step zero | t = 2.53, p = .016 |
| 6 ANOVA | A group-comparison readout with Tukey only when warranted | F = 76.51; F = .71 |
| 7 Chi-square | A segment-association audit with expected-count checks | chi-square = 9.42 |

## After the course

This repo is public and openly licensed on purpose. Fork it, keep it, add your own skills, and use
it in INFO 2020 and beyond. The method sheets in `4_Library/method/` are the formula reference for
the whole course.

## Credits

Course materials by Jasmine Walker Motupalli, Daniels College of Business, University of Denver.
Course datasets are fictional or anonymized and provided for instruction. Built on the same
conventions as the [INFO 4610 Analytics OS](https://github.com/data-love-co/info4610-analytics-os).
