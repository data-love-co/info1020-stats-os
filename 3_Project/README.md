# Course project

Thirty percent of the grade, in three parts plus a recorded presentation. You find your own
dataset, clean it, describe it, and run the tests we learn on it. You may work with a partner.
Sports datasets are strongly discouraged. Every deadline is a Sunday at 11:59 PM, at least a full
week after the class that teaches what the part requires. Canvas has the rubrics, the video
specs, and the dataset resources; this folder has the working templates and the AI rules for the
project.

| Part | Due | What it contains |
|---|---|---|
| Part 1 | Sunday, September 27 | The decision frame and the data audit: what decision the data should support, and whether it can |
| Part 2 | Sunday, October 25 | Confidence intervals and one- and two-sample tests on your data, plus an AI-built artifact with its citation trail |
| Part 3 | Sunday, November 8 | ANOVA and chi-square where they apply, and the full written decision memo |
| Video | Sunday, November 15 | A recorded presentation of your findings with an infographic or a slide deck |

## Data rules

- Your raw file goes in `4_Library/sources/raw/`. That folder is gitignored; nothing there leaves
  your machine through this repo.
- A few hundred rows, at least one numeric variable and two categorical variables.
- No personal identifiers in anything you paste into a tracked file or an AI tool: names,
  emails, IDs, addresses. Drop or mask them first. `project-analyst` does this for you and tells
  you what it dropped.

## The AI rules on the project

Same four: verify, cite, add value, never on quizzes or exams. On the project specifically:

- The agent audits, computes, and lists what each deliverable must contain. **You fill the
  templates by hand.** The templates are in `templates/`.
- Part 2 requires an AI-built artifact with its citation trail. The readout the agent builds on
  your data is that artifact. Verify it against numbers you computed in Excel yourself.
- The decision memo in Part 3 is yours. The agent may list what it must contain and check a draft
  for the classic errors; it does not write it.

Say **"help me with Part 1"** (or 2, or 3) to start.
