# M7: Chi-square, goodness of fit and independence

**The question:** t and F compare means. Chi-square compares **counts**. Does an observed mix
match a claimed mix (goodness of fit)? Are two categorical variables related (independence)?

## Telling the question apart

If the data are a measurement per row (dollars, minutes, scores), the question is about means: t
or F. If the data are a category per row (color, activity, amenity), the question is about counts:
chi-square.

## Goodness of fit

- Expected count for each category = n times the claimed share. M&Ms: 200 times .24 = 48.00 blue.
- Contribution per cell = (observed minus expected)^2 / expected. Blue: (38 minus 48)^2 / 48 = 2.08.
- Chi-square = sum of the contributions = **12.05**, df = categories minus 1 = 5.
- Critical: `CHISQ.INV.RT(.05, 5)` = 11.07; at .01, 15.09. p-value: `CHISQ.DIST.RT(12.05, 5)` =
  .034, or `CHISQ.TEST(observed, expected)` directly.
- Reject at .05, not at .01. A moderate result is a finding: say which cell drives it (green,
  3.60) and that one bag is one bag.

## Independence

1. Build the table of counts from raw rows with `COUNTIFS(col1, rowlabel, col2, collabel)`.
2. Expected count for each cell = row total times column total / n.
3. **Check the condition: every expected count at least 5.** The 5 x 5 ski-resort table fails
   (20 of 25 cells under 5). Do not test it.
4. Combine categories **on business meaning**, not to chase significance, and say how. Downhill,
   cross-country, and snowshoe become "on skis"; spa and hot tub become "wellness."
5. Recheck expected counts on the combined table, then compute chi-square cell by cell.
   df = (rows minus 1)(columns minus 1). The 3 x 2: **chi-square = 9.42, df = 2**, critical 5.99,
   p = .009.
6. Say which cell drives the result: snowboarders use wellness amenities far less than expected
   (4 observed against 9.32 expected).

## Reporting

"chi-square(2) = 9.42, p = .009." Expected counts to two decimals, contributions to two decimals,
observed counts whole. Name the grouping used in the same paragraph as the result.

## Classic mistakes

- Testing a table with expected counts under 5.
- Combining categories to get a small p, or combining without explaining.
- Reporting "activity and amenity are related" without saying which cell.
- Treating one bag, one survey, or one weekend as the population.
