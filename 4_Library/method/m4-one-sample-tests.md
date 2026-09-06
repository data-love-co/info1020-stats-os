# M4: One-sample hypothesis tests

**The question:** somebody has made a claim about a population number. You have a sample. Is your
evidence strong enough to call the claim wrong?

## The seven steps (every test in the course uses them)

1. **Parameter.** Name the population quantity in words: "the true mean balance of mid-tier
   accounts."
2. **H0.** The claim, as an equality: H0: mu = 2500.
3. **Ha.** What you would conclude if H0 fails. **Choose the tail from the business question,
   before looking at the data.** Denice funds the promotion only if the mean is above $2,500, so
   Ha: mu > 2500 (right-tailed). "Is it different from $2,800" is two-tailed: Ha: mu not equal
   2800.
4. **Test statistic.** t = (x-bar minus mu0) / (s / SQRT(n)), df = n minus 1. Use z for a
   proportion: z = (p-hat minus p0) / SQRT(p0 (1 minus p0) / n).
5. **Rejection region and picture.** alpha (usually .05), the critical value, and a sketch of the
   tail. `T.INV(.95, df)` right tail; `T.INV.2T(.05, df)` two tails; `NORM.S.INV(.95)` = 1.645.
6. **Compute.** The statistic and the p-value. `T.DIST.RT(t, df)` right tail; `T.DIST(t, df, TRUE)`
   left tail; `T.DIST.2T(ABS(t), df)` two tails; `1 - NORM.S.DIST(z, TRUE)` for a right-tailed z.
7. **Decide and interpret.** Reject H0 if p < alpha (equivalently, if the statistic is beyond the
   critical value). Then say what it means in business language, and what it does not prove.

## Denice Toney, worked

n = 16, x-bar = $2,650.68, s = $317.11, SE = $79.28. Right-tailed against $2,500: t = 1.90,
critical 1.753, **p = .038**. Reject at .05. The evidence supports a mean above $2,500. It does
not prove the mean is $2,650; the 95% interval is $2,481.70 to $2,819.66, and it does not say the
promotion will work.

Two-tailed against $2,800: t = -1.88, p = .079. Fail to reject. "The data are consistent with a
$2,800 mean" is not "the mean is $2,800."

## Errors

- **Type I:** rejecting a true H0. Its probability is alpha. Fund a promotion the segment cannot
  support.
- **Type II:** failing to reject a false H0. Its probability is beta; power = 1 minus beta. Miss a
  promotion that would have paid off.
- Lowering alpha lowers Type I and raises Type II. A larger sample lowers both. "Just use alpha =
  .10" is choosing to accept more false alarms; say so.

## The confidence interval and the two-tailed test

A 95% interval that excludes mu0 is the same decision as a two-tailed test at .05 that rejects.
The interval is the more useful thing to report because it shows the size of the effect.

## Reporting

t to two decimals, p to three with no leading zero, critical values to three. Always report the
tail, alpha, the statistic, the p-value, and the decision in one line: "t(15) = 1.90, p = .038,
right-tailed, reject H0 at .05."

## Classic mistakes

- Picking the tail after seeing which way the sample mean fell.
- Doubling a right-tailed p for a two-tailed question, or forgetting to.
- "Accept H0." You fail to reject; you never accept.
- "The test proves the mean is above $2,500." It provides evidence against the claim of $2,500.
