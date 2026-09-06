---
name: ab-test-readout
description: >
  Module 5 AI Block. Builds an A/B test readout: given two columns of scores it runs step zero
  (paired or independent, with the reason), picks the right test (Welch t or paired t), reports
  the statistic, df, p, and the interval for the difference, and frames a ship, iterate, or hold
  call against a practical threshold the student sets. Triggers on "run AI Block 5", "A/B test",
  "did the new version win", "two groups", "before and after", "paired or independent", "compare
  these two columns".
---

# ab-test-readout: Module 5 AI Block

The student has run Streamly by hand in tab 2 (t = 2.53, p = .016, interval .16 to 1.44) and the
multitasking pairs in tab 3 (t = 12.52, p < .001). You build the readout. They check you on
Streamly, then feed you the multitasking columns **without saying they are paired** to see whether
you notice.

## Phase 0: step zero, before any statistics

Look at the shape of the data and ask one question: **is each row one unit measured twice, or
are the two columns different units?**

- Same customer, store, or student on both sides of a row: **paired**. Analyze the column of
  differences as a one-sample test.
- Different people in each group, no row-by-row link: **independent**. Welch t-test.

Signals that data are paired even when nobody says so: equal n with a row identifier that is a
person or a unit, column names like Round 1 and Round 2 or Before and After, and differences that
are far less variable than either column. `Multitasking_Example14.csv` has all three. Say which
you found and why. If you cannot tell, ask; do not guess and do not default to independent.

Then, before the data: the parameter in words, H0 (no difference), Ha and its tail from the
business question (Streamly: is the new flow better or worse, two-tailed), alpha.

## Phase 1: independent samples (Streamly)

```
A (current): n = 40, mean = 7.44, sd = 1.60
B (new):     n = 40, mean = 8.24, sd = 1.21
difference B - A = .80
SE = SQRT(sA^2/40 + sB^2/40) = .317              (Welch: variances not pooled, say so)
t = .80 / .317 = 2.53
df: conservative = 39 (smaller n - 1)  -> p = .016      Excel: =T.DIST.2T(2.53, 39)
    Welch df                            -> p = .014      Excel: =T.TEST(A, B, 2, 3)
t* (95%, df 39) = 2.023                                 Excel: =T.INV.2T(.05, 39)
95% interval for the difference: .80 +/- 2.023 x .317 = .16 to 1.44
```

Report both p-values and say which one the workbook uses (conservative df, .016) and why they
differ. Never pool unless the student has a reason to believe the spreads are equal; if they ask,
show the pooled result (`T.TEST(...,2,2)`) next to Welch and explain the difference.

## Phase 2: paired samples (multitasking)

```
d = Round 2 - Round 1 for each student; n = 14
d-bar = 28.14 s, s_d = 8.41, SE = 2.25
t = 28.14 / 2.25 = 12.52, df = 13, p < .001            Excel: =T.TEST(R1, R2, 2, 1)
```

If the student fed you this as two unlabeled columns and you had run it as independent, say so
plainly and show both results side by side; the gap between them is the lesson.

## Phase 3: practical significance and the call

Ask for the **practical threshold** before making the call: how much would CX have to rise to be
worth shipping the new flow? If the student has not decided, show the table and let them place
their threshold on it:

| Interval versus threshold | Call |
|---|---|
| Whole interval above the threshold | Ship |
| Interval straddles the threshold | Iterate or extend the test |
| Whole interval below the threshold | Hold |
| Interval includes zero and is narrow | Hold: no meaningful effect |
| Interval includes zero and is wide | Inconclusive: run a bigger test |

Streamly's interval is .16 to 1.44. Against a threshold of .50, it straddles; against .10, it
clears. Say that the threshold changes the recommendation more than any statistic does. List what
the manager sentence must contain (the call, the difference with its interval, the p-value, and
the threshold it was judged against). Do not write it.

## Phase 4: make it reusable

Offer the readout as a function that takes two columns and a `paired` flag (default: ask), plus
the threshold, and returns step zero, the test, the numbers, and the table row that applies.

## Phase 5: verify and cite

Call `util_verify_and_cite` with target **Streamly t = 2.53, p = .016 (conservative), .014
(Welch), 95% CI .16 to 1.44; multitasking paired t = 12.52, p < .001** and the classic errors to
check: pooled by default, pairing missed, p reported without the interval. Write to
`2_Outputs/.agents/M5/AB-Test-Readout.md`.

## Guardrails

- Step zero first, stated with a reason.
- Welch unless told otherwise, and say which df you used.
- Interval next to the p-value, every time.
- "Not significant" is never written as "no effect." Say what the interval rules out.
- The ship or hold call is the student's once they set the threshold.
