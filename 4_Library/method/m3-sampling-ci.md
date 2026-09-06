# M3: Sampling and confidence intervals

**The question:** the data you have is never the whole world. How much should you trust a number
computed from a sample, and how do you report it as a range a manager can defend?

## Population, sample, sampling distribution

- **Population:** everyone or everything the decision is about. Usually unavailable.
- **Sample:** the rows you actually have. SummitGear's 250 orders were one quarter of one year.
- **Sampling distribution:** what the sample statistic would look like across many samples of the
  same size. Its spread is the **standard error**.

For a mean: SE = sd / SQRT(n). For n = 40 SummitGear orders with sd $36.99, SE = $5.85. The
**Central Limit Theorem** says the sampling distribution of the mean is close to normal once n is
around 30 or more, whatever shape the data has, so `NORM.DIST` on the sample mean is legitimate.

## Confidence interval for a mean (sd unknown: use t)

point estimate plus or minus t* times SE

- t* comes from the t distribution with df = n minus 1: `T.INV.2T(.05, n-1)` for 95%.
- Margin of error in one call: `CONFIDENCE.T(.05, sd, n)`.
- Green Valley Commons, 20 residents: $3,398.90 plus or minus 2.093 times $78.57, so **$3,234.45
  to $3,563.35**.

Use z (`NORM.S.INV(.975)` = 1.960) only when the population sd is known, which in practice means
almost never for a mean.

## Confidence interval for a proportion (use z)

p-hat plus or minus z* times SQRT(p-hat (1 minus p-hat) / n)

**Check the condition first:** n times p-hat and n times (1 minus p-hat) must both be at least 10.
With 20 residents and p-hat = .40, that is 8 and 12. The interval is not reportable. The honest
sentence is "not yet: survey more residents."

## Sample size for a target margin of error

For a mean: n = (z* times sd / margin)^2, rounded **up**. For a $100 margin at 95% with sd $351.38:
(1.96 times 351.38 / 100)^2 = 47.4, so **48**. For a proportion with no prior estimate use p = .5:
n = (z* / (2 times margin))^2.

## Interpreting an interval

Right: "We are 95% confident the true mean monthly income of residents is between $3,234 and
$3,563." The confidence is in the method: 95 of 100 such intervals would capture the true mean.

Wrong, and graded: "95% of residents earn between $3,234 and $3,563." An interval is about the
parameter, not about individuals. "There is a 95% probability the mean is in this range" is also
wrong; the mean is fixed, the interval is what varies.

## Reporting

Interval endpoints to the cent for money, two decimals otherwise. t* and z* to three decimals.
Always state n and the confidence level in the same sentence as the interval.

## Classic mistakes

- Using z for a mean with an unknown sd.
- Reporting a proportion interval that fails the condition.
- Rounding SE before multiplying by t*.
- Probability language about individuals.
