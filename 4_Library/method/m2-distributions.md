# M2: Probability distributions

**The question:** when the business can describe how something behaves (a fixed number of
yes-or-no trials, arrivals per hour, a bell-shaped measurement, an evenly spread wait), what is the
probability of the outcomes the manager cares about?

## Recognizing the situation

| Situation | Distribution | Parameters | Excel |
|---|---|---|---|
| A probability table of outcomes and payoffs | Expected value | outcomes and probabilities | `SUMPRODUCT(x, p)`; sd = `SQRT(SUMPRODUCT((x-EV)^2, p))` |
| Fixed n trials, each yes or no with the same p | **Binomial** | n, p | `BINOM.DIST(k, n, p, FALSE)` exact; `TRUE` for "k or fewer" |
| Counts of events in a fixed window, no upper limit | **Poisson** | mean rate (lambda) | `POISSON.DIST(k, lambda, FALSE)` exact; `TRUE` for cumulative |
| A bell-shaped measurement | **Normal** | mean, sd | `NORM.DIST(x, mean, sd, TRUE)` for "less than"; `NORM.INV(p, mean, sd)` for a percentile |
| Every value between a and b equally likely | **Uniform** | a, b | P(under c) = (c minus a)/(b minus a); mean = (a+b)/2 |

State the distribution and its parameters before computing anything. That sentence is the
assumption the manager needs to see.

## Turning a cumulative function around

- "more than k": `1 - BINOM.DIST(k, n, p, TRUE)` or `1 - POISSON.DIST(k, lambda, TRUE)`
- "k or more": `1 - BINOM.DIST(k-1, ...)`; watch the off-by-one.
- "between a and b" for the normal: `NORM.DIST(b,...) - NORM.DIST(a,...)`
- Percentile: `NORM.INV(.90, mean, sd)` is the value 90% of days fall below.

## Standard deviations

Binomial: `SQRT(n*p*(1-p))`. Poisson: `SQRT(lambda)`. These are the spread the staffing plan
should absorb, and they are what a manager means by "how bad can a busy hour get."

## From probability to a staffing or budget call

Compute the probability of exceeding capacity, then decide whether that risk is acceptable. "There
is a .19 chance of more than 15 walk-ins in an hour" becomes "staff for 15 and accept a queue one
hour in five" or "staff for 17 so the queue forms one hour in twenty." The number does not decide;
it prices the choice.

## Reporting

Probabilities two decimals, no leading zero. Means and sds two decimals. Percentiles in the unit of
the data (skiers, dollars), whole numbers when the data are counts.

## Classic mistakes

- Using the binomial when there is no fixed n (arrivals are Poisson).
- `TRUE` versus `FALSE` in BINOM.DIST and POISSON.DIST.
- "More than 15" computed as `1 - POISSON.DIST(16, ...)`.
- Applying the normal to something that cannot be negative and is heavily skewed. Say what you
  assumed and what would break it.
