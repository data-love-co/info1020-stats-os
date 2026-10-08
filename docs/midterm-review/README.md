# INFO 1020 Midterm Review Jeopardy, Fall 2026

A single-file, browser-based Jeopardy game for reviewing Modules 1 to 3 of **INFO 1020: Analytics
II** before the midterm. Five categories, twenty-five questions, one Daily Double, team scoring
for up to six teams. No build step, no dependencies, no tracking. It runs offline once loaded.

**Play it:** open `index.html` in any browser, or visit the GitHub Pages copy at
`https://data-love-co.github.io/info1020-stats-os/midterm-review/` once this folder is on `main`.

This is the Fall 2026 rebuild of the
[Spring 2026 game](https://github.com/dataloveco/info1020-midterm-review-jeopardy). The game shell
is the same. The question bank is new, and every number in it comes from the course datasets in
`4_Library/sample-data/`, so a student can check any answer against their own lab workbook.

## In the classroom

1. Open the game and press **F11** (Windows) or **Ctrl+Cmd+F** (Mac) for full screen.
2. The six teams come pre-named: Bayes Watch, Margin of Terror, Significant Others, The
   Outliers, Mode Squad, Standard Errors. Click a name in the right-hand panel to change it.
3. Click a dollar cell to show a question. **R** or the button reveals the answer. **Esc** returns
   to the board and marks the cell played.
4. Score with the +/− buttons after each question. Correct adds the value, wrong subtracts it.
5. The **$500 cell in The Manager Sentence** is the Daily Double. The game asks which team is
   answering and for their wager, then shows **Award wager** and **Deduct wager** buttons so the
   odd amount does not have to be entered by hand.
6. Scores and played cells are saved in the browser, so an accidental refresh does not lose the
   game. **Reset Game** clears everything.

The instructor's timing, the full answer key with scoring notes, and the wrap-up reminders are in
`Run-of-Show-and-Answer-Key.md`.

## Coverage

| Category | Module | Scenario | What it tests |
|---|---|---|---|
| Know Your Rules | M1 to M3 | none | t versus z, conditional probability, the union rule, standard error, the full interval formula with every symbol |
| Read the Table | M1 | SummitGear Outfitters, 250 orders, and the fraud flag | Marginal, joint, and conditional probability from the contingency table; independence; the tree of 10,000 |
| Pick the Distribution | M2 | University of Highlands Ranch registration, Mt. Highlands Ranch resort | Poisson, binomial, uniform, normal: name it, state its parameters, compute with the Excel function |
| Mind the Margin | M3 | SummitGear as a population, Green Valley Commons | Standard error and the Central Limit Theorem, sampling bias, SE and t*, the 95% interval, the proportion condition, sample size |
| The Manager Sentence | M1 to M3 | all three | The one correct interpretation, the two graded wrong sentences, decision sentences for the fraud flag and the staffing call, the Daily Double memo |

Verification targets, by cell, all from `4_Library/sample-data/README.md`:

| Cell | Target |
|---|---|
| Read the Table $100 to $400 | P(member) = .34, P(member and over $100) = .26, P(member or over $100) = .56, P(over $100 given member) = .78, P(member given over $100) = .54, P(over $100) = .49 |
| Read the Table $500 | 180 true flags, 490 false flags, 670 flags, P(fraud given flagged) = .27 |
| Pick the Distribution | Poisson sd 3.54; binomial EV 12.00, sd 1.55, P(12) = .25, P(12 or more) = .65; uniform P(under 5) = .38, mean 6.00; P(more than 15) = .19; normal P(more than 800) = .37, 90th percentile 952 |
| Mind the Margin | SE $5.85 at n = 40; SE $78.57; t* = 2.093; margin $164.45; $3,234.45 to $3,563.35; 90% interval $3,263.04 to $3,534.76; proportion condition 8 and 12, not reportable; n = 48 for a $100 margin |

Run `python 0_System/scripts/check-values.py` from the repo root to recompute every target from
the CSVs.

## What changed from Spring 2026

- **Scope.** Spring covered probability, discrete distributions, sampling design, and confidence
  intervals on a LaunchPad and DU Men's Soccer scenario. Fall covers Modules 1 to 3 on the course
  datasets students already have in their workbooks: SummitGear, Highlands Ranch, Green Valley
  Commons.
- **Dropped.** Geometric and negative binomial (not in the Fall Module 2 method sheet), the soccer
  workbook, the Twitter survey and Monday-tickets bias items.
- **Added.** The fraud-flag base rate (tree of 10,000), independence from a contingency table, the
  normal and uniform, the standard error and the Central Limit Theorem, the proportion condition,
  sample size for a target margin, and the course rounding policy (two decimals and no leading
  zero for probabilities, money to the cent, critical values to three decimals).
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
(`SUMMITGEAR`, `SG_TABLE`, `HIGHLANDS`, `GREENVALLEY`) are constants above the question bank, so a
change to a scenario shows up in every cell that uses it.

Keep the rounding policy when you edit a number: `4_Library/method/rounding-policy.md`.

## License

Course materials in this repository are CC BY-NC-SA 4.0 and the code is MIT. See the repository
root.
