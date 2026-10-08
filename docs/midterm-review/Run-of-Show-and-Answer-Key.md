# INFO 1020 Midterm Review Jeopardy, Fall 2026

## Run-of-show and answer key

**Game:** https://data-love-co.github.io/info1020-stats-os/midterm-review/
**Scope:** Modules 1 to 3. Probability, distributions, sampling and confidence intervals.
**What each team needs open:** Excel with a **blank workbook**, plus `SummitGear_Data.csv` and
`GreenValleyCommons_Residents48.csv` from `4_Library/sample-data/`. Lab workbooks stay closed.
Every computation in the game is a cut the labs did not make, so the old tabs will not help and
the habit the game builds is applying the method to a new question. Every cell asks one thing,
and every answer gives the number, the computation, and the Excel function.
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
- Clock budget: the 25 limits add up to 47 minutes with the Excel minutes, which leaves about a
  minute per cell for the reveal inside the 80-minute gameplay block.

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
`check-game-values.py`.

### 1. Know Your Rules

Formulas and vocabulary. No computation.

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | Confidence interval for a mean, population sd unknown: which critical value? | **t**, df = n minus 1. | Accept "t" or "t-star". |
| 200 | Write the formula for P(B given A). | **P(A and B) / P(A).** | Full credit needs P(A) in the denominator. |
| 300 | State the rule for P(A or B). | **P(A) + P(B) minus P(A and B).** | Full credit needs the subtracted overlap. |
| 400 | If n goes from 40 to 160, what happens to the standard error of the sample mean? | **It is cut in half.** SE = sd / SQRT(n); SQRT(160) is twice SQRT(40). | Half credit for "it gets smaller" without the half. |
| 500 | Full confidence-interval formula for a mean with sd unknown, naming each symbol. | **x̄ ± t* · (s / √n).** x̄ sample mean; t* from the t distribution with df = n minus 1; s sample sd; n sample size. | Full credit needs df = n minus 1. |

### 2. Read the Table

Module 1. SummitGear's 250 orders cut by channel and membership. Shown on the $100 to $300 cells:

|  | Online | In-store | Total |
|---|---|---|---|
| Rewards member | 51 | 34 | 85 |
| Not a member | 113 | 52 | 165 |
| Total | 164 | 86 | 250 |

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | P(online and member)? | **.20** (51 / 250 = .204). | ".20", not "0.20". |
| 200 | P(member given online)? | **.31** (51 / 164 = .311). | No credit for .20 (divided by 250). |
| 300 | P(online or member)? | **.79** ((164 + 85 minus 51) / 250 = 198 / 250 = .792). | No credit for 1.00 (overlap not subtracted). |
| 400 | **Excel.** From `SummitGear_Data.csv`: P(returned given in-store), where returned means Items Returned is 1 or more. | **.22** (19 of 86 = .221). | Accept .22 or 19 of 86. |
| 500 | New detector: 2% fraud, 95% catch rate, 1% false-alarm rate. P(fraud given flagged)? | **.66.** 200 fraud, 9,800 legitimate; 190 true flags, 98 false flags, 288 flags; 190 / 288 = .6597. | Accept .66 or 190 of 288. No credit for .95, the catch rate. |

### 3. Pick the Distribution

Module 2. Highlands Ranch registration and the ski resort, new numbers throughout.

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | The desk's phone line averages 8 calls per hour, no upper limit. Which distribution? | **Poisson**, lambda = 8. | Accept "Poisson" alone. |
| 200 | 25 acceptance letters, each enrolls with probability .60, independently. Expected number who enroll? | **15.00** (binomial, n times p). | Accept "15". |
| 300 | Gondola stops 3 to 15 minutes, every length equally likely. P(under 5)? | **.17** (uniform, 2 / 12 = .167). | Accept 2/12 said aloud if they then round to .17. |
| 400 | **Excel.** Drop/add week, 25 walk-ins per hour, capacity 30. P(more than 30)? | **.14** (`=1-POISSON.DIST(30,25,TRUE)`, unrounded .1367). | No credit for .10, which is P(more than 31). |
| 500 | **Excel.** Skier counts: mean 747.39, sd 159.63, bell shaped. 95th percentile of daily skiers? | **1,010 skiers** (`=NORM.INV(.95,747.39,159.63)` = 1,009.96). | Accept 1,010 or 1,009.96. |

### 4. Mind the Margin

Module 3. SummitGear as a population (Lab 3A) with a new sample size; Angela's follow-up survey of
48 residents, which the labs never opened.

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | SummitGear population mean $100.14, sd $36.99. Samples of 100. Standard error of the sample mean? | **$3.70** ($36.99 / SQRT(100) = 3.6992). | Accept $3.70. |
| 200 | Angela surveys the 20 residents who show up to Tuesday's meeting. What is wrong with this sample? | **Convenience sample with voluntary-response bias.** Attendees differ from non-attendees. | Accept "convenience", "voluntary response", or "not representative" with the reason. |
| 300 | **Excel.** From `GreenValleyCommons_Residents48.csv`, the standard error of mean monthly income. | **$49.91** (sd $345.78 / SQRT(48) = 49.9086). | Accept $49.91. |
| 400 | **Excel.** The 95% interval for mean monthly income from the 48-resident file, money to the cent. | **$3,328.85 to $3,529.65.** t* = `T.INV.2T(.05, 47)` = 2.012; margin = 2.012 × 49.9086 = $100.40. | Endpoints within one cent earn full credit. |
| 500 | **Excel.** 22 of 48 residents are men. The 95% interval for the share of men, if the condition allows it. | **.32 to .60.** Condition passes: 22 and 26, both at least 10. p-hat .46, margin .14. | No credit for "not reportable". |

### 5. The Manager Sentence

Interpretation and the decision sentence. The $500 is the Daily Double.

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | 95% interval $3,328.85 to $3,529.65 from 48 residents. The one correct interpretation sentence. | "We are 95% confident that the true mean monthly income of Green Valley Commons residents is between $3,328.85 and $3,529.65, based on a sample of 48." | Accept any wording that puts the confidence on the method and names the parameter, n, and the level. |
| 200 | A classmate writes "95% of residents earn between $3,329 and $3,530." Why is this wrong? | **The interval is about the mean, not individuals.** Individuals vary by sd $345.78, the mean by SE $49.91. | Full credit for "mean, not individuals" in any wording. |
| 300 | New detector: P(fraud given flagged) = .66; of 288 flags per 10,000 orders, 190 fraud and 98 legitimate. Manager wants to auto-cancel. Write the manager sentence. | Either decision with the counts: **hold for a quick verification step** (98 good customers turned away per 10,000 orders), or **auto-cancel and budget 98 apology calls**. Plus: .66 is not the catch rate. | Full credit needs a decision verb, the counts, and what .66 does not mean. No credit for "66% accurate". |
| 400 | Drop/add week, 25 per hour: P(more than 25) = .45, P(more than 30) = .14, P(more than 35) = .02. Fill the Module 2 skeleton. | Any level with its probability next to the action: "Plan for 30; .14 chance of exceeding, post the wait." Or "Plan for 35; .02 chance, open two more desks." | No credit for a level with no probability, or a probability with no action. |
| 500 DD | Three-sentence So What / Now What memo to the board on the follow-up survey, with the facts given on screen. | (1) point estimate and interval with n and level; (2) a takeaway a board member can act on; (3) a next step with a number: act on income now, or 82 residents for a $75 margin, or both. Model in the game. | Only the picking team answers, for their wager. Full credit needs all three parts. |

### Final Jeopardy (tie-break only)

Category shown before wagers: Read the Table.

| Question | Answer | Scoring |
|---|---|---|
| SummitGear adds a riskier product line and the fraud rate rises from 2% to 5%. The detector is the original one: 90% catch rate, 5% false-alarm rate. P(fraud given flagged) now? | **.49.** 500 fraudulent, 9,500 legitimate; true flags 450, false flags 475, flags in all 925; 450 / 925 = .4865. | Accept .49 or 450 of 925. No credit for .90, the catch rate. Written answers only; one per team. |

**Spare question** (sudden death, or swap it into the `FINAL` object in `index.html`): Angela
wants a $50 margin of error on mean monthly income at 95%, with sd $351.38. How many residents?
Answer: (1.96 × 351.38 / 50)² = 189.7, rounded up to **190**. Accept 190 only.

---

## Wrap-up: the five minutes after the game

Most-missed concepts to name for the room, in the order they usually come up:

1. **P(fraud given flag) is not the catch rate.**
2. **Off by one in the cumulative functions.** "More than 30" is 1 minus P(30 or fewer).
3. **"95% of residents earn between."** The interval is about the mean.
4. **Check the proportion condition every time.** It failed at 20 and passed at 48.
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
