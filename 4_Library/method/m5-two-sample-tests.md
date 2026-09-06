# M5: Two-sample hypothesis tests

**The question:** did the new version beat the old one, does this group differ from that group,
did the intervention change anything? Same seven steps as Module 4; only the statistic changes.

## Step zero: paired or independent?

Ask it before anything else, and defend the answer.

- **Paired:** the same unit measured twice, or units matched one to one. Each student timed
  before and after; each store before and after a change. Analyze the **column of differences**
  as a one-sample test.
- **Independent:** different units in each group, no row-by-row link. 40 customers saw variant A,
  40 different customers saw variant B.

The wrong call gives the wrong answer. Paired data run as independent throws away the pairing and
usually understates the effect (the multitasking data give t = 12.52 paired; run as independent
they give a much smaller t). Independent data run as paired is meaningless.

## Independent samples: the Welch t-test (the course default)

t = (x-bar1 minus x-bar2) / SQRT(s1^2/n1 + s2^2/n2)

- df: the course uses the **conservative** df = the smaller n minus 1 (39 for Streamly) by hand;
  `T.TEST(range1, range2, 2, 3)` uses the Welch df and gives a slightly smaller p (.014 versus
  .016). Say which you used.
- Do not pool variances (type 2 in T.TEST) unless you have a reason to believe the spreads are
  equal. Welch is safe either way.
- Streamly: 8.24 minus 7.44 = .80, SE = .317, **t = 2.53, p = .016** two-tailed. 95% interval for
  the difference: .80 plus or minus 2.023 times .317 = **.16 to 1.44**.

## Paired samples

d-bar = mean of the differences, s_d = their sd, SE = s_d / SQRT(n), t = d-bar / SE, df = n minus
1. `T.TEST(range1, range2, 2, 1)`. Multitasking: d-bar = 28.14 s, s_d = 8.41, SE = 2.25,
**t = 12.52, p < .001**.

## Interval for a difference

Report it next to the p-value. Its width says how much you learned; its location against the
practical threshold says whether to act.

## Statistical versus practical significance

Streamly's lift of .80 on a 10-point scale is significant. Whether it is worth shipping depends on
what a point of CX is worth and what the new flow costs. The readout ends in **ship, iterate, or
hold**, and the interval against the threshold decides:

| Interval versus threshold | Call |
|---|---|
| Whole interval above the threshold | Ship |
| Interval straddles the threshold | Iterate or extend the test |
| Whole interval below the threshold | Hold |
| Interval includes zero and is narrow | Hold: no meaningful effect |
| Interval includes zero and is wide | Inconclusive: underpowered |

## Reporting

"t(39) = 2.53, p = .016, two-tailed; the new flow scored .80 higher (95% CI .16 to 1.44)." State
paired or independent, Welch or pooled, and the df you used.

## Classic mistakes

- Skipping step zero.
- Pooling by default.
- Reporting p without the difference and its interval.
- "Not significant" read as "no effect" when the interval is wide.
