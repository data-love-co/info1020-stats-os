# INFO 1020 Midterm Review Jeopardy, Fall 2026

## Run-of-show and answer key

**Game:** `docs/midterm-review/index.html` (GitHub Pages:
`https://data-love-co.github.io/info1020-stats-os/midterm-review/`)
**Scope:** Modules 1 to 3. Probability, distributions, sampling and confidence intervals.
**Datasets students should have open:** their Lab 1A, 2A, and 3B workbooks, or the CSVs in
`4_Library/sample-data/` (SummitGear_Data.csv, GreenValleyCommons_Residents.csv).
**Daily Double:** The Manager Sentence, $500.

> Fill in: review date, midterm date, class length, team size, prize. The timing below assumes
> the Spring 2026 block (110 minutes, 25 questions). Scale it to the Fall class period.

### Run-of-show

| Time | Segment |
|---|---|
| 0:00 to 0:05 | Welcome, intro slide, prize reveal |
| 0:05 to 0:10 | Form six teams (five students each with a roster of 30). Teams are pre-named in the game: Bayes Watch, Margin of Terror, Significant Others, The Outliers, Mode Squad, Standard Errors. Each team opens the game URL on one laptop and their lab workbooks on another |
| 0:10 to 0:15 | Walk through the rules and the Daily Double mechanic |
| 0:15 to 1:35 | Gameplay. About 80 minutes for 25 questions, 3 to 4 minutes each |
| 1:35 to 1:45 | Final scores, prize, photos |
| 1:45 to 1:50 | Closing reminders for the midterm |

**Keeping pace**

- 60-second timer on $100 to $300. Two minutes on $400 and $500. The Excel cells (Pick the
  Distribution $400 and $500, Mind the Margin $200 to $500) take the full two minutes.
- Wrong answer: open it to the next team in rotation. Do not dwell.
- Correct adds the value, wrong subtracts it. The panel's +/− buttons do this.
- Daily Double: only the team that picked the cell answers. They wager up to their current score,
  or up to $500 if their score is under $500. After the answer, click **Award wager** or **Deduct
  wager**.
- Reveal the answer with **R** or the button. Read the "Check it in Excel" line aloud: the point
  of the game is that every number is checkable in their own workbook.

**Rounding is graded, even here.** If a team says "zero point three four," stop and ask for it the
course way: ".34". If they give a p-value style number with a leading zero, same. Money to the
cent, critical values to three decimals, counts as whole numbers.

---

## Answer key

Ordered by category, lowest to highest value. The game presents cells in whatever order teams pick
them. Use this to score in real time.

### 1. Know Your Rules

Formulas and vocabulary. Quick recall across all three modules.

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | Confidence interval for a mean, population sd unknown: which critical value, and how many degrees of freedom? | **t**, df = n minus 1. z is for a known population sd (almost never) and for proportions. Excel: `T.INV.2T(.05, n-1)`; `CONFIDENCE.T(.05, sd, n)` for the margin of error. | Accept "t" or "t-star". Full credit needs df = n minus 1. |
| 200 | Formula for P(B given A), and what happens to the denominator. | **P(A and B) / P(A).** The denominator shrinks to the rows where A is true. Excel: `COUNTIFS(...) / COUNTIF(...)`. | Half credit for the formula without the denominator sentence. "Divide by n" is the Module 1 classic error. |
| 300 | The rule for P(A or B), and why the last term is there. | **P(A) + P(B) minus P(A and B).** The overlap is in both terms; subtract it once so it is counted once. | Full credit needs both. |
| 400 | Standard error of a sample mean: formula, what it measures, and what happens when n goes from 40 to 160. | **SE = sd / SQRT(n).** The spread of the sampling distribution (how far sample means wander), not the spread of the data. Four times n halves the SE. Excel: `STDEV.S(range)/SQRT(n)`. | Full credit needs all three parts. "The spread of the data" is wrong. |
| 500 | Full confidence-interval formula for a mean with sd unknown; name every symbol including df; name the one-call Excel function for the margin of error. | **x̄ ± t* · (s / √n).** x̄ sample mean; t* from the t distribution with df = n minus 1; s sample sd; n sample size. `CONFIDENCE.T(alpha, s, n)`. | The df detail is required. Half credit for the formula without df or without the Excel function. |

### 2. Read the Table

Module 1. SummitGear Outfitters, 250 orders. The table shown on the $200 to $400 cells:

|  | Over $100 | $100 or less | Total |
|---|---|---|---|
| Rewards member | 66 | 19 | 85 |
| Not a member | 56 | 109 | 165 |
| Total | 122 | 128 | 250 |

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | P(Rewards member), rounded the course way. | **.34** (85 / 250). Excel: `COUNTIF(range,"Yes")/250`. | ".34", not "0.34" and not "34%". Warm-up. |
| 200 | P(member and over $100), and P(member or over $100). | **.26** (66 / 250 = .264) and **.56** ((85 + 122 minus 66) / 250 = .564). Excel: `COUNTIFS`. | No credit for .83 (added without subtracting the overlap). |
| 300 | P(over $100 given member) and P(member given over $100). Why different? | **.78** (66 / 85) and **.54** (66 / 122). Same numerator, different denominator: the member row versus the over-$100 column. | Full credit needs both numbers and the denominator explanation. The most common Module 1 error. |
| 400 | Is spending over $100 independent of membership? Show the comparison and the marketing meaning. | **No.** .78 given member versus .49 overall; independent would mean they match. Members are the better target. Caution: association, not cause. | Half credit for "not independent" without the two rates side by side. Bonus praise for the causation caution. |
| 500 | Fraud detector: 2% fraud, 90% caught, 5% of legitimate flagged. Tree of 10,000 and P(fraud given flagged). | 200 fraud / 9,800 legitimate. **180 true flags, 490 false flags, 670 flags.** 180 / 670 = .2687, so **.27**. | Full credit needs the counts and .27. The teaching moment: 90% is P(flag given fraud), not P(fraud given flag). A team that answers ".90" or "about 90%" has made the Lab 1B error; say so to the room. |

### 3. Pick the Distribution

Module 2. University of Highlands Ranch registration, Mt. Highlands Ranch resort.

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | 12.5 walk-ins per hour on average, no upper limit. Distribution, parameter, standard deviation. | **Poisson**, lambda = 12.5. sd = SQRT(12.5) = **3.54**. Excel: `POISSON.DIST(k, 12.5, FALSE)`. | Full credit needs all three. "Binomial" is the Module 2 classic error: there is no n. |
| 200 | 15 admits, each enrolls with probability .80, independently. Distribution, two conditions, expected number. | **Binomial**, n = 15, p = .80. Conditions: fixed n, yes/no trials, constant p, independence. EV = **12.00**; sd = **1.55**. Excel: `BINOM.DIST(12,15,.8,FALSE)` = .25; `1-BINOM.DIST(11,15,.8,TRUE)` = .65. | Full credit: binomial plus two conditions plus 12. |
| 300 | Lift stops 2 to 10 minutes, every length equally likely. Distribution, P(under 5), mean. | **Uniform** (continuous). P(under 5) = 3 / 8 = .375, reported **.38**. Mean = **6.00** minutes. P(over 4) = .75. | Accept .375 said aloud if they then round to .38. |
| 400 | Excel: P(more than 15 walk-ins). Function and value. What did `=1-POISSON.DIST(16,12.5,TRUE)` compute? | **`=1-POISSON.DIST(15,12.5,TRUE)` = .19** (unrounded .1940). The teammate computed P(more than 16) = .13. For the record: P(exactly 8) = .06, P(15 or fewer) = .81. | Full credit needs .19 and the diagnosis of the off-by-one. Half credit for .19 alone. |
| 500 | Skier counts: 229 days, mean 747.39, sd 159.63, bell shaped. Distribution and why; P(more than 800); 90th percentile. | **Normal.** A bell-shaped measurement on both sides of the mean. P(more than 800) = `1-NORM.DIST(800,747.39,159.63,TRUE)` = **.37**. 90th percentile = `NORM.INV(.9,747.39,159.63)` = **952 skiers**. | Full credit needs the name, the reason, and both numbers. Percentile as a whole number (counts). |

### 4. Mind the Margin

Module 3. SummitGear as a population (Lab 3A), Green Valley Commons (Lab 3B).

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | SummitGear population mean $100.14, sd $36.99. SE for samples of 40, and what it describes. | **$36.99 / SQRT(40) = $5.85.** How far the mean of 40 orders typically lands from the true mean; the sampling distribution's spread, not the orders' spread. CLT: n = 40 makes it close to normal; P(sample mean over $110) = .05. | Full credit needs $5.85 and "spread of the sample mean" (not the data). |
| 200 | Angela surveys the 20 residents who show up to Tuesday's meeting. Name the problem and recommend a fix. | **Convenience sample, voluntary-response bias.** Attendees differ from non-attendees. Fix: a simple random sample from the resident list, or stratified by building. | Half credit for naming the bias without a concrete fix. Any defensible random design from the full population earns full credit. |
| 300 | 20 incomes, mean $3,398.90, sd $351.38. SE and t* for 95%. Excel function for each. | **SE = $78.57** (unrounded 78.5717), `STDEV.S(range)/SQRT(20)`. **t* = 2.093**, `T.INV.2T(.05, 19)`. | df = 19. t* to three decimals. |
| 400 | The 95% interval. Margin of error, both endpoints, course rounding for money. One-call Excel function. | **Margin $164.45. $3,234.45 to $3,563.35.** `CONFIDENCE.T(.05, 351.38, 20)`. Multiply with the unrounded SE. 90% interval for the record: $3,263.04 to $3,534.76 (t* = 1.729). | Endpoints to the cent. Bounds within one cent earn full credit. |
| 500 | (1) 8 of 20 are men: can you report the 95% interval for the share? Check the condition. (2) n for a $100 margin on income at 95%. | **(1) Not reportable.** n p-hat = 8 and n(1 minus p-hat) = 12; both must be at least 10. "Not yet: survey more." **(2) (1.96 × 351.38 / 100)² = 47.4, round up to 48.** | Full credit needs the condition stated with its numbers and 48 (not 47). Reporting the proportion interval anyway is a graded error. |

### 5. The Manager Sentence

Interpretation, the classic errors, and the decision sentence. The $500 is the Daily Double.

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | 95% interval $3,234.45 to $3,563.35 from 20 residents. The one correct interpretation sentence. | "We are 95% confident that the true mean monthly income of Green Valley Commons residents is between $3,234.45 and $3,563.35, based on a sample of 20." Confidence is in the method: 95 of 100 such intervals capture the true mean. | Accept any wording that puts the confidence on the procedure and names the parameter, n, and the level. |
| 200 | Why is "95% of residents earn between..." wrong, and why is "there is a 95% probability the mean is in this range" wrong? | **First:** the interval is about the mean, not individuals; individuals vary by sd $351.38, the mean by SE $78.57. **Second:** the mean is fixed, not random; the 95% belongs to the procedure. | Full credit needs both. Catching the first sentence is a graded Module 3 skill. |
| 300 | P(fraud given flagged) = .27. Manager wants to auto-cancel flagged orders. Decision verb, evidence in business units, what it does not mean. | **Review, do not cancel.** Of 670 flags, about 490 are legitimate and 180 fraud: nearly three good customers turned away per fraud stopped. Does not mean the detector is bad (90% catch rate), does not mean every flag is legitimate. | Half credit for the right decision without the counts. Reject any sentence that leads with ".27" and no business units. |
| 400 | P(more than 15) = .19, P(more than 17) = .08, P(more than 20) = .02. Fill the Module 2 skeleton and defend the staffing level. | Any level with its risk priced: "Plan for 15; .19 chance of exceeding, so expect a queue one hour in five." Or "Plan for 17; .08 chance, so open one more desk." The number prices the choice; it does not make it. | No credit for a level with no probability, or a probability with no action. |
| 500 DD | Three-sentence So What / Now What memo to the Green Valley board: estimate with uncertainty, business takeaway, next step with a number. | Rubric: (a) point estimate and interval with n and level; (b) a takeaway a board member can act on, in business language; (c) survey 48 residents for a $100 margin and hold the proportion results until then. Model answer in the game. | Only the picking team answers, for their wager. Half credit for two of three. Reject formula-heavy memos and the "probability the mean is" sentence. Read the model aloud after revealing. |

---

## Wrap-up: the five minutes after the game

Most-missed concepts to name for the room, in the order they usually come up:

1. **P(fraud given flag) is not the catch rate.** The 90% is the other direction.
2. **Off by one in the cumulative functions.** "More than 15" is 1 minus P(15 or fewer).
3. **"95% of residents earn between."** The interval is about the mean.
4. **The proportion condition.** 8 and 12 is not 10 and 10. Not reportable is a real answer.
5. **Rounding.** .34 not 0.34, money to the cent, t* to three decimals, round n up.

Confirm the midterm format (date, length, open-note policy, calculator, no AI tools of any kind,
which is the course rule and the Honor Code). Point students at the module workbooks, the notes
guides, and the method sheets in `4_Library/method/` as the formula reference. Students can replay
the game on the Pages URL for solo practice.

**Questions to expect**

- "Will the midterm be this hard?" About this difficulty, with more multi-step items.
- "Are these the exact questions?" No. The concepts and the datasets are the same ones in your
  workbooks.
- "Can we use the AI Block tools on the midterm?" No. Never on quizzes or exams.
