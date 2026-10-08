# INFO 1020 Midterm Review Jeopardy, Fall 2026

A single-file, browser-based Jeopardy game for reviewing Modules 1 to 3 of **INFO 1020: Analytics
II** before the midterm. Five categories, twenty-five questions, one Daily Double, a Final
Jeopardy tie-break, team scoring for six teams. No build step, no dependencies, no tracking. It
runs offline once loaded.

**Play it:** https://data-love-co.github.io/info1020-stats-os/midterm-review/ or open
`index.html` in any browser.

This is the Fall 2026 rebuild of the
[Spring 2026 game](https://github.com/dataloveco/info1020-midterm-review-jeopardy). The game shell
is the same. The question bank is new.

## Net new by design

The scenarios are the course scenarios (SummitGear, Highlands Ranch, Green Valley Commons), but
**no computed answer is a number the labs produced.** The lab workbooks are no help during the
game; the work has to be done fresh in a blank sheet. Lab values appear only as inputs where the
scenario needs them (the skier mean and standard deviation, the SummitGear population mean and
standard deviation, the first survey's n of 20).

| Lab did | Game asks |
|---|---|
| SummitGear: membership by spending over $100 | Membership by sales channel; returns by channel; a new fraud detector |
| Binomial 15 at .80; Poisson 12.5; uniform 2 to 10; skier tail over 800 and the 90th percentile | Binomial 25 at .60; Poisson 8 and 25; uniform 3 to 15; skier tail under 500 and the 95th percentile |
| Standard error for samples of 40; Green Valley's first survey of 20 | Samples of 100; Angela's follow-up survey of 48 residents (`GreenValleyCommons_Residents48.csv`), which the labs never touched |

Every number in the game is recomputed from the CSVs by `check-game-values.py`:

```
python3 docs/midterm-review/check-game-values.py
```

## In the classroom

1. Open the game and press **F11** (Windows) or **Ctrl+Cmd+F** (Mac) for full screen.
2. The six teams come pre-named: Bayes Watch, Margin of Terror, Significant Others, The
   Outliers, Mode Squad, Standard Errors. Click a name in the right-hand panel to change it.
3. Each team needs one laptop with Excel open to a **blank workbook** and the two CSVs the cells
   name: `SummitGear_Data.csv` and `GreenValleyCommons_Residents48.csv`, both in
   `4_Library/sample-data/`. Lab workbooks stay closed.
4. Click a dollar cell to show a question. A countdown starts in the top bar: 45 seconds for
   $100, 1 minute for $200, 1.5 for $300, 2 for $400, 3 for $500, plus one minute on the seven
   cells that need Excel open. **Pause** and **+30s** sit next to it. **Every team** works the
   question within the limit; nobody buzzes in.
5. **R** or the button reveals the answer and stops the clock. A row of team chips appears under
   the answer: click each team that got it right and the cell value is added (click again to
   undo). A wrong answer costs nothing, so every team has a reason to try. The +/− buttons in the
   side panel still work for corrections. **Esc** returns to the board and marks the cell played.
6. The **$500 cell in The Manager Sentence** is the Daily Double, the one cell only the picking
   team answers. The game asks for that team and their wager, then shows **Award wager** and
   **Deduct wager** buttons.
7. Scores and played cells are saved in the browser, so an accidental refresh does not lose the
   game. **Reset Game** clears everything.
8. **Final Jeopardy** (the ★ button in the banner) is the tie-breaker. It pre-selects the teams
   tied for the lead, or everyone if there is no tie, and you can change who plays. Each playing
   team wagers up to its score, or up to $500 if its score is below $500, before the question
   appears. A 60-second clock runs while teams write their answer on paper. Reveal the answer,
   then mark each team Correct or Wrong and the wager is added or subtracted. **R** reveals,
   **Esc** returns to the board.

The instructor's timing, the full answer key with scoring notes, the tie-break rule, and the
wrap-up reminders are in `Run-of-Show-and-Answer-Key.md`.

## Coverage

| Category | Module | Scenario | What it tests |
|---|---|---|---|
| Know Your Rules | M1 to M3 | none | t versus z, conditional probability, the union rule, standard error, the full interval formula with every symbol |
| Read the Table | M1 | SummitGear by channel and membership; a new fraud detector | Joint, conditional, and union probability from a new contingency table; a COUNTIFS cut the lab did not make; the tree of 10,000 with new rates |
| Pick the Distribution | M2 | Highlands Ranch phone line, acceptance letters, the gondola, drop/add week, skier counts | Poisson, binomial, uniform, normal: name it, state its parameters, compute with the Excel function on new numbers |
| Mind the Margin | M3 | SummitGear samples of 100; Angela's follow-up survey of 48 | Standard error and the Central Limit Theorem, sampling bias, SE and t* from a fresh file, the 95% interval and whether the sample-size plan worked, a proportion interval that passes the condition, sample size for a new margin |
| The Manager Sentence | M1 to M3 | all three | The one correct interpretation, the two graded wrong sentences, a decision sentence on the new detector, a staffing call for drop/add week, the Daily Double memo on the follow-up survey |

Answers by cell. These are the game's own verification targets, not the lab's.

| Cell | Answer |
|---|---|
| Read the Table $100 | 51 orders, P(online and member) = .20 |
| $200 | P(member given online) = .31, P(member given in-store) = .40, against .34 overall |
| $300 | P(online or member) = .79; adding .66 and .34 double-counts 51 orders |
| $400 | P(returned given in-store) = .22, P(returned given online) = .10 |
| $500 | New detector: 190 true flags, 98 false flags, 288 flags, P(fraud given flagged) = .66 |
| Pick the Distribution $100 | Poisson, lambda 8, sd 2.83 |
| $200 | Binomial, n 25, p .60, EV 15.00, sd 2.45 |
| $300 | Uniform 3 to 15: P(under 5) = .17, P(over 10) = .42, mean 9.00 |
| $400 | P(more than 30) at 25 per hour = .14; the off-by-one gives .10 |
| $500 | Normal: P(fewer than 500) = .06, 95th percentile 1,010 |
| Mind the Margin $100 | SE at n = 100 is $3.70; P(sample mean over $105) = .09 |
| $300 | 48 residents: mean $3,429.25, sd $345.78, SE $49.91, t* 2.012 |
| $400 | Margin $100.40; $3,328.85 to $3,529.65; the $100 plan worked |
| $500 | Men 22 of 48: condition passes, .46, interval .32 to .60; n = 82 for a $75 margin |
| Manager Sentence $400 | P(more than 25) = .45, P(more than 30) = .14, P(more than 35) = .02 |
| Final Jeopardy | 5% base rate: 450 true, 475 false, 925 flags, P(fraud given flagged) = .49 |

## What changed from Spring 2026

- **Scope.** Spring covered probability, discrete distributions, sampling design, and confidence
  intervals on a LaunchPad and DU Men's Soccer scenario. Fall covers Modules 1 to 3 on the course
  scenarios, with every computation net new.
- **Dropped.** Geometric and negative binomial (not in the Fall Module 2 method sheet), the soccer
  workbook, the Twitter survey and Monday-tickets bias items.
- **Added.** The fraud-flag base rate (tree of 10,000), independence judged from a contingency
  table, the normal and uniform, the standard error and the Central Limit Theorem, the proportion
  condition passing and failing, sample size for a target margin, a Final Jeopardy tie-break, and
  the course rounding policy (two decimals and no leading zero for probabilities, money to the
  cent, critical values to three decimals).
- **Every computed answer names its Excel function**, in a "Check it in Excel" box, so students can
  compare cell by cell.
- **No em dashes, plain language, business language.** The course writing conventions in
  `AGENTS.md` apply to the game text.
- **Shell improvements.** Scores persist across a refresh, the Daily Double awards or deducts the
  exact wager with one click, **R** reveals the answer, cells are keyboard-focusable buttons, and
  the layout stacks on a phone so students can replay it for practice.

## Editing the questions

All content is in the `QUESTIONS` object inside `index.html`. Each entry is keyed
`"categoryIndex-valueIndex"` (both 0-based) with `q` and `a` HTML strings. Add `dailyDouble: true`
to make any cell the Daily Double. Category names are in `CATEGORIES`. The shared scenario cards
(`SUMMITGEAR`, `SG_TABLE`, `HIGHLANDS`, `GREENVALLEY`, `GREENVALLEY48`) are constants above the
question bank, so a change to a scenario shows up in every cell that uses it.

The Final Jeopardy question is the `FINAL` object just above the keyboard handler: `category`,
`q`, `a` (the short answer), and `explain`. The shipped question is the fraud-flag tree at a 5%
base rate (answer .49), chosen because the written answer is one checkable number. A spare is in
the run-of-show.

When you change a number, add or update its line in `check-game-values.py` and run it. Keep the
rounding policy: `4_Library/method/rounding-policy.md`.

## License

Course materials in this repository are CC BY-NC-SA 4.0 and the code is MIT. See the repository
root.
