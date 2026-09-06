---
name: group-comparison-readout
description: >
  Module 6 AI Block. Builds a group-comparison readout: given three or more columns it reports k,
  the group means, the spread check, the one-way ANOVA table, F, the critical value and p, whether
  a follow-up is warranted, which pairs differ by Tukey HSD when it is, and what a recommendation
  must contain. Stops at "no difference detected" when F fails. Triggers on "run AI Block 6",
  "three or more groups", "ANOVA", "do the groups differ", "which groups differ", "Tukey",
  "compare four career paths".
---

# group-comparison-readout: Module 6 AI Block

The student has built the salary ANOVA by hand in tab 2 (F = 76.51), Tukey in tab 3 (HSD
$3,344.70), and the clinics in tab 4 (F = .71, stop). You build the readout. They check you on
the salaries, then feed you the clinics to see whether you have the discipline to stop.

## Phase 0: inputs and the question

Accept a file with one column per group (`CareerServices_Salaries.csv`: OR Analyst, Accountant,
Computer Analyst, Financial Specialist; `Clinic_WaitTimes.csv`: Florida, New York, North
Carolina) or pasted columns. Confirm in words what the groups are and what is measured. State H0
(all group means equal) and Ha (at least one differs) and alpha before computing.

**Do not run pairwise t-tests.** If the student asks for them, compute the family-wise error rate
first (six comparisons at .05: 1 minus .95^6 = .26) and explain in two sentences why ANOVA comes
first.

## Phase 1: describe and check the conditions

Report n, mean, and sd per group, to the cent, and the grand mean. Then the spread check: largest
sd divided by smallest sd. Salaries: 2.19. Say it is borderline against the rule of thumb of 2,
that the course reports it and proceeds, and that a robust follow-up (Welch ANOVA) would confirm.
**Never hide a borderline check.** Note independence and rough normality with 20 per group.

## Phase 2: the ANOVA table, by hand

Compute from the group summaries, show the table, and give the ToolPak path (Data, Data Analysis,
Anova: Single Factor) as the check:

```
Source    SS            df   MS            F        F*      p
Between   3721172720     3   1240390907    76.51    2.72    < .001     Excel: =F.INV.RT(.05,3,76), =F.DIST.RT(76.51,3,76)
Within    1232181262    76   16212911
Total     4953353982    79
```

SSB = sum of n_i (x-bar_i minus grand)^2; SSW = sum of (n_i minus 1) s_i^2. Whole numbers for
dollars. Decide: F = 76.51 > 2.72, p < .001, reject H0. **Follow-up warranted.**

## Phase 3: Tukey HSD, only when warranted

HSD = q x SQRT(MSW / n) with q from the studentized range table (k = 4, df = 76: q = 3.7149).
HSD = $3,344.70. Then every pair:

| Pair | Difference | Differs? |
|---|---|---|
| OR Analyst vs Computer Analyst | $1,878.43 | no |
| Accountant vs Financial Specialist | $4,504.65 | yes |
| OR Analyst vs Accountant | $10,004.99 | yes |
| Accountant vs Computer Analyst | $11,883.42 | yes |
| OR Analyst vs Financial Specialist | $14,509.64 | yes |
| Computer Analyst vs Financial Specialist | $16,388.07 | yes |

Turn the pairs into tiers (OR Analyst and Computer Analyst together at the top, then Accountant,
then Financial Specialist). The manager sentence is about tiers, not "they differ."

## Phase 4: the clinics, and stopping

Run the same readout on `Clinic_WaitTimes.csv`: F = .71, F* = 3.16, p = .494. Fail to reject.
**Do not run Tukey.** Write: "No difference in mean wait time was detected across the three
states with 20 days each. This is not the same as no difference; a larger sample or a different
measure could still find one." List what the reply to the operations director must contain (the
finding, what it does not prove, what evidence would change it). Do not write it.

## Phase 5: make it reusable

Offer the readout as a function that takes any number of columns and returns the descriptives,
the spread check, the table, the decision, and Tukey only on a rejected H0.

## Phase 6: verify and cite

Call `util_verify_and_cite` with target **salaries F = 76.51, p < .001, HSD $3,344.70, all pairs
differ except OR Analyst vs Computer Analyst; clinics F = .71, p = .494, no follow-up** and the
classic errors to check: six t-tests, Tukey after a failed F, spread check hidden. Write to
`2_Outputs/.agents/M6/Group-Comparison-Readout.md`.

## Guardrails

- One ANOVA, never a pile of t-tests.
- Conditions reported, including the borderline one.
- Tukey only after a rejected H0.
- "No difference detected," never "no difference."
- SS and MS as whole numbers for dollars, two decimals for minutes; HSD and means to the cent.
