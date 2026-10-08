# INFO 1020 Midterm Review Jeopardy, Fall 2026

## Run-of-show and answer key

**Game:** https://data-love-co.github.io/info1020-stats-os/midterm-review/
**Scope:** Modules 1 to 3. Probability, distributions, sampling and confidence intervals.
**What each team needs open:** Excel with a **blank workbook**, plus `SummitGear_Data.csv` and
`GreenValleyCommons_Residents48.csv` from `4_Library/sample-data/`. Lab workbooks stay closed.
Every computation in the game is a cut the labs did not make, so the old tabs will not help and
the habit the game builds is applying the method to a new question.
**Daily Double:** The Manager Sentence, $500.
**Tie-break:** Final Jeopardy, the ★ button in the banner. Rules and key below.

> Fill in: review date, midterm date, class length, prize list, extra-credit rule. The timing
> below assumes the Spring 2026 block (110 minutes, 25 questions). Scale it to the Fall period.

### Run-of-show

| Time | Segment |
|---|---|
| 0:00 to 0:05 | Welcome, intro slide, prize reveal, the tie-break rule |
| 0:05 to 0:10 | Form six teams (five students each with a roster of 30). Teams are pre-named in the game: Bayes Watch, Margin of Terror, Significant Others, The Outliers, Mode Squad, Standard Errors. Each team opens the game URL on one laptop and a blank workbook plus the two CSVs on another |
| 0:10 to 0:15 | Walk through the rules and the Daily Double mechanic |
| 0:15 to 1:35 | Gameplay. About 80 minutes for 25 questions, 3 to 4 minutes each |
| 1:35 to 1:45 | Final scores (Final Jeopardy if tied), prizes, photos |
| 1:45 to 1:50 | Closing reminders for the midterm |

**How a question runs: all teams play**

Every team works every question. The picking team chooses the cell; nobody buzzes in. The game
starts a countdown the moment the question appears:

| Cell | Time | With Excel open |
|---|---|---|
| $100 | 45 seconds | 1:45 |
| $200 | 1 minute | 2:00 |
| $300 | 1.5 minutes | 2:30 |
| $400 | 2 minutes | 3:00 |
| $500 | 3 minutes | 4:00 |

The seven Excel cells get the extra minute automatically: Read the Table $400, Pick the
Distribution $400 and $500, Mind the Margin $100 and $300 to $500. **Pause** and **+30s** sit
next to the clock.

- When time is up, every team holds up its written answer at once. Reveal with **R** or the
  button, which stops the clock.
- Click each team that got it right in the row under the answer; each click adds the cell value
  (click again to undo). A wrong answer costs nothing, so every team has a reason to try. For a
  partial-credit call, use the side panel's +/− buttons instead.
- Daily Double is the one exception: only the team that picked the cell answers, for a wager up
  to their current score (or up to $500 if under $500). After the answer, click **Award wager**
  or **Deduct wager**.
- Read the "Check it in Excel" line aloud after each reveal: the point of the game is that every
  number is checkable with one function in a blank sheet.
- Clock budget: the 25 limits add up to 48 minutes with the Excel minutes, which leaves about a
  minute per cell for the reveal and the teaching moment inside the 80-minute gameplay block.

**Tie-break: Final Jeopardy**

Say this rule before the first cell is picked, so no one argues later.

- If two or more teams are tied for first when the board is cleared, click **★ Final Jeopardy**.
  The tied teams are pre-selected; untick anyone else.
- Each playing team writes a wager, up to its score (or up to $500 if its score is below $500),
  before the question is shown. Lock the wagers.
- Show the question. Sixty seconds. Teams write one answer on paper and hold it up together.
- Reveal the answer, then mark each team **Correct** or **Wrong**. The wager is added or
  subtracted and the new score shows in the row.
- Still tied (both right or both wrong with equal wagers): the team with fewer wrong answers
  during the board wins. Keep a tally on paper, or run the spare question below as sudden death.

**Rounding is graded, even here.** If a team says "zero point three one," stop and ask for it the
course way: ".31". Money to the cent, critical values to three decimals, counts and sample sizes
as whole numbers, sample sizes rounded up.

---

## Answer key

Ordered by category, lowest to highest value. The game presents cells in whatever order teams pick
them. Use this to score in real time. Every value below is recomputed from the CSVs by
`check-game-values.py`.

### 1. Know Your Rules

Formulas and vocabulary. Quick recall across all three modules. No computation.

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | Confidence interval for a mean, population sd unknown: which critical value, and how many degrees of freedom? | **t**, df = n minus 1. z is for a known population sd (almost never) and for proportions. Excel: `T.INV.2T(.05, n-1)`; `CONFIDENCE.T(.05, sd, n)` for the margin of error. | Accept "t" or "t-star". Full credit needs df = n minus 1. |
| 200 | Formula for P(B given A), and what happens to the denominator. | **P(A and B) / P(A).** The denominator shrinks to the rows where A is true. Excel: `COUNTIFS(...) / COUNTIF(...)`. | Half credit for the formula without the denominator sentence. "Divide by n" is the Module 1 classic error. |
| 300 | The rule for P(A or B), and why the last term is there. | **P(A) + P(B) minus P(A and B).** The overlap is in both terms; subtract it once so it is counted once. | Full credit needs both. |
| 400 | Standard error of a sample mean: formula, what it measures, and what happens when n goes from 40 to 160. | **SE = sd / SQRT(n).** The spread of the sampling distribution (how far sample means wander), not the spread of the data. Four times n halves the SE. Excel: `STDEV.S(range)/SQRT(n)`. | Full credit needs all three parts. "The spread of the data" is wrong. |
| 500 | Full confidence-interval formula for a mean with sd unknown; name every symbol including df; name the one-call Excel function for the margin of error. | **x̄ ± t* · (s / √n).** x̄ sample mean; t* from the t distribution with df = n minus 1; s sample sd; n sample size. `CONFIDENCE.T(alpha, s, n)`. | The df detail is required. Half credit for the formula without df or without the Excel function. |

### 2. Read the Table

Module 1. SummitGear's 250 orders cut by channel and membership. The lab cut them by membership
and spending; this table is new. Shown on the $100 to $300 cells:

|  | Online | In-store | Total |
|---|---|---|---|
| Rewards member | 51 | 34 | 85 |
| Not a member | 113 | 52 | 165 |
| Total | 164 | 86 | 250 |

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | How many orders were both online and from a member, and the probability, course rounding. | **51 orders, .20** (51 / 250 = .204). Excel: `COUNTIFS`. | ".20", not "0.20". A joint divides by the grand total. |
| 200 | P(member given online), P(member given in-store), compared with P(member) overall; what it tells marketing. | **.31** (51 / 164) and **.40** (34 / 86), against .34 overall. Not independent, but a nine-point gap, far smaller than the lab's membership-by-spending gap. Members are already in the store; the online sign-up pitch is the opportunity. | Full credit needs both conditionals and the comparison with .34. Praise a team that sizes the gap instead of just saying "dependent". |
| 300 | P(online or member). A teammate added .66 and .34 and got 1.00; show from the table why that cannot be right. | **.79** ((164 + 85 minus 51) / 250 = 198 / 250). 1.00 would mean every order was online or from a member; the 52 in-store non-member orders prove otherwise. The 51 overlap orders were counted twice. | Full credit needs .79 and the table-based refutation. |
| 400 | **Excel.** From `SummitGear_Data.csv`: P(returned given in-store) and P(returned given online), where returned means Items Returned is 1 or more. What does the comparison say? | **.22** (19 of 86) and **.10** (17 of 164). In-store orders are returned about twice as often; the overall .14 from the lab hid it. | Full credit needs both numbers and the business reading. The counts 19 and 17 are not in any lab tab. |
| 500 | New detector: 2% fraud, 95% catch rate, 1% false-alarm rate. Tree of 10,000, P(fraud given flagged), and which improvement did most of the work. | 200 fraud, 9,800 legitimate. **190 true flags, 98 false flags, 288 flags.** 190 / 288 = .6597, so **.66**. The false-alarm cut (490 to 98) did almost all of it; the catch rate added 10 true flags. | Full credit needs the counts, .66, and the lever. A team that answers ".95" has given the catch rate; say so to the room. |

### 3. Pick the Distribution

Module 2. Highlands Ranch registration and the ski resort, new numbers throughout.

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | The desk's phone line averages 8 calls per hour, no upper limit. Distribution, parameter, standard deviation. | **Poisson**, lambda = 8. sd = SQRT(8) = **2.83**. Excel: `POISSON.DIST(8, 8, FALSE)` = .14 for exactly 8. | Full credit needs all three. "Binomial" is the Module 2 classic error: there is no n. |
| 200 | 25 acceptance letters, each enrolls with probability .60, independently. Distribution, two conditions, expected number, sd. | **Binomial**, n = 25, p = .60. Conditions: fixed n, yes/no trials, constant p, independence. EV = **15.00**; sd = **2.45**. Excel: `BINOM.DIST(15,25,.6,FALSE)` = .16; `1-BINOM.DIST(17,25,.6,TRUE)` = .15 for 18 or more. | Full credit: binomial plus two conditions plus 15.00 and 2.45. |
| 300 | Gondola stops 3 to 15 minutes, every length equally likely. Distribution, P(under 5), P(over 10), mean. | **Uniform** (continuous). P(under 5) = 2 / 12 = .167, reported **.17**. P(over 10) = 5 / 12 = **.42**. Mean = **9.00** minutes. | Accept the fractions said aloud if they then round the course way. |
| 400 | **Excel.** Drop/add week, 25 walk-ins per hour, capacity 30. P(more than 30)? Function and value. What did `=1-POISSON.DIST(31,25,TRUE)` compute? | **`=1-POISSON.DIST(30,25,TRUE)` = .14** (unrounded .1367). The teammate computed P(more than 31) = .10. For the record: P(more than 35) = .02, sd = 5.00. | Full credit needs .14 and the diagnosis of the off-by-one. Half credit for .14 alone. |
| 500 | **Excel.** Skier counts: mean 747.39, sd 159.63, bell shaped. Distribution and why; P(fewer than 500); 95th percentile. | **Normal.** A bell-shaped measurement on both sides of the mean. P(fewer than 500) = `NORM.DIST(500,747.39,159.63,TRUE)` = **.06**. 95th percentile = `NORM.INV(.95,747.39,159.63)` = **1,010 skiers**. | Full credit needs the name, the reason, and both numbers. Percentile as a whole number (counts). The lab asked for the other tail and the 90th percentile; this is the other side. |

### 4. Mind the Margin

Module 3. SummitGear as a population (Lab 3A) with a new sample size; Angela's follow-up survey of
48 residents, which the labs never opened.

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | **Excel.** SummitGear population mean $100.14, sd $36.99. Samples of 100 (the lab used 40). SE, and P(sample mean over $105). | **$36.99 / SQRT(100) = $3.70** (unrounded 3.6992). P(sample mean over $105) = `1-NORM.DIST(105,100.14,3.70,TRUE)` = **.09**. CLT makes the sampling distribution close to normal at n = 100. | Full credit needs $3.70, .09, and "spread of the sample mean, not the data". |
| 200 | Angela surveys the 20 residents who show up to Tuesday's meeting. Name the problem and recommend a fix. | **Convenience sample, voluntary-response bias.** Attendees differ from non-attendees. Fix: a simple random sample from the resident list, or stratified by building. | Half credit for naming the bias without a concrete fix. Any defensible random design from the full population earns full credit. |
| 300 | **Excel.** From `GreenValleyCommons_Residents48.csv`, monthly income: mean, sd, SE, t* for 95%. Excel function for each. | **Mean $3,429.25** (AVERAGE), **sd $345.78** (STDEV.S), **SE $49.91** (unrounded 49.9086), **t* = 2.012** (`T.INV.2T(.05, 47)`). df = 47. | All four for full credit. SE $49.91 against the lab's $78.57 at n = 20 is worth a sentence to the room. |
| 400 | **Excel.** The 95% interval from the 48-resident file. Margin and both endpoints, money to the cent. Did the Lab 3B plan (48 residents for a $100 margin) work? | **Margin $100.40. $3,328.85 to $3,529.65.** Yes: the plan promised about $100 and delivered $100.40, because the follow-up sd ($345.78) landed near the assumed $351.38. `CONFIDENCE.T(.05, STDEV.S(range), 48)`. 90% for the record: $3,345.51 to $3,512.99 (t* = 1.678). | Endpoints within one cent earn full credit. Full credit also needs the "yes, and why" on the plan. |
| 500 | **Excel.** (1) 22 of 48 are men: check the condition and, if it passes, the 95% interval for the share. (2) n for a $75 margin on income at 95% using sd $345.78. | **(1) Passes:** 22 and 26, both at least 10. p-hat .46, margin .14, **interval .32 to .60**. "Not yet" at n = 20 became an answer at n = 48, a wide one. **(2) (1.96 × 345.78 / 75)² = 81.7, round up to 82.** | Full credit needs the condition with its numbers, the interval, and 82 (not 81). A team that says "not reportable" has copied the lab's answer without checking. |

### 5. The Manager Sentence

Interpretation, the classic errors, and the decision sentence, all on the new numbers. The $500 is
the Daily Double.

| $ | Question | Answer | Scoring note |
|---|---|---|---|
| 100 | 95% interval $3,328.85 to $3,529.65 from 48 residents. The one correct interpretation sentence. | "We are 95% confident that the true mean monthly income of Green Valley Commons residents is between $3,328.85 and $3,529.65, based on a sample of 48." Confidence is in the method: 95 of 100 such intervals capture the true mean. | Accept any wording that puts the confidence on the procedure and names the parameter, n, and the level. |
| 200 | Why is "95% of residents earn between..." wrong, and why is "there is a 95% probability the mean is in this range" wrong? | **First:** the interval is about the mean, not individuals; individuals vary by sd $345.78, the mean by SE $49.91. **Second:** the mean is fixed, not random; the 95% belongs to the procedure. | Full credit needs both. Catching the first sentence is a graded Module 3 skill. |
| 300 | New detector: P(fraud given flagged) = .66; of 288 flags per 10,000 orders, 190 fraud and 98 legitimate. Manager wants to auto-cancel. Decision verb, evidence in business units, what it does not mean. | Either decision earns credit with the counts: **hold for a quick verification step** (98 good customers turned away per 10,000 orders, one in three flags), or **auto-cancel and budget 98 apology calls** if fraud losses outweigh them. Does not mean .66 is the catch rate (95%), does not mean the 98 are careless shoppers. | Half credit for a decision with no counts. No credit for "66% accurate". This cell rewards judgment, not recall. |
| 400 | Drop/add week, 25 per hour: P(more than 25) = .45, P(more than 30) = .14, P(more than 35) = .02. Fill the Module 2 skeleton and defend the staffing level. | Any level with its risk priced: "Plan for 30; .14 chance of exceeding, a queue about one hour in seven, post the wait." Or "Plan for 35; .02 chance, open two more desks." Planning for the average means a queue nearly every other hour. | No credit for a level with no probability, or a probability with no action. |
| 500 DD | Three-sentence So What / Now What memo to the board on the follow-up survey: 48 residents, mean $3,429.25, interval $3,328.85 to $3,529.65 (margin $100.40, the $100 target met), share of men .46 (.32 to .60), 82 residents for a $75 margin. | Rubric: (a) point estimate and interval with n and level; (b) a takeaway a board member can act on, in business language; (c) a next step with a number: act on income now, or 82 residents for a $75 margin, or both. Model answer in the game. | Only the picking team answers, for their wager. Half credit for two of three. Reject formula-heavy memos and the "probability the mean is" sentence. Read the model aloud after revealing. |

### Final Jeopardy (tie-break only)

Category shown before wagers: Read the Table.

| Question | Answer | Scoring note |
|---|---|---|
| SummitGear adds a riskier product line and the fraud rate rises from 2% to 5%. The detector is the original one: 90% catch rate, 5% false-alarm rate. Build the tree of 10,000. P(fraud given flagged) now? | 500 fraudulent, 9,500 legitimate. True flags 450, false flags 475, flags in all 925. 450 / 925 = .4865, so **.49**. Up from .27 at a 2% base rate. | Accept .49, or 450 of 925. ".90" is the catch rate and is wrong. Written answers only; one per team. |

**Spare question** (sudden death, or swap it into the `FINAL` object in `index.html`): Angela
wants a $50 margin of error on mean monthly income at 95%, with sd $351.38. How many residents?
Answer: (1.96 × 351.38 / 50)² = 189.7, rounded up to **190**. Accept 190 only; 189 is the
rounding-down error.

---

## Wrap-up: the five minutes after the game

Most-missed concepts to name for the room, in the order they usually come up:

1. **P(fraud given flag) is not the catch rate.** The 95% is the other direction, and the
   false-alarm rate is the lever when the condition is rare.
2. **Off by one in the cumulative functions.** "More than 30" is 1 minus P(30 or fewer).
3. **"95% of residents earn between."** The interval is about the mean.
4. **Check the proportion condition every time.** It failed at 20 and passed at 48. "Not
   reportable" is a check, not a reflex.
5. **Rounding.** .31 not 0.31, money to the cent, t* to three decimals, round n up.

Confirm the midterm format (date, length, open-note policy, calculator, no AI tools of any kind,
which is the course rule and the Honor Code). Point students at the module workbooks, the notes
guides, and the method sheets in `4_Library/method/` as the formula reference. Students can replay
the game on the Pages URL for solo practice.

**Questions to expect**

- "Will the midterm be this hard?" About this difficulty, with more multi-step items.
- "Are these the exact questions?" No. The concepts and the scenarios are the ones from the labs;
  the numbers on the exam will be new, the way these were.
- "Can we use the AI Block tools on the midterm?" No. Never on quizzes or exams.
