# Rounding policy (graded)

Rounding is part of statistics, and accurate rounding is required in INFO 1020. Every number an
agent reports to a student must already follow this policy, because the student will paste it into
a graded workbook. Show the unrounded value once, in a method note, then the rounded value. Never
round an intermediate result and then compute from the rounded value.

| Rule | Example |
|---|---|
| Round with statistical precision: round up when the next digit is 5 or greater. | 4.678 becomes 4.68 |
| Use a leading zero when the value can exceed 1.0. Do not use one when it cannot. | M = 0.89, but r = .98 and p = .004 |
| Probabilities, proportions, correlations, and test statistics: two decimals. Correlation is not a percentage. | P(member) = .34, t = 3.45, F = 76.51 |
| p-values: three decimals, no leading zero. | p = .023 |
| p-values below .001 are reported as an inequality. Never as 0 or .000. | p < .001 |
| Money: to the cent. | $100.14 |
| Critical values from tables: three decimals. | t* = 2.093, z* = 1.645 |
| Sums of squares and mean squares: whole numbers when the data are dollars, two decimals otherwise. They are intermediate steps. | SSB = 3721172720; MSW = 11.92 |
| Expected counts in a chi-square table: two decimals. | 9.32 |
| Degrees of freedom and counts: whole numbers. | df = 39, n = 250 |

Excel does this for the student through cell formatting (a custom format of `.00` drops the
leading zero). When you report a number, match what their formatted cell shows.
