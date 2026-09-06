# Course datasets and what they should produce

Every dataset used in an INFO 1020 lab, as CSV, with the key values the solution workbook gets
from it. These are the **verification targets** for the AI Blocks: run the course data through
whatever the agent built and compare. All values follow the course rounding policy.

| File | Module | Rows | Columns |
|---|---|---|---|
| `SummitGear_Data.csv` | M1, M3 | 250 orders | Customer, Age, Gender, Channel, Rewards Member, Number of Items, Order Total ($), Items Returned, Orders This Month |
| `MtHighlands_SkierCounts.csv` | M2 | 229 days | Skiers per day |
| `MtHighlands_LiftStops.csv` | M2 | 170 stops | Stop length (min) |
| `GreenValleyCommons_Residents.csv` | M3 | 20 residents | Resident, Miles to their doctor, Age, Monthly income ($), Male |
| `DeniceToney_Balances.csv` | M4 | 16 accounts | Customer, Account balance ($) |
| `GreenValleyCommons_Residents48.csv` | M4 | 48 residents | same columns as the 20-resident file |
| `Streamly_ABTest_CX.csv` | M5 | 80 customers | Customer, Variant, CX score (1 to 10) |
| `Multitasking_Example14.csv` | M5 | 14 students | Student, Round 1 single task (sec), Round 2 switching (sec) |
| `CareerServices_Salaries.csv` | M6 | 20 per path | Graduate, OR Analyst, Accountant, Computer Analyst, Financial Specialist |
| `Clinic_WaitTimes.csv` | M6 | 20 per state | Sampled day, Florida, New York, North Carolina |
| `SkiResort_Survey.csv` | M7 | 73 guests | Guest, Primary activity, Amenity used most |

Run `python 0_System/scripts/check-values.py` to recompute every target below from the CSVs and
confirm nothing has drifted.

## Module 1: SummitGear (probability)

Excel: COUNTIF and COUNTIFS over 250 rows.

| Quantity | Value |
|---|---|
| P(Rewards member) | .34 |
| P(order over $100) | .49 |
| P(female) | .52 |
| P(online) | .66 |
| P(age 60 or over) | .08 |
| P(member AND over $100) | .26 |
| P(member OR over $100) | .56 |
| P(over $100 given member) | .78 |
| P(member given over $100) | .54 |
| P(over $100 given female) | .45 |
| P(over $100 given male) | .53 |
| P(at least one item returned) | .14 |
| Mean order total | $100.14 |

**Fraud-flag base rate** (tab 4, not from the CSV): 2% of orders are fraudulent, the system
catches 90% of fraud, and flags 5% of legitimate orders. Tree of 10,000: 180 true flags, 490
false flags, 670 flags in all. **P(fraud given flagged) = .27.**

## Module 2: Highlands Ranch (distributions)

Registration values are from the workbook's given parameters, not from a CSV.

| Quantity | Excel | Value |
|---|---|---|
| Binomial, n = 15, p = .80: P(exactly 12) | BINOM.DIST(12,15,.8,FALSE) | .25 |
| P(12 or more) | 1 - BINOM.DIST(11,15,.8,TRUE) | .65 |
| Binomial sd | SQRT(15*.8*.2) | 1.55 |
| Poisson, mean 12.5 per hour: P(exactly 8) | POISSON.DIST(8,12.5,FALSE) | .06 |
| P(15 or fewer) | POISSON.DIST(15,12.5,TRUE) | .81 |
| **P(more than 15)** | 1 - POISSON.DIST(15,12.5,TRUE) | **.19** |
| Poisson sd | SQRT(12.5) | 3.54 |

Ski resort values from `MtHighlands_SkierCounts.csv` (mean 747.39, sd 159.63) and
`MtHighlands_LiftStops.csv` (uniform between the shortest stop, 2 minutes, and the longest, 10):

| Quantity | Excel | Value |
|---|---|---|
| P(more than 800 skiers) | 1 - NORM.DIST(800,747.39,159.63,TRUE) | .37 |
| P(450 to 770 skiers) | NORM.DIST(770,...) - NORM.DIST(450,...) | .53 |
| 90th percentile of skiers | NORM.INV(.9,747.39,159.63) | 952 |
| 25th percentile | NORM.INV(.25,...) | 640 |
| P(stop under 5 minutes), uniform 2 to 10 | (5-2)/(10-2) | .38 |
| P(stop over 4 minutes) | (10-4)/(10-2) | .75 |
| Mean stop length | (2+10)/2 | 6.00 |

## Module 3: sampling and confidence intervals

SummitGear as a population: mean $100.14, sd $36.99. Standard error for n = 40: $5.85.
P(sample mean over $110) = .05.

Green Valley Commons, 20 residents, monthly income:

| Quantity | Excel | Value |
|---|---|---|
| Mean | AVERAGE | $3,398.90 |
| Standard deviation | STDEV.S | $351.38 |
| Standard error | sd/SQRT(20) | $78.57 |
| t* for 95%, df = 19 | T.INV.2T(.05,19) | 2.093 |
| Margin of error | CONFIDENCE.T(.05,351.38,20) | $164.45 |
| **95% interval for mean income** | | **$3,234.45 to $3,563.35** |
| 90% interval | | $3,263.04 to $3,534.76 |
| Share within 5 miles of a doctor | COUNTIF/20 | .50 |
| Share male | 8 of 20 | .40 |
| Sample size for a $100 margin at 95% | (1.96*351.38/100)^2, rounded up | 48 |
| Sample size for a $150 margin | | 22 |

The proportion intervals **fail the condition** (np and n(1 minus p) must both be at least 10;
with n = 20 they are 10 and 10 for the miles question and 8 and 12 for gender). The workbook
teaches that the honest answer is "not yet reportable, survey 48."

## Module 4: one-sample tests

Denice Toney, 16 account balances:

| Quantity | Excel | Value |
|---|---|---|
| Mean | AVERAGE | $2,650.68 |
| sd | STDEV.S | $317.11 |
| Standard error | sd/SQRT(16) | $79.28 |
| Right-tailed test against $2,500: t | (2650.68 - 2500)/79.28 | **1.90** |
| p-value, right tail, df = 15 | T.DIST.RT(1.90,15) | **.038** |
| Critical t at .05, right tail | T.INV(.95,15) | 1.753 |
| Two-tailed test against $2,800: t | | -1.88 |
| p-value, two tails | T.DIST.2T(1.88,15) | .079 |
| 95% interval for the mean | | $2,481.70 to $2,819.66 |

Green Valley Commons, 48 residents, share over 5 miles from a doctor: 23 of 48, p-hat = .48,
test against .40, z = 1.12, p = .131 right-tailed, z* = 1.645. Fail to reject.

## Module 5: two-sample tests

Streamly A/B test, 40 per variant, CX score:

| Quantity | Excel | Value |
|---|---|---|
| Mean A (current) | | 7.44 |
| Mean B (new) | | 8.24 |
| sd A, sd B | | 1.60, 1.21 |
| Difference B minus A | | .80 |
| Standard error of the difference (Welch) | SQRT(sA^2/40 + sB^2/40) | .317 |
| **t** | | **2.53** |
| df (conservative, smaller n minus 1) | | 39 |
| **p, two-tailed, conservative df** | T.DIST.2T(2.53,39) | **.016** |
| p, Welch df, via T.TEST(...,2,3) | | .014 |
| t* for 95%, df = 39 | T.INV.2T(.05,39) | 2.023 |
| 95% interval for the difference | | .16 to 1.44 |

Multitasking, 14 students, paired: mean difference 28.14 seconds, sd of differences 8.41,
standard error 2.25, **t = 12.52, p < .001**. Fed to a tool as two unlabeled columns, an
independent test is the wrong answer; the skill must notice the pairing.

## Module 6: ANOVA

Career Services salaries, 4 paths, 20 each:

| Quantity | Value |
|---|---|
| Group means | OR Analyst $81,375.21; Computer Analyst $79,496.78; Accountant $71,370.22; Financial Specialist $66,865.57 |
| Grand mean | $75,716.16 |
| Largest sd / smallest sd | 2.19 (report it; the course treats it as borderline and proceeds) |
| SSB, SSW | 3721172720, 1232181262 |
| df between, within | 3, 76 |
| MSB, MSW | 1240390907, 16212911 |
| **F** | **76.51** |
| F* at .05 | 2.72 |
| p | < .001 |
| Tukey HSD (q = 3.7149 for k = 4, df = 76) | $3,344.70 |
| Pairs that differ | all except OR Analyst vs Computer Analyst (difference $1,878.43) |
| Family-wise error of six t-tests at .05 | .26 (1 minus .95^6) |

Atlas clinics, 3 states, 20 days each: **F = .71**, F* = 3.16, p = .494. Fail to reject. No Tukey.
Group means Florida 14.50, New York 15.25, North Carolina 13.95 minutes; grand mean 14.57.

## Module 7: chi-square

M&M goodness of fit (tab 2, given counts, not a CSV): 200 pieces, observed Blue 38, Green 52,
Orange 40, Yellow 22, Red 18, Brown 30 against the claimed mix .24, .20, .16, .14, .13, .13.
Expected Blue 48.00, Green 40.00. Contributions Blue 2.08, Green 3.60.
**Chi-square = 12.05, df = 5, p = .034**; critical 11.07 at .05 and 15.09 at .01.

Ski resort survey, 73 guests, `SkiResort_Survey.csv`:

| Quantity | Value |
|---|---|
| Full 5 x 5 table | 20 of 25 cells have expected counts under 5: **cannot test** |
| Grouping used | Activity: On skis (downhill, cross-country, snowshoe), Snowboard, Shop. Amenity: Wellness (spa, hot tub), Not wellness (bar/restaurant, bus route, pool) |
| 3 x 2 observed | Skis 23 / 15; Snowboard 4 / 13; Shop 13 / 5 |
| Snowboarders | 17 (.23 of guests) |
| Expected, Snowboard and Wellness | 9.32 |
| **Chi-square on the 3 x 2** | **9.42**, df = 2 |
| Critical at .05 | 5.99 |
| p | .009 |
| The cell that drives it | Snowboarders use wellness amenities far less than expected |
