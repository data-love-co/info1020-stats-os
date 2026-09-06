# M1: Probability for business decisions

**The question:** given a snapshot of what customers did, how likely is each thing, and does
knowing one thing change the odds of another?

## Vocabulary

- **Marginal probability** P(A): the share of all rows where A is true. `=COUNTIF(range,"Yes")/n`
- **Joint probability** P(A and B): the share where both are true. `=COUNTIFS(r1,"Yes",r2,">100")/n`
- **Union** P(A or B) = P(A) + P(B) minus P(A and B). Subtract the overlap or you count it twice.
- **Conditional probability** P(B given A) = P(A and B) / P(A). The denominator shrinks to the
  rows where A is true. `=COUNTIFS(r1,"Yes",r2,">100")/COUNTIF(r1,"Yes")`
- **Independence:** A and B are independent when P(B given A) = P(B). In practice, compare the
  conditional rate to the overall rate and say whether the gap is big enough to matter for the
  business, not just whether it is exactly zero.
- **Complement** P(not A) = 1 minus P(A).

## The contingency table

Rows are one variable, columns the other, cells are counts (COUNTIFS), margins are totals. Read it
in both directions: P(over $100 given member) uses the member row as denominator; P(member given
over $100) uses the over-$100 column. They are different numbers (.78 and .54 on SummitGear) and
confusing them is the most common error in the module.

## Base rates: the tree of 10,000

When a test or a flag is involved (fraud detection, medical screening, a spam filter), the rate at
which the flag is right depends on how rare the thing is. Build a tree with 10,000 cases:

1. Split by the base rate: 2% fraud = 200 fraudulent, 9,800 legitimate.
2. Split each branch by the detector: 90% of fraud caught = 180 true flags; 5% of legitimate
   flagged = 490 false flags.
3. P(fraud given flagged) = 180 / (180 + 490) = .27.

A flagged order is legitimate almost three times out of four. The manager sentence is about what
to do with a flag (review, not cancel), not about whether the detector is "good."

## Reporting

Two decimals, no leading zero: P(member) = .34. Always name the base: ".78 of Rewards members
spend over $100," never ".78" alone. Counts stay whole numbers.

## Classic mistakes

- Dividing by n when the question is conditional (the denominator is the condition's count).
- Adding P(A) and P(B) for "or" without subtracting the overlap.
- Reading "P(fraud given flag)" as "P(flag given fraud)". The detector's catch rate is the
  second; the business question is the first.
- Calling two events independent because the rates differ by a hair. Say how big the gap is.
