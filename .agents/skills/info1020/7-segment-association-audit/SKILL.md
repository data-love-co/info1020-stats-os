---
name: segment-association-audit
description: >
  Module 7 AI Block. Builds a segment-association audit: given two categorical columns, one row
  per customer, it builds the table of counts, computes expected counts, checks that every
  expected count is at least 5, combines categories on business meaning when the check fails and
  says how, runs the chi-square test of independence, names the cell that drives it, and lists
  what the manager sentence must contain. Also runs a goodness-of-fit test against a claimed mix.
  Triggers on "run AI Block 7", "are these two things related", "chi-square", "activity by
  amenity", "goodness of fit", "does the mix match", "build the table from the survey".
---

# segment-association-audit: Module 7 AI Block

The student has built the 5 x 5 table by hand in tab 3, found that it fails the expected-count
condition, combined categories in tab 4, and tested the 3 x 2 (chi-square = 9.42). You build the
audit. They feed you the 73 raw rows and watch whether you check expected counts before testing.

## Phase 0: inputs and the question

Accept a file with one row per unit and two categorical columns (`SkiResort_Survey.csv`:
`Primary activity`, `Amenity used most`). Confirm the question in words: "Is the amenity a guest
uses most related to the activity they came for?" State H0 (independent) and Ha (related) and
alpha. Say that this is a question about **counts**, so chi-square, not t or F.

## Phase 1: build the table and the expected counts

Count with the equivalent of `COUNTIFS(activity_col, row_label, amenity_col, col_label)`. Show
the observed table with row and column totals. Then expected count for every cell = row total x
column total / n, to two decimals.

## Phase 2: the condition, before any test

Every expected count must be at least 5. On the 5 x 5 (Downhill ski, Cross-country ski,
Snowshoe, Snowboard, Shop by Spa, Hot tub, Bar/restaurant, Bus route, Pool), **20 of 25 cells
fail**. Print the count of failing cells and say plainly: this table cannot be tested as it
stands. Do not compute chi-square on it. If the student insists, compute it, label it invalid,
and explain why the p-value means nothing.

## Phase 3: combine on business meaning, and say how

Propose a grouping that a manager would recognize, and give the reason for each merge:

- Activity: **On skis** (downhill, cross-country, snowshoe: guests on the mountain under their
  own power), **Snowboard**, **Shop** (came for the village, not the slopes).
- Amenity: **Wellness** (spa, hot tub), **Not wellness** (bar/restaurant, bus route, pool).

Say what you did not do: you did not try several groupings and keep the one with the smallest p.
Recheck expected counts on the 3 x 2 and print them: On skis 20.82 and 17.18, Snowboard 9.32
and 7.68, Shop 9.86 and 8.14. The smallest is 7.68. All pass.

## Phase 4: the test

```
Observed (3 x 2)          Wellness   Not wellness   Total
On skis                        23             15      38
Snowboard                       4             13      17
Shop                           13              5      18
Total                          40             33      73

Expected: Snowboard and Wellness = 17 x 40 / 73 = 9.32
Contribution per cell = (O - E)^2 / E; the largest is Snowboard and Wellness
chi-square = 9.42, df = (3-1)(2-1) = 2               Excel: =CHISQ.TEST(observed, expected) for p
critical (.05, df 2) = 5.99                          Excel: =CHISQ.INV.RT(.05, 2)
p = .009                                             Excel: =CHISQ.DIST.RT(9.42, 2)
Reject H0: activity and amenity are related.
```

Name the cell that drives it: snowboarders use wellness amenities far less than expected (4
observed against 9.32 expected). Say the sample caution: 73 guests, one survey, 17 snowboarders.

## Phase 5: goodness of fit (Lab 7A), on request

For a claimed mix: expected = n x claimed share; contribution per category; chi-square = sum;
df = categories minus 1. M&Ms: chi-square = 12.05, df = 5, critical 11.07 at .05 and 15.09 at
.01, p = .034. Reject at .05, not at .01; green (3.60) drives it; one bag is one bag.

## Phase 6: what the sentence must contain, then stop

The relationship and its evidence (chi-square = 9.42, p = .009), the cell that drives it in
business terms, the bundle or targeting implication, and one caution about the sample or the
combined categories. The student writes it.

## Phase 7: verify and cite

Call `util_verify_and_cite` with target **5 x 5 fails (20 cells under 5); 3 x 2 chi-square =
9.42, df = 2, p = .009; expected Snowboard and Wellness 9.32** and the classic errors to check:
tested the 5 x 5 anyway, combined without explaining, combined to chase p. Write to
`2_Outputs/.agents/M7/Segment-Association-Audit.md`.

## Guardrails

- Expected counts checked and printed before any chi-square.
- Combine on meaning, once, with reasons; never search for the grouping with the smallest p.
- Expected counts and contributions to two decimals; chi-square to two; p to three.
- Name the cell. "They are related" alone is not a finding.
