# INFO 1020 Final Review Jeopardy, Fall 2026

## Run-of-show and answer key

**Game:** https://data-love-co.github.io/info1020-stats-os/final-review/
**Date:** Thursday, November 12, 2026.
**Scope:** Modules 4 to 7. One-sample and two-sample tests, ANOVA, chi-square.
**What each team needs open:** one laptop with Excel open to a **blank workbook**. No data file:
the four Excel cells put every number on the screen. Lab workbooks stay closed. Every computation
is net new, so the old tabs will not help. Every cell asks one thing, and every answer gives the
result, the computation, and the Excel function.
**Scenario:** Fourteener Fitness, a fictional Colorado gym chain with 4 locations (Golden,
Boulder, Fort Collins, Colorado Springs). Read the card on screen once before the first cell.
**Daily Double:** So What? Now What?, $500.
**Tie-break:** Final Jeopardy, the ★ button in the banner. Rules and key below.

> Fill in: [class length], [prize list], [extra-credit rule], [final exam date]. The clocks are
> double the original plan, for the pace of this section. The board runs in about 81 minutes: the
> 25 clocks add up to 62.5 minutes, plus about 45 seconds per cell for the reveal and the scoring.
> If the period is shorter, skip the $100 row or stop the clock early on cells every team has
> answered.

### Run-of-show

| Time | Segment |
|---|---|
| 0:00 to 0:05 | Welcome, prize reveal, the tie-break rule |
| 0:05 to 0:10 | Form six teams. Teams are pre-named in the game: Bayes Watch, Margin of Terror, Significant Others, The Outliers, Mode Squad, Standard Errors. Each team opens a blank workbook on one laptop and gets paper for written answers |
| 0:10 to 0:12 | Read the Fourteener Fitness card. Walk through the letter hold-up and the Daily Double |
| 0:12 to 1:33 | Gameplay. About 81 minutes for 25 cells |
| 1:33 to 1:40 | Final scores (Final Jeopardy if tied), prizes |
| 1:40 to 1:45 | Wrap-up: the five things to say before the final |

**How a cell runs: all teams play**

Every team answers every cell. The picking team only chooses the cell; nobody buzzes in. The game
starts a countdown the moment the question appears:

| Cell | Clock | Format |
|---|---|---|
| $100 | 1 minute | Multiple choice, hold up a letter |
| $200 | 1.5 minutes | Multiple choice (Chi Another Day $200: write the number) |
| $300 | 2 minutes | Multiple choice |
| $400 | 2 minutes | Multiple choice |
| $500 | 6 minutes | Excel, numbers on screen (4 minutes plus 2 for Excel). Daily Double: written memo, 6 minutes |

The four Excel cells get the 2 extra minutes automatically: the $500 cells in Pick Your Test, Reject
or Not?, ANOVA-thing Goes, and Chi Another Day. **Pause** and **+30s** sit next to the clock.

- $100 to $400: when the clock ends, every team holds up A, B, C or D at once. The right letter
  earns the cell value; a wrong letter costs nothing.
- $500 Excel cells: teams write the answer on paper and hold it up when the clock ends.
- Reveal with **R** or the button, which stops the clock. Click each team that got it right in
  the row under the answer; each click adds the cell value (click again to undo). For a
  partial-credit call, use the side panel's +/− buttons instead.
- Daily Double is the one exception: only the team that picked the cell answers, for a wager up
  to its current score (or up to $500 if under $500). After the answer, click **Award wager** or
  **Deduct wager**.

**Tie-break: Final Jeopardy**

Say this rule before the first cell is picked, so no one argues later.

- If two or more teams are tied for first when the board is cleared, click **★ Final Jeopardy**.
  The tied teams are pre-selected; untick anyone else.
- Each playing team writes a wager, up to its score (or up to $500 if its score is below $500),
  before the question is shown. Lock the wagers.
- Show the question. The game runs a 2-minute clock. Teams write one answer on paper and hold it
  up together.
- Reveal the answer, then mark each team **Correct** or **Wrong**. The wager is added or
  subtracted and the new score shows in the row.
- Still tied (both right or both wrong with equal wagers): the team with fewer wrong answers
  during the board wins. Keep a tally on paper, or run the spare question below as sudden death.

**Rounding is graded, even here.** If a team writes "0.029", ask for it the course way: ".029".
p-values to three decimals with no leading zero and p < .001 below that, test statistics to two,
critical values to three, money to the cent.

---

## Answer key

Ordered by category, lowest to highest value. The game presents cells in whatever order teams pick
them. Every value below is recomputed by `check-game-values.py`.

### 1. Pick Your Test

Step zero. Read the design, name the test.

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | The same 30 members, weekly visits for 4 weeks before and 4 weeks after the app. Which test answers whether visits changed? | **C. Paired t-test.** The same members are measured twice. | Letter only. |
| 200 | 50 new members saw page A, 50 different new members saw page B. Which test answers whether average first-month spend differs? | **D. Two-sample t-test.** Different people in each group. | Letter only. Point out that equal group sizes do not make it paired. |
| 300 | Satisfaction (1 to 10), 12 members at each of 4 locations. Which test answers whether average satisfaction differs by location? | **C. One-way ANOVA.** 4 means in one test. | Letter only. Talking point: 6 separate t-tests would push the false-alarm chance to about .26 (1 minus .95^6). |
| 400 | Last year 40% yoga, 30% spin, 20% strength, 10% climbing. Which test answers whether this year's 400 bookings moved off that split? | **D. Chi-square goodness of fit.** 1 categorical variable against benchmark shares. | Letter only. Independence needs 2 categorical variables. |
| 500 | **Excel.** Page A: n = 50, mean $62.40, s = $18.20. Page B: n = 50, mean $71.10, s = $20.50. Two-tailed p-value with df = 49. | **p = .029.** SE = $3.88, t = 2.24. `=T.DIST.2T(8.70/SQRT(18.2^2/50+20.5^2/50), 49)` | Accept .029 only. No credit for .015 (one tail). If a team pooled with df 98 per the guide's ratio rule (20.50 / 18.20 = 1.13, under 2), they get .027: give half and point to the df the question set. |

### 2. Reject or Not?

Reading output and p-values. This Excel output is shown on the $200, $300 and $500 cells:

| t-Test: Two-Sample Assuming Unequal Variances | Morning | Evening |
|---|---|---|
| Mean (visits per month) | 11.80 | 10.10 |
| Variance | 20.3 | 19.0 |
| Observations | 45 | 48 |
| df | 90 | |
| t Stat | 1.85 | |
| P(T<=t) one-tail | 0.034 | |
| t Critical one-tail | 1.662 | |
| P(T<=t) two-tail | 0.068 | |
| t Critical two-tail | 1.987 | |

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | Excel prints P(T<=t) two-tail = 4.7E-06. How do you write it in a memo? | **C. p < .001.** | Letter only. |
| 200 | Do morning and evening members visit a **different** number of times? Decision at .05 from the output. | **D. Fail to reject H0: the two-tail p (.068) is above .05.** | Letter only. Talking point: the one-tail line answers a question nobody asked. |
| 300 | A 95% interval for mu(morning) minus mu(evening) must: | **A. Contain 0.** A 95% interval and a two-tailed test at .05 always agree. | Letter only. |
| 400 | A different test returns p = .011. Which statement is correct? | **C. A gap this large is rare (1.1%) if H0 is true.** | Letter only. Never "the chance that H0 is true". |
| 500 | **Excel.** Difference 1.70 visits, SE 0.92, df 90. The 95% interval for mu(morning) minus mu(evening). | **-0.13 to 3.53 visits.** t* = 1.987, margin = 1.83. `=1.70-T.INV.2T(0.05,90)*0.92` and `=1.70+...` | Endpoints within .02 earn full credit. It contains 0, which agrees with the $200 decision: say it aloud after scoring. |

### 3. ANOVA-thing Goes

Reading an ANOVA and what comes after it. Both tables are shown on the $100 to $400 cells:

| Location | n | Mean | Std dev |
|---|---|---|---|
| Golden | 12 | 8.10 | 1.30 |
| Boulder | 12 | 7.90 | 1.25 |
| Fort Collins | 12 | 7.70 | 1.40 |
| Colorado Springs | 12 | 6.10 | 1.35 |

| Source of Variation | SS | df | MS | F | P-value | F crit |
|---|---|---|---|---|---|---|
| Between Groups | 30.12 | 3 | 10.04 | 5.71 | 0.0022 | 2.816 |
| Within Groups | 77.39 | 44 | 1.76 | | | |
| Total | 107.51 | 47 | | | | |

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | The alternative hypothesis for this ANOVA is: | **C. At least 1 location mean differs.** | Letter only. |
| 200 | F = 5.71 above F crit 2.816, p = .002. What can you conclude? | **D. The 4 locations do not all share the same mean.** | Letter only. F does not say which ones differ. |
| 300 | ANOVA rejected H0. The right next step to find which locations differ? | **C. Run a Tukey HSD post hoc test.** | Letter only. |
| 400 | Tukey: Colorado Springs differs from each of the other 3; no other pair differs. Which So What is right? | **A. Location matters: Colorado Springs is the low one.** No difference detected among the other 3. | Letter only. Checked: HSD = 1.45 (q = 3.776 for 4 groups, df 44); Colorado Springs gaps are 1.60 to 2.00, the others 0.40 or less. |
| 500 | **Excel.** Spend by tier (Basic, Plus, Premium), 10 each: SS between 1,840, SS within 9,720. The ANOVA p-value. | **p = .096.** df 2 and 27, MSTr 920, MSE 360, F = 2.56. `=F.DIST.RT((1840/2)/(9720/27),2,27)` | Accept .096 only. Talking point after scoring: fail to reject, so no Tukey. A post hoc test after a failed F is fishing. |

### 4. Chi Another Day

Goodness of fit against a benchmark. This table is shown on the $100, $200 and $400 cells:

| Class type | Benchmark share | This year (400 bookings) |
|---|---|---|
| Yoga | 40% | 138 |
| Spin | 30% | 128 |
| Strength | 20% | 92 |
| Climbing | 10% | 42 |

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | Degrees of freedom for this goodness-of-fit test? | **B. 3.** Categories minus 1. | Letter only. Sample size does not enter the df. |
| 200 | Expected yoga bookings under last year's mix? (Write the number.) | **160.00.** .40 times 400. `=0.40*400` | Accept 160. No credit for 138, the observed count. |
| 300 | Pilates at 1% of 400 bookings has an expected count of 4. What should you do? | **C. Combine Pilates with a related class type.** | Letter only. Alpha does not fix a small expected count. |
| 400 | Chi-square = 5.46 on 3 df, p = .141. Which conclusion is right? | **D. The mix has not been shown to differ from last year.** Critical value 7.815. `=CHISQ.INV.RT(0.05,3)` | Letter only. Failing to reject is not proof the mix is unchanged. |
| 500 | **Excel.** Colorado Springs, 200 bookings: yoga 58, spin 74, strength 42, climbing 26, same benchmark. The chi-square statistic. | **11.22.** Expected 80, 60, 40, 20; contributions 6.05 + 3.27 + 0.10 + 1.80. `=SUMPRODUCT((O-E)^2/E)` | Accept 11.22 only. Talking point after scoring: p = .011 (`=CHISQ.DIST.RT(11.22,3)`), so reject: Colorado Springs books less yoga and more spin than the benchmark. |

### 5. So What? Now What?

Interpretation in business language. The $500 is the Daily Double.

| $ | Question | Answer | Scoring |
|---|---|---|---|
| 100 | The app test fails to reject H0. Which statement is right? | **A. We found no evidence that the app changed visits.** | Letter only. |
| 200 | Failed to reject, dropped the app; better data later shows it raises visits. Which error? | **C. Type II error.** A real effect was missed. | Letter only. Type I is a false alarm. |
| 300 | 20,000 members, page B raises spend $0.40 a month, p = .003. The right read? | **D. Significant, but $0.40 may be too small to matter.** | Letter only. |
| 400 | Colorado Springs is the 1 location below the others. Which Now What fits best? | **B. Investigate Colorado Springs before changing the rest.** | Letter only. No winner to reward, no reason to change all 4. |
| 500 DD | 30 members, 0.9 more visits per week after the app (paired t = 3.10, p = .004, 95% interval 0.31 to 1.49). What, So What, Now What memo for the VP of Member Experience, ending with 1 question to investigate next. | 4 parts: What (reject H0), So What with the numbers, Now What, next question with a reason. Model in the game. | Only the picking team answers, for its wager. Award the wager for at least 3 of 4 parts, as on the exam essays. |

### Final Jeopardy (tie-break only)

Category shown before wagers: Reject or Not?

| Question | Answer | Scoring |
|---|---|---|
| Marketing's 95% interval for mu(page B) minus mu(page A), average first-month spend, is $0.91 to $16.49. What is the margin of error? | **$7.79.** Half the width: (16.49 minus 0.91) / 2. `=(16.49-0.91)/2` | Accept $7.79 only. No credit for $15.58, the full width, or $8.70, the point estimate. Written answers, 2 minutes. |

**Spare question** (sudden death, or swap it into the `FINAL` object in `index.html`): the
membership-tier ANOVA has df 2 and 27. What is the critical F at alpha = .05? Answer:
`=F.INV.RT(0.05,2,27)` = **3.354**. Accept 3.354 only.

---

## Wrap-up: the five things to say before the final

Most-missed concepts to name for the room, in the order they usually come up:

1. **Paired or independent is about whether the rows are linked**, not whether the groups are the
   same size.
2. **A "different" question is two-tailed: read the two-tail line.** A 95% interval and a
   two-tailed test at .05 always agree.
3. **Failing to reject is not proof.** Say "not shown to differ", never "proven the same".
4. **ANOVA says at least 1 mean differs. Tukey names the pairs**, and groups with no detected
   difference do not get ranked.
5. **Chi-square: expected counts come from the benchmark**, every one must be at least 5, and a
   tiny p-value is written p < .001.

Confirm the final format (date, length, the Course Reference Guide as the permitted aid,
calculator, no AI tools of any kind, which is the course rule and the Honor Code). Students can
replay the game on the Pages URL for solo practice.

**Questions to expect**

- "Is the final like this?" The final covers Modules 1 to 7; this board reviews 4 to 7, where the
  final is weighted. Expect more Excel work per question.
- "Are these the exact questions?" No. Fourteener Fitness is a practice scenario; the exam's
  scenarios and numbers are different.
- "Can we use the AI Block tools on the final?" No. Never on quizzes or exams.
