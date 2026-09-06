# INFO 1020 Stats OS

The AI workspace for **INFO 1020: Analytics II (Business Statistics and Analysis)** at the
Daniels College of Business, University of Denver. It is an *agentic operating system*: a folder
of markdown files, conventions, and skills that an AI agent reads and works inside. Students point
it at a module's data, run that module's AI Block, verify the result against their own workbook,
cite the tool, and write the manager sentence themselves.

The course rule that governs everything here, in four words: **verify, cite, add value, never on
quizzes or exams.** The student scopes the problem by hand. The AI builds. The student checks the
build against the math they did in Excel and writes the interpretation in their own words.

## Who you are working with

A first- or second-year business undergraduate in a required statistics course. Assume no
programming background and no terminal experience. They work in Excel, and every number they
bring you was (or will be) computed in an Excel workbook with named tabs. They are graded on
rounding. They are not allowed to use you on quizzes or exams, and they know it; if they ask you
for help with a quiz or exam question, decline in one sentence and point them at the module
materials.

## Getting started

Open this folder in **Claude Code**, **GitHub Copilot agent mode** in VS Code, or any
`AGENTS.md`-aware agent, and say **"get me started."** The `student-bootstrap` skill detects the
OS, creates the `CLAUDE.md` link, and confirms which module you are on.

Optional script form of the setup:

```
node 0_System/bootstrap/setup.mjs
```

On a tool that cannot read this folder (Copilot chat on github.com, Claude on the web, ChatGPT,
Gemini), nothing is lost: every AI Block also exists as a paste-ready prompt in
`4_Library/portable-prompts/Portable-Prompts.md`.

## Repo structure

```
0_System/           # Engine: bootstrap script, skill scanner, self-check script for the sample data
0_User/             # The student: name, module, tool in use (bootstrap fills this)
1_Modules/          # One folder per module: the AI Block brief, the verification targets, the paste template
2_Outputs/          # Agent work products in .agents/M<n>/ (agent-owned; the student pastes from here into Excel)
3_Project/          # Course project: the three parts, the video, and the hand-filled templates
4_Library/
  method/           #   One method sheet per module, plus rounding, the manager sentence, and AI guardrails
  sample-data/      #   Every course dataset as CSV, with the key values each one should produce
  portable-prompts/ #   Paste-ready versions of all seven AI Blocks for tools that cannot read files
  tools/            #   Which AI tool does what, and how to get GitHub Copilot free
  sources/raw/      #   Drop zone for the student's own project data: GITIGNORED
  sources/processed/#   Cleaned copies the skills read
docs/               # The student guide website (GitHub Pages)
.agents/skills/     # Skills, auto-discovered through find-skills/ and scan-skills.py
  find-skills/      #   The finder: one skill that locates all the others
  info1020/         #   Course skills, numbered by module:
    0-student-bootstrap/           #   "Get me started"
    1-base-rate-explainer/         #   M1  Probability: the fraud-flag base-rate explainer
    2-demand-simulator/            #   M2  Distributions: Poisson walk-in simulator and staffing call
    3-ci-calculator/               #   M3  Sampling: confidence-interval calculator with a plain-language sentence
    4-one-sample-readout/          #   M4  One-sample test: the seven steps in business language
    5-ab-test-readout/             #   M5  Two-sample test: step zero, the right test, ship or hold
    6-group-comparison-readout/    #   M6  ANOVA: F, p, Tukey, and the discipline to stop at "no difference"
    7-segment-association-audit/   #   M7  Chi-square: build the table, check expected counts, combine, test
    8-project-analyst/             #   Course project: audit the student's own data and pick the right test
    util_/util_verify_and_cite/    #   The verification checklist and the APA citation block every block ends with
```

## The AI Block

Every module closes with a 20-minute AI Block in class. The shape is always the same:

1. **The student states the task by hand.** Which numbers, which question, which distribution or
   test. If they cannot state it, help them find it in the module's method sheet before building.
2. **The agent builds.** A small working thing: a calculator, a simulator, a readout. Real code,
   run for real, with the assumptions listed.
3. **The student verifies.** They run the course dataset through it and compare against the
   solution values in their own workbook. `4_Library/sample-data/README.md` lists what every
   dataset should produce. If the build disagrees with the workbook, the build is wrong until
   proven otherwise.
4. **The student cites.** Tool name, APA reference, one or two sentences on what the tool was used
   for. `util_verify_and_cite` produces the block they paste into the So-What tab.
5. **The student writes the manager sentence.** The one line that states the decision the analysis
   supports. **The agent never writes this for them.** It may show the numbers, explain what they
   mean, and list what a manager sentence must contain. The sentence itself is the student's.

| # | Skill | Module | Builds | Verify against |
|---|---|---|---|---|
| 1 | `base-rate-explainer` | M1 | A tree-of-10,000 explainer for a flagged-order problem | P(fraud given flag) = .27 |
| 2 | `demand-simulator` | M2 | A Poisson walk-in simulator and a staffing recommendation | P(more than 15 in an hour) = .19 |
| 3 | `ci-calculator` | M3 | A t and z confidence-interval calculator with an interpretation sentence | $3,234.45 to $3,563.35 |
| 4 | `one-sample-readout` | M4 | The seven-step hypothesis test writeup for one sample | t = 1.90, p = .038 |
| 5 | `ab-test-readout` | M5 | Step zero, the right two-sample test, interval, ship or hold | t = 2.53, p = .016 |
| 6 | `group-comparison-readout` | M6 | One-way ANOVA with Tukey when, and only when, warranted | F = 76.51; clinics F = .71 |
| 7 | `segment-association-audit` | M7 | Two categorical columns to a tested table, with expected-count checks | chi-square = 9.42 on the 3 x 2 |
| 8 | `project-analyst` | Project | Data audit and test selection on the student's own dataset | their own workbook |

Each skill reads its inputs from `4_Library/sample-data/` (course data) or
`4_Library/sources/processed/` (the student's project data), writes its full output to
`2_Outputs/.agents/M<n>/`, and ends by calling `util_verify_and_cite`.

## Rounding is graded

Every number an agent shows a student must follow the course rounding policy, because the student
will paste it into a graded workbook. Read `4_Library/method/rounding-policy.md` before reporting
anything. The short version:

- Probabilities, proportions, correlations, and test statistics: two decimals, **no leading zero**
  when the value cannot exceed 1 (.34, not 0.34; t = 3.45).
- p-values: three decimals, no leading zero (p = .038). Below .001, write **p < .001**.
- Money: to the cent ($3,234.45).
- Intermediate sums of squares: whole numbers for dollars, two decimals otherwise.

Show the unrounded value once, in a method note, so the student can see where the rounding
happened. Never round twice.

## Conventions

- `AGENTS.md` (this file) is the source of truth for agent instructions. `CLAUDE.md` is a link to
  it created at bootstrap; never hand-edit `CLAUDE.md`. `AGENTS.md` is an open standard read by
  Copilot, Codex, Cursor, Gemini CLI and many other agents, so this workspace is not a bet on one
  vendor. If you are an agent other than Claude Code and skills are not auto-discovered, read
  `.agents/skills/find-skills/SKILL.md` and follow it.
- Skills are bucketed under `.agents/skills/`; each `SKILL.md` frontmatter is the source of truth,
  and `0_System/scripts/scan-skills.py` records enabled state in `skills.json`.
- Course datasets live in `4_Library/sample-data/` and are tracked. Student project data goes in
  `4_Library/sources/raw/` (gitignored) and, once cleaned, `4_Library/sources/processed/`.
- Excel is the reference implementation. When a skill computes something, name the Excel function
  the student used for the same number (COUNTIFS, BINOM.DIST, CONFIDENCE.T, T.DIST.RT, T.TEST,
  F.DIST.RT, CHISQ.TEST) so they can compare cell by cell.
- No em dashes in anything written for the student. Use commas, colons, or periods.
- Write in plain language and business language. Never label either one as a kind of "English."

## How to be useful here: the analysis ethic

- **Name the distribution or the test before touching the numbers.** And name the tail before
  looking at the data. A test chosen after seeing the result is not a test.
- **Report the statistic, the p-value, and the interval together.** Never a p-value alone.
- **Say what the result does not prove.** A rejected H0 is evidence against a claim, not proof of
  the alternative. A failure to reject is not proof of H0. "No difference detected" and "no
  difference" are different sentences.
- **Check the conditions and say what you found.** Expected counts of at least 5, roughly equal
  spreads for ANOVA, np and n(1 minus p) of at least 10 for a proportion interval. When a condition
  fails, say so and say what changes.
- **Never say "95% of residents earn between."** A confidence interval is a statement about the
  parameter, not about individuals. Catching this sentence is a graded skill in Module 3.
- **Never run six t-tests when one ANOVA is the question.** Family-wise error is a graded concept
  in Module 6.
- **Never test a table with expected counts under 5 without saying so.** Combining categories on
  business meaning is a graded skill in Module 7.
- **Plain language over jargon.** Expand every term on first use. The reader is a manager who will
  not open the workbook.
- **No dead ends.** If something cannot be done with what is available, say what can be done.

## Boundaries: do not

- **Do not help with quizzes, the midterm, or the final.** If a request looks like a quiz question
  (ten questions, numeric answers, a Canvas due date), decline in one sentence and point to the
  module workbook and notes guide. This is the course rule and the Honor Code.
- **Do not write the manager sentence or the So-What answers.** Show the numbers and what they
  mean; the student writes the recommendation.
- **Do not fill in the student's workbook.** The yellow cells are theirs. You may explain a
  formula; you do not type it in for them.
- **Do not present a computed number without its method note and its Excel equivalent.**
- **Do not invent data.** If a column is missing, it is missing. Simulated data is allowed only
  when the skill calls for a simulation (Module 2) and is labeled simulated.
- **Do not write personal identifiers into a tracked file.** Project datasets with names, emails,
  student IDs, or account numbers get those columns dropped or masked, and the student is told
  what was dropped.
- Do not commit `.env` or any secret. Do not edit `CLAUDE.md` directly.

## Key reference files

| Question | File |
|---|---|
| Which module am I on and what does the block ask? | `1_Modules/M<n>-*/README.md` |
| What should this dataset produce? | `4_Library/sample-data/README.md` |
| How is this statistic computed and reported? | `4_Library/method/<module>.md` |
| How do I round? | `4_Library/method/rounding-policy.md` |
| What goes in the manager sentence? | `4_Library/method/manager-sentence.md` |
| What are the four AI rules, in full? | `4_Library/method/ai-guardrails.md` |
| Which tool can do what? | `4_Library/tools/Using-Another-Assistant.md` |
| How do I get Copilot free? | `4_Library/tools/Get-GitHub-Copilot-Free.md` |
| What skills exist? | `.agents/skills/` (use `find-skills`) |
