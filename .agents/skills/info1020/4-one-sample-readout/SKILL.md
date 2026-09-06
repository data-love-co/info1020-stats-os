---
name: one-sample-readout
description: >
  Module 4 AI Block. Builds a hypothesis-test readout generator for one sample: given a column of
  numbers (or n, mean, sd), a claimed value, the tail, and alpha, it returns all seven steps in
  business language, the p-value, the critical value, the confidence interval, and what the result
  does not prove. Also handles a one-sample proportion (z). Triggers on "run AI Block 4", "test a
  claim", "is the mean above", "one sample", "seven steps", "p-value for this", "proportion test".
---

# one-sample-readout: Module 4 AI Block

The student has run Denice Toney's test by hand in tab 1 (t = 1.90, p = .038, reject) and the
two-tailed version in tab 2 (t = -1.88, p = .079, fail to reject). You build the readout
generator. They check you against those tabs, and they check whether you picked the tail
honestly.

## Phase 0: inputs, and the tail before the data

Ask for, in this order, and do not look at the data until item 3 is answered:

1. **The parameter in words.** "The true mean balance of mid-tier accounts at Summit Ridge Bank."
2. **The claimed value.** $2,500.
3. **The tail, from the business question.** Denice funds the promotion only if the mean is
   *above* $2,500: right-tailed. "Is it different from $2,800": two-tailed. If the student cannot
   say, ask what decision hangs on the answer; the decision picks the tail. Record the tail
   before opening the file.
4. **Alpha.** Default .05; say so.
5. **The data.** `DeniceToney_Balances.csv`, column `Account balance ($)`, or n, mean, sd.

For a proportion (Lab 4B: 23 of 48 residents over 5 miles, claim .40, right-tailed): the same
order, then check n p0 and n (1 minus p0) at least 10 before using z.

## Phase 1: the seven steps, computed for real

Show each step with its number and its Excel equivalent:

```
1. Parameter: mu = true mean balance of mid-tier accounts
2. H0: mu = 2500
3. Ha: mu > 2500 (right-tailed, chosen from the business question before the data)
4. Statistic: t = (x-bar - 2500) / (s / SQRT(n)), df = 15
   n = 16   x-bar = 2650.68   s = 317.11   SE = 79.28        Excel: AVERAGE, STDEV.S, /SQRT(16)
5. Rejection region: alpha = .05, right tail, t* = 1.753        Excel: =T.INV(.95, 15)
   [picture: a t curve with the right 5% shaded, 1.753 marked]
6. Compute: t = 1.90, p = .038                                  Excel: =T.DIST.RT(1.90, 15)
7. Decide: p = .038 < .05, reject H0.
```

Then the two-tailed version against $2,800: t = -1.88, p = .079 (`=T.DIST.2T(1.88, 15)`), fail to
reject. Point out that the two-tailed p is double the one-tailed p for the same t, and why.

Add the 95% interval ($2,481.70 to $2,819.66) and say what it shows: $2,500 is inside it, which
looks like a contradiction until the student notices the interval is two-sided and the test was
one-sided. That is a graded concept; explain it in two sentences.

## Phase 2: what it means and what it does not prove

Write the interpretation in business language, in this shape, and label it as what the manager
sentence must contain rather than the sentence itself:

- The decision on the claim (reject: the evidence supports a mean above $2,500).
- The evidence in dollars (sample mean $2,650.68, 16 accounts, p = .038).
- What it does not prove: not that the mean is $2,650, not that the promotion will work, and not
  "proof" of anything. "The data are inconsistent with a mean of $2,500 at the 5% level."
- The error risk: a Type I error here means funding a promotion the segment cannot support; the
  chance of that, if H0 were true, is 5%.

Never write "accept H0." Never write "proves."

## Phase 3: make it reusable

Offer the generator as a function that takes (data or n, mean, sd), the null value, the tail,
alpha, and returns the seven steps. Run the proportion case through the z version: p-hat = .48,
z = 1.12, p = .131, z* = 1.645, fail to reject; the shuttle decision stays open.

## Phase 4: verify and cite

Call `util_verify_and_cite` with target **t = 1.90, p = .038, t* = 1.753, reject; two-tailed
against $2,800: t = -1.88, p = .079** and the classic errors to check: tail chosen after the data,
one-tailed p reported for a two-tailed question, "accept H0," "proves." Write to
`2_Outputs/.agents/M4/One-Sample-Readout.md`.

## Guardrails

- Tail before data. If the student gives you the data first, set it aside and ask for the tail.
- Statistic, critical value, and p-value together, with the tail named.
- t to two decimals, p to three with no leading zero, critical values to three.
- The interpretation lists what a sentence must contain; the student writes it.
