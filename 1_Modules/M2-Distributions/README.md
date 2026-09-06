# Module 2: Probability distributions

**In the lab:** Lab 2A: University of Highlands Ranch registration (expected value, binomial, Poisson). Lab 2B: Mt. Highlands Ranch skier counts (normal) and lift stops (uniform).

Method sheet: `4_Library/method/m2-*.md`. Verification targets:
`4_Library/sample-data/README.md`, Module 2 section.

## AI Block 2

**You build:** A demand-planning simulator. Given an average arrival rate, it simulates walk-ins per hour, reports the probability of exceeding a capacity, and recommends staffing for a busy hour with the risk stated.

**Inputs you give the tool:** Average 12.5 walk-ins per hour (Poisson). Capacity to test: 15 per hour. Optional: the skier counts file for a second run with the normal.

**Data file:** MtHighlands_SkierCounts.csv (optional) (in `4_Library/sample-data/`).

**Verify against:** P(more than 15 walk-ins in an hour) = .19; sd = 3.54.

**The guardrail this block teaches:** Make the tool state the distribution it assumed before it computes anything. If it did not say Poisson, or if it used the binomial with an invented n, the build is wrong.

## How to run it

- With an agent that can read this folder: say **"run AI Block 2"** (skill `demand-simulator`).
- With a chat tool: paste prompt 2 from `4_Library/portable-prompts/Portable-Prompts.md`
  and upload the data file.

Then fill `AI-Block-2-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
