# INFO 1020 Midterm Review Jeopardy, Fall 2026

## Run-of-show and answer key

**Game:** https://data-love-co.github.io/info1020-stats-os/midterm-review/
**Scope:** Modules 1 to 3. Probability, distributions, sampling and confidence intervals.
**What each team needs open:** Excel with a **blank workbook**, plus `SummitGear_Data.csv` and
`GreenValleyCommons_Residents48.csv` from `4_Library/sample-data/`. Lab workbooks stay closed.
Every computation in the game is a cut the labs did not make, so the old tabs will not help and
the habit the game builds is applying the method to a new question. Every cell asks one thing.
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

The six Excel cells get the extra minute automatically: Read the Table $400, Pick the
Distribution $400 and $500, Mind the Margin $300 to $500. **Pause** and **+30s** sit next to the
clock.

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
- Clock budget: the 25 limits add up to 47 minutes with the Excel minutes, which leaves about a
  minute per cell for the reveal and the teaching moment inside the 80-minute gameplay block.

**Tie-break: Final Jeopardy**

Say this rule before the first cell is picked, so no one argues later.

- If two or more teams are tied for first when the board is cleared, click **★ Final Jeopardy**.
  The tied teams are pre-selected; untick anyone else.
- Each playing team writes a wager, up to its score (or up to $500 if its score is below $500),
  before the question is shown. Lock the wagers.
- Show the question. The game runs a 60-second clock. Teams write one answer on paper and hold it
  up together.
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
`check-game-values.py`. The "teaching moment" column is what to say after the reveal; it is not
part of the question.

### 1. Know Your Rules

Formulas and vocabulary. Quick recall across all three modules. No computation.

| $ | Question | Answer | Teaching moment and scoring |
|---|---|---|---|
| 100 | Confidence interval for a mean, population sd unknown: which critical value? | **t**, df = n minus 1. | z is for a known population sd (almost never) and for proportions. Accept "t" or "t-star". |
| 200 | Write the formula for P(B given A). | **P(A and B) / P(A).** | The denominator shrinks to the rows where A is true. "Divide by n" is the Module 1 classic error. |
| 300 | State the rule for P(A or B). | **P(A) + P(B) minus P(A and B).** | The overlap is in both terms; subtract it once so it is counted once. |
| 400 | If n goes from 40 to 160, what happens to the standard error of the sample mean? | **It is cut in half.** SE = sd / SQRT(n); SQRT(160) is twice SQRT(40). | SE is the spread of the sampling distribution, not the data. Half credit for "it gets smaller" without the half. |
| 500 | Full confidence-interval formula for a mean with sd unknown, naming each symbol. | **x̄ ± t* · (s / √n).** x̄ sample mean; t* from the t distribution with df = n minus 1; s sample sd; n sample size. | The df detail is required. Excel: `CONFIDENCE.T(alpha, s, n)` is the margin. |

### 2. Read the Table

Module 1. SummitGear's 250 orders cut by channel and membership. The lab cut them by membership
and spending; this table is new. Shown on the $100 to $300 cells:

|  | Online | In-store | Total |
|---|---|---|---|
| Rewards member | 51 | 34 | 85 |
| Not a member | 113 | 52 | 165 |
| Total | 164 | 86 | 250 |

| $ | Question | Answer | Teaching moment and scoring |
|---|---|---|---|
| 100 | P(online and member)? | **.20** (51 / 250 = .204). | A joint divides by the grand total. ".20", not "0.20". |
| 200 | P(member given online)? | **.31** (51 / 164). | For the record: P(member given in-store) = .40 and P(member) = .34. Not independent, but a nine-point gap, far smaller than the lab's membership-by-spending gap. Size the gap before calling it a finding. |
| 300 | P(online or member)? | **.79** ((164 + 85 minus 51) / 250 = 198 / 250). | Adding .66 and .34 gives 1.00, which the 52 in-store non-member orders disprove. The overlap was counted twice. |
| 400 | **Excel.** From `SummitGear_Data.csv`: P(returned given in-store), where returned means Items Returned is 1 or more. | **.22** (19 of 86). | For the record: online is .10 (17 of 164). In-store orders are returned about twice as often; the lab's overall .14 hid it. The counts are not in any lab tab. |
| 500 | New detector: 2% fraud, 95% catch rate, 1% false-alarm rate. P(fraud given flagged)? | **.66.** 200 fraud, 9,800 legitimate; 190 true flags, 98 false flags, 288 flags; 190 / 288 = .6597. | Up from .27. The false-alarm cut (490 to 98) did almost all of it; the catch rate added 10 true flags. A team that answers ".95" has given the catch rate; say so to the room. Full credit needs the counts and .66. |

### 3. Pick the Distribution

Module 2. Highlands Ranch registration and the ski resort, new numbers throughout.

| $ | Question | Answer | Teaching moment and scoring |
|---|---|---|---|
| 100 | The desk's phone line averages 8 calls per hour, no upper limit. Which distribution? | **Poisson**, lambda = 8. | sd = SQRT(8) = 2.83. "Binomial" is the Module 2 classic error: there is no n. Accept "Poisson" alone. |
| 200 | 25 acceptance letters, each enrolls with probability .60, independently. Expected number who enroll? | **15.00** (binomial, n times p). | Name the binomial and its conditions after the reveal; sd = 2.45. Accept "15". |
| 300 | Gondola stops 3 to 15 minutes, every length equally likely. P(under 5)? | **.17** (2 / 12 = .167). | Uniform. For the record: P(over 10) = .42, mean 9.00 minutes. Accept the fraction said aloud if they then round the course way. |
| 400 | **Excel.** Drop/add week, 25 walk-ins per hour, capacity 30. P(more than 30)? | **.14** (`=1-POISSON.DIST(30,25,TRUE)`, unrounded .1367). | The off-by-one caution: 31 in that formula gives P(more than 31) = .10, a different question. For the record: P(more than 35) = .02. |
| 500 | **Excel.** Skier counts: mean 747.39, sd 159.63, bell shaped. 95th percentile of daily skiers? | **1,010 skiers** (`=NORM.INV(.95,747.39,159.63)` = 1,009.96). | Normal, because a daily count is a bell-shaped measurement. For the record: P(fewer than 500) = .06. Whole number, because counts. |

### 4. Mind the Margin

Module 3. SummitGear as a population (Lab 3A) with a new sample size; Angela's follow-up survey of
48 residents, which the labs never opened.

| $ | Question | Answer | Teaching moment and scoring |
|---|---|---|---|
| 100 | SummitGear population mean $100.14, sd $36.99. Samples of 100 (the lab used 40). Standard error of the sample mean? | **$3.70** ($36.99 / SQRT(100) = 3.6992). | Spread of the sample mean, not the data. For the record: P(sample mean over $105) = .09 by the CLT. |
| 200 | Angela surveys the 20 residents who show up to Tuesday's meeting. What is wrong with this sample? | **Convenience sample, voluntary-response bias.** Attendees differ from non-attendees. | The fix: a simple random sample from the resident list, or stratified by building. Accept "convenience", "voluntary response", or "not representative" with the reason. |
| 300 | **Excel.** From `GreenValleyCommons_Residents48.csv`, the standard error of mean monthly income. | **$49.91** (unrounded 49.9086). Mean $3,429.25 (AVERAGE), sd $345.78 (STDEV.S), divided by SQRT(48). | $49.91 at n = 48 against the lab's $78.57 at n = 20 is worth a sentence to the room. |
| 400 | **Excel.** The 95% interval for mean monthly income from the 48-resident file, money to the cent. | **$3,328.85 to $3,529.65.** t* = `T.INV.2T(.05, 47)` = 2.012; margin = 2.012 × 49.9086 = $100.40. `CONFIDENCE.T(.05, STDEV.S(range), 48)`. | Lab 3B promised a margin near $100 at n = 48 and the survey delivered $100.40. Endpoints within one cent earn full credit. |
| 500 | **Excel.** 22 of 48 residents are men. The 95% interval for the share of men, if the condition allows it. | **.32 to .60.** Condition passes: 22 and 26, both at least 10. p-hat .46, margin .14. | "Not yet" at n = 20 became an answer at n = 48, a wide one. A team that says "not reportable" has copied the lab's answer without checking. For the record: a $75 margin on income needs 82 residents. |

### 5. The Manager Sentence

Interpretation, the classic error, and the decision sentence, all on the new numbers. The $500 is
the Daily Double.

| $ | Question | Answer | Teaching moment and scoring |
|---|---|---|---|
| 100 | 95% interval $3,328.85 to $3,529.65 from 48 residents. The one correct interpretation sentence. | "We are 95% confident that the true mean monthly income of Green Valley Commons residents is between $3,328.85 and $3,529.65, based on a sample of 48." | Confidence is in the method: 95 of 100 such intervals capture the true mean. Accept any wording that puts the confidence on the procedure and names the parameter, n, and the level. |
| 200 | A classmate writes "95% of residents earn between $3,329 and $3,530." Why is this wrong? | **The interval is about the mean, not individuals.** Individuals vary by sd $345.78, the mean by SE $49.91. | The other wrong sentence, "there is a 95% probability the mean is in this range," is worth naming after the reveal. Catching the first is a graded Module 3 skill. |
| 300 | New detector: P(fraud given flagged) = .66; of 288 flags per 10,000 orders, 190 fraud and 98 legitimate. Manager wants to auto-cancel. Write the manager sentence. | Either decision with the counts: **hold for a quick verification step** (98 good customers turned away per 10,000 orders, one in three flags), or **auto-cancel and budget 98 apology calls** if fraud losses outweigh them. Plus what it does not mean: .66 is not the catch rate (95%). | Half credit for a decision with no counts. No credit for "66% accurate". This cell rewards judgment, not recall. |
| 400 | Drop/add week, 25 per hour: P(more than 25) = .45, P(more than 30) = .14, P(more than 35) = .02. Fill the Module 2 skeleton. | Any level with its risk priced: "Plan for 30; .14 chance of exceeding, a queue about one hour in seven, post the wait." Or "Plan for 35; .02 chance, open two more desks." | Planning for the average means a queue nearly every other hour. No credit for a level with no probability, or a probability with no action. |
| 500 DD | Three-sentence So What / Now What memo to the board on the follow-up survey, with the facts given on screen. | Rubric: (a) point estimate and interval with n and level; (b) a takeaway a board member can act on, in business language; (c) a next step with a number: act on income now, or 82 residents for a $75 margin, or both. Model answer in the game. | Only the picking team answers, for their wager. Half credit for two of three. Reject formula-heavy memos and the "probability the mean is" sentence. Read the model aloud after revealing. |

### Final Jeopardy (tie-break only)

Category shown before wagers: Read the Table.

| Question | Answer | Teaching moment and scoring |
|---|---|---|
| SummitGear adds a riskier product line and the fraud rate rises from 2% to 5%. The detector is the original one: 90% catch rate, 5% false-alarm rate. P(fraud given flagged) now? | **.49.** 500 fraudulent, 9,500 legitimate; true flags 450, false flags 475, flags in all 925; 450 / 925 = .4865. | Up from .27 at a 2% base rate: same detector, different base rate, different answer. Accept .49, or 450 of 925. ".90" is the catch rate and is wrong. Written answers only; one per team. |

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
