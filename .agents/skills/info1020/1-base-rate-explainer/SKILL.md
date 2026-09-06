---
name: base-rate-explainer
description: >
  Module 1 AI Block. Builds a tree-of-10,000 base-rate explainer for a flag or test (fraud
  detection, a screening test, a spam filter): given the base rate, the catch rate, and the
  false-alarm rate it computes P(condition given flag) and explains, in plain language, why a flag
  is usually wrong when the condition is rare. Triggers on "run AI Block 1", "base rate", "fraud
  flag", "why is a flagged order not fraud", "positive predictive value", "the 2% 90% 5% problem".
---

# base-rate-explainer: Module 1 AI Block

The student has just worked SummitGear's fraud-flag problem by hand in tab 4 of their workbook.
You build the reusable version and explain it to a finance manager. They check you against tab 4.

## Phase 0: get the three rates from the student

Ask for, or confirm, three numbers. Do not assume them; the point is that the student states the
problem.

- **Base rate**: the share of all cases that have the condition. Course value: 2% of orders are
  fraudulent.
- **Catch rate** (sensitivity): the share of true cases the detector flags. Course value: 90%.
- **False-alarm rate**: the share of legitimate cases the detector flags anyway. Course value: 5%.

Say back what you heard as a sentence: "2 in 100 orders are fraud; the system catches 9 of 10
frauds; it also flags 1 in 20 legitimate orders."

## Phase 1: build the tree of 10,000

Compute for real (Python, or shown arithmetic). Never a single formula with no intermediate
counts; the counts are what make the explanation land.

```
10,000 orders
  fraudulent:   10,000 x .02  =   200
    flagged:      200 x .90   =   180   (true flags)
    missed:       200 x .10   =    20
  legitimate:   10,000 x .98  = 9,800
    flagged:    9,800 x .05   =   490   (false flags)
    not flagged:                9,310
flags in all: 180 + 490 = 670
P(fraud given flagged) = 180 / 670 = .27
P(legitimate given flagged) = 490 / 670 = .73
P(fraud given not flagged) = 20 / 9,330 = .00
```

Excel equivalent for the student: the same four cells in tab 4, and `=180/670` formatted `.00`.

## Phase 2: the explanation for a finance manager

Write four to six sentences in business language. Requirements:

- Lead with the count, not the probability: "Of every 670 orders the system flags, about 180 are
  fraud and about 490 are legitimate customers."
- Name the reason in one sentence: fraud is rare, so even a small false-alarm rate on the huge
  legitimate pile outnumbers the real catches.
- Say what the number is **not**: it is not the detector's accuracy (the detector catches 90% of
  fraud, which is a different question), and .27 is not "the detector is wrong 73% of the time."
- End with what it implies operationally, without deciding for the manager: a flag is a reason to
  review, not to cancel; the cost of a wrong cancellation falls on a real customer.
- Do **not** write the manager sentence for the So-What tab. List what it must contain (the .27,
  the 490, the "review not cancel" idea, and one data limit) and stop.

## Phase 3: make it reusable

Offer a small calculator (a Python function or a three-input table) that takes base rate, catch
rate, and false-alarm rate and returns the tree and P(condition given flag). Show it working on
two extra cases so the student sees the base rate move the answer: 10% base rate (P = .67) and
.5% base rate (P = .08). Label these as illustrations, not course numbers.

## Phase 4: verify and cite

Call `util_verify_and_cite` with target **P(fraud given flagged) = .27, 180 true flags, 490 false
flags, 670 flags** and the classic error to check: confusing P(flag given fraud) = .90 with
P(fraud given flag) = .27. Write the full output to `2_Outputs/.agents/M1/Base-Rate-Explainer.md`.

## Guardrails

- Never state the rates as facts; get them from the student.
- Never round the intermediate counts. 180, 490, and 670 are exact.
- Report .27, two decimals, no leading zero.
- Never say the detector is "27% accurate."
- Never write the So-What answers.
