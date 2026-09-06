# Module 3: Sampling and confidence intervals

**In the lab:** Lab 3A: SummitGear as a population, samples of 40, the sampling distribution and the standard error. Lab 3B: Angela Green, 20 residents of Green Valley Commons, intervals for income and two proportions, a sample-size recommendation.

Method sheet: `4_Library/method/m3-*.md`. Verification targets:
`4_Library/sample-data/README.md`, Module 3 section.

## AI Block 3

**You build:** A confidence-interval calculator for a mean (t) and a proportion (z) that checks the proportion condition and writes the one-sentence interpretation a manager could read aloud.

**Inputs you give the tool:** GreenValleyCommons_Residents.csv, or n = 20, mean $3,398.90, sd $351.38, 95%.

**Data file:** GreenValleyCommons_Residents.csv (in `4_Library/sample-data/`).

**Verify against:** 95% interval for mean income $3,234.45 to $3,563.35 (t* = 2.093, SE $78.57); proportion intervals not reportable at n = 20.

**The guardrail this block teaches:** Read its sentence. If it says "95% of residents earn between" or "there is a 95% probability the mean is between," it failed. If it used z for the mean, it failed. If it reported the gender proportion interval without checking np and n(1 minus p), it failed.

## How to run it

- With an agent that can read this folder: say **"run AI Block 3"** (skill `ci-calculator`).
- With a chat tool: paste prompt 3 from `4_Library/portable-prompts/Portable-Prompts.md`
  and upload the data file.

Then fill `AI-Block-3-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
