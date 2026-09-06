# Module 5: Two-sample hypothesis testing

**In the lab:** Lab 5A: Streamly, a randomized A/B test of an onboarding flow, 40 customers per variant. Lab 5B: the multitasking experiment, run live on the class, a paired test.

Method sheet: `4_Library/method/m5-*.md`. Verification targets:
`4_Library/sample-data/README.md`, Module 5 section.

## AI Block 5

**You build:** An A/B test readout. Given two columns of scores, it returns step zero (paired or independent, with the reason), the right test, t, df, p, the interval for the difference, and a ship, iterate, or hold call against a practical threshold you set.

**Inputs you give the tool:** Streamly_ABTest_CX.csv. Then Multitasking_Example14.csv, without telling it the columns are paired.

**Data file:** Streamly_ABTest_CX.csv, Multitasking_Example14.csv (in `4_Library/sample-data/`).

**Verify against:** Streamly: t = 2.53, p = .016 (conservative df 39; .014 Welch df), 95% CI .16 to 1.44. Multitasking paired: t = 12.52, p < .001.

**The guardrail this block teaches:** Did it say Welch or pooled? Did it notice the multitasking columns are paired when you did not say so? Did it report the interval next to the p-value?

## How to run it

- With an agent that can read this folder: say **"run AI Block 5"** (skill `ab-test-readout`).
- With a chat tool: paste prompt 5 from `4_Library/portable-prompts/Portable-Prompts.md`
  and upload the data file.

Then fill `AI-Block-5-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
