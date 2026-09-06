# M6: ANOVA, comparing several groups

**The question:** four career paths, three states, five product lines. Do the group means differ,
and if so, which ones?

## Why not six t-tests

Each test at alpha = .05 has a 5% false-alarm chance. Six independent tests: 1 minus .95^6 = **.26**.
Three tests: .14. ANOVA tests all the means in **one** test, so the family-wise error stays at .05.
Then, only if H0 is rejected, a post-hoc test with a correction says which pairs differ.

## The seven steps, ANOVA version

1. Parameter: the true mean of each group. 2. H0: all group means are equal. 3. Ha: at least one
differs (always one-tailed, upper). 4. Statistic: F = MSB / MSW. 5. Critical value:
`F.INV.RT(.05, dfB, dfW)`. 6. p-value: `F.DIST.RT(F, dfB, dfW)`. 7. Decide, then Tukey if
rejected.

## The ANOVA table, by hand from group summaries

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between groups | SSB = sum of n_i (x-bar_i minus grand mean)^2 | k minus 1 | SSB / dfB | MSB / MSW |
| Within groups | SSW = sum of (n_i minus 1) s_i^2 | N minus k | SSW / dfW | |
| Total | SST = SSB + SSW | N minus 1 | | |

Career Services: k = 4, N = 80, SSB = 3721172720, SSW = 1232181262, dfB = 3, dfW = 76,
MSB = 1240390907, MSW = 16212911, **F = 76.51**, F* = 2.72, p < .001. Reject.

Atlas clinics: k = 3, N = 60, **F = .71**, F* = 3.16, p = .494. Fail to reject. Stop there.

The ToolPak (Data, Data Analysis, Anova: Single Factor) produces the same table; use it to check
the hand build, not to replace it.

## Conditions

1. Independent random samples in each group.
2. Roughly normal within groups, or n large enough (20 per group is fine).
3. Roughly equal spreads: largest sd divided by smallest sd under about 2. Career Services is
   2.19: **report it as borderline and proceed**, saying that a robust follow-up would confirm.
   Hiding a borderline check is worse than reporting one.

## Tukey HSD, only after a rejected H0

HSD = q times SQRT(MSW / n) with q from the studentized range table for k groups and dfW (q = 3.7149
for k = 4, df = 76). Career Services: **HSD = $3,344.70**. Any pair of means more than HSD apart
differs. Five of six pairs differ; OR Analyst and Computer Analyst ($1,878.43 apart) do not. The
manager sentence is about tiers, not "they differ."

Never run Tukey on the clinics. A post-hoc test after a failed F is fishing.

## Reporting

"F(3, 76) = 76.51, p < .001." SS and MS as whole numbers for dollars, two decimals for minutes.
HSD to the cent. Group means to the cent.

## Classic mistakes

- Six t-tests.
- Tukey after a failed F, or no Tukey after a rejected one.
- Reading "fail to reject" as "the states are identical." No difference detected is the sentence.
- Skipping the spread check, or hiding a borderline result.
