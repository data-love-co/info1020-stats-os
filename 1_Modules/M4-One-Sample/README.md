# Module 4: One-sample hypothesis testing

**In the lab:** Lab 4A: Denice Toney, Summit Ridge Bank, 16 balances, a right-tailed test against $2,500 and a two-tailed test against $2,800. Lab 4B: Angela Green returns with 48 residents and a proportion test against .40.

Method sheet: `4_Library/method/m4-*.md`. Verification targets:
`4_Library/sample-data/README.md`, Module 4 section.

## AI Block 4

**You build:** A hypothesis-test readout generator. Given a column of numbers (or n, mean, sd), a claimed value, the tail, and alpha, it returns all seven steps in business language plus the interval.

**Inputs you give the tool:** DeniceToney_Balances.csv, claimed value $2,500, right-tailed, alpha .05. Then $2,800, two-tailed.

**Data file:** DeniceToney_Balances.csv (in `4_Library/sample-data/`).

**Verify against:** t = 1.90, p = .038 right-tailed, critical 1.753, reject; two-tailed against $2,800: t = -1.88, p = .079, fail to reject.

**The guardrail this block teaches:** Give it the tail before the data. If it "chose" a tail after seeing the mean, it failed. Ask it whether the result proves H0 false, and check that it says no.

## How to run it

- With an agent that can read this folder: say **"run AI Block 4"** (skill `one-sample-readout`).
- With a chat tool: paste prompt 4 from `4_Library/portable-prompts/Portable-Prompts.md`
  and upload the data file.

Then fill `AI-Block-4-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
