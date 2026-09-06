---
name: ci-calculator
description: >
  Module 3 AI Block. Builds a confidence-interval calculator for a mean (t) and a proportion (z)
  that checks the conditions, computes the interval, gives the sample size for a target margin,
  and writes a one-sentence interpretation in correct language. Triggers on "run AI Block 3",
  "confidence interval", "margin of error", "how many should we survey", "95% interval for
  income", "is this range right".
---

# ci-calculator: Module 3 AI Block

The student has built Angela Green's intervals by hand in tabs 3 to 5 (income $3,234.45 to
$3,563.35; the proportion intervals not reportable at n = 20; survey 48). You build the
calculator and its sentence. They check you against tab 3, and they check your sentence for the
one error the module is about.

## Phase 0: inputs

Accept either a column of data (`GreenValleyCommons_Residents.csv`, column `Monthly income ($)`)
or the summary: n, mean, sd, confidence level. For a proportion: n and the count (or p-hat). Ask
which parameter the student is estimating, in words: "the true mean monthly income of Green Valley
Commons residents." That sentence becomes the subject of the interpretation.

## Phase 1: the mean (t)

State the method before the number: sd is unknown, so the t distribution with df = n minus 1.
Compute and show every intermediate value unrounded once, then rounded:

```
n = 20      mean = 3398.90      sd = 351.38
SE = sd / SQRT(n) = 78.57                       Excel: =STDEV.S(range)/SQRT(20)
t* (95%, df 19) = 2.093                         Excel: =T.INV.2T(.05, 19)
margin = t* x SE = 164.45                       Excel: =CONFIDENCE.T(.05, 351.38, 20)
interval = 3234.45 to 3563.35
```

Also give the 90% interval (3263.04 to 3534.76) so the student sees the width shrink.

## Phase 2: the proportion (z), with the condition first

Before computing, check n p-hat and n (1 minus p-hat), both at least 10. Print the check.

- Within 5 miles of a doctor: 10 of 20, p-hat = .50: 10 and 10, borderline, report with the caveat.
- Male: 8 of 20, p-hat = .40: 8 and 12, **fails**. Do not print an interval. Print: "not
  reportable at n = 20; see the sample-size step."

When the condition passes: p-hat plus or minus 1.960 x SQRT(p-hat (1 minus p-hat) / n).
Excel: `=NORM.S.INV(.975)`.

## Phase 3: sample size for a target margin

For the mean: n = (1.96 x sd / margin)^2, rounded **up**. $100 margin: 47.4, so **48**. $150
margin: 22. For a proportion with no estimate, p = .5: n = (1.96 / (2 x margin))^2. Show the
formula and the rounding direction; rounding down is the classic error.

## Phase 4: the sentence

Write exactly one interpretation sentence per interval and label it as a draft the student may
use as a model, not as their manager sentence:

> "We are 95% confident that the true mean monthly income of Green Valley Commons residents is
> between $3,234.45 and $3,563.35, based on a sample of 20."

Then show the two sentences that are **wrong** and why, because the student is graded on
catching them:

- "95% of residents earn between $3,234 and $3,563." (about individuals, not the parameter)
- "There is a 95% probability the true mean is in this range." (the mean is fixed; the interval
  is what varies)

## Phase 5: make it reusable

Offer the calculator as a small function or a four-input table (n, mean, sd, level; or n, count,
level) with the condition check built in. Run one extra case on SummitGear (n = 40 from the
250-order population, sd $36.99, SE $5.85) so the student sees the same machine on Lab 3A.

## Phase 6: verify and cite

Call `util_verify_and_cite` with target **$3,234.45 to $3,563.35 (t* = 2.093, SE $78.57);
proportion intervals not reportable at n = 20; survey 48** and the classic errors to check: z
instead of t for the mean, probability language in the sentence, an interval reported despite a
failed condition. Write to `2_Outputs/.agents/M3/CI-Calculator.md`.

## Guardrails

- t for a mean with unknown sd. Always.
- Condition check before any proportion interval, printed.
- Never round SE before multiplying by t*.
- Money to the cent; t* and z* to three decimals.
- One model sentence, clearly labeled; the So-What sentence is the student's.
