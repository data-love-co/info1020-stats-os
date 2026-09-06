# The manager sentence

Every module in INFO 1020 ends with one line: the decision the analysis supports, written for a
manager who will not open the workbook. The student writes it. The agent may check it.

## What it must contain

1. **The decision or recommendation**, as a verb. Fund it, do not fund it, target this group,
   keep the current flow, survey 48 more residents.
2. **The evidence, in business units.** A rate, a dollar amount, a difference, a range. Not a
   test statistic. The statistic goes in the memo body, not the sentence.
3. **The confidence, honestly.** "The 95% interval runs from $3,234 to $3,563." "The evidence is
   strong (p < .001)." "The data cannot settle this yet."
4. **What it does not prove**, when that matters. "This does not mean every flagged order is
   legitimate." "No difference was detected, which is not the same as no difference."

## Templates by module

| Module | Skeleton |
|---|---|
| M1 Probability | "[Group] is the better target: [rate] of them [behavior], against [rate] overall. One caution: [data limit]." |
| M2 Distributions | "Plan for [number] per [period]; there is a [probability] chance of exceeding [threshold], so [staffing or budget action]." |
| M3 Confidence intervals | "We are 95% confident the true [parameter] is between [low] and [high]; with [n] respondents that range is [wide or narrow enough] to [decision]." |
| M4 One-sample test | "[Decision on the claim]: the sample mean of [value] is [above or below] [claimed value], p = [p], so [action]. The test does not prove [the alternative]; it shows the claim is [not] consistent with the data." |
| M5 Two-sample test | "[Ship or hold]: [B] scored [difference] higher than [A] (95% interval [low] to [high], p = [p]), which [does or does not] clear the [practical threshold]." |
| M6 ANOVA | "The [groups] differ (F = [F], p [p]); [tier statement from Tukey]. For [group] there is no detectable difference, so [action]." |
| M7 Chi-square | "[Variable A] and [variable B] are related (chi-square = [value], p = [p]): [the cell that drives it], so [bundle or targeting action]. One caution: [sample size or combined categories]." |

## Classic errors an agent should catch

- "95% of residents earn between" (probability language on an interval).
- "This proves the new flow is better" (a test never proves).
- "No difference" when the sentence should say "no difference detected."
- A p-value with no effect size or interval next to it.
- A rate with no base: ".78" without "of Rewards members."
- Leading zeros on probabilities and p-values.
