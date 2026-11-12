# INFO 1020 Final Review Jeopardy, Fall 2026

A single-file, browser-based Jeopardy game for reviewing Modules 4 to 7 of **INFO 1020: Analytics
II** before the final. Five categories, twenty-five questions, one Daily Double, a Final Jeopardy
tie-break, team scoring for six teams. No build step, no dependencies, no tracking. It runs
offline once loaded.

**Play it:** https://data-love-co.github.io/info1020-stats-os/final-review/ or open `index.html`
in any browser.

This is the Fall 2026 rebuild of the
[Spring 2026 final game](https://github.com/dataloveco/info1020-final-review-jeopardy). The game
shell is the midterm game's. The question bank is new.

## Interpretation first, one ask per cell

The final is about choosing the right test and saying what the result means, so the board leans
that way:

- **$100 to $400 cells are multiple choice**, in the style of the Canvas quiz. Every team holds up
  A, B, C or D when the clock ends, and the cell is done in about two minutes.
- **Four $500 cells use Excel**, and every number a team needs is on the screen. There is **no
  data file to open**: one laptop per team with a blank workbook is enough.
- **The fifth $500 is the Daily Double**: a "What?", "So What?", "Now What?" memo in the shape of the exam
  essays.

The scenario is **Fourteener Fitness**, a fictional Colorado gym chain with 4 locations (Golden,
Boulder, Fort Collins, Colorado Springs). Every computed answer is net new: none is a number the
labs or the midterm game produced, and `check-game-values.py` enforces that.

Every cell asks **one thing**, and every answer gives the result, the computation, and the Excel
function. Nothing else. The scoring notes and the talking points for the room are in the
run-of-show, not on screen.

Every number in the game is recomputed by `check-game-values.py`, which also checks that the
Excel output tables on screen agree with their own inputs:

```
python docs/final-review/check-game-values.py
```

## In the classroom

1. Open the game and press **F11** (Windows) or **Ctrl+Cmd+F** (Mac) for full screen.
2. The six teams come pre-named from The Hitchhiker's Guide to the Galaxy: Don't Panic,
   Improbability Drive, Deep Thought, The Answer Is 42, Mostly Harmless, and
   Paranoid Androids. Click a name in the right-hand panel to change it.
3. Each team needs one laptop with Excel open to a **blank workbook**. No CSV is needed: the
   Excel cells put every number on the screen. Lab workbooks stay closed.
4. Click a dollar cell to show a question. A countdown starts in the top bar: 1 minute for
   $100, 1.5 for $200, 2 minutes for $300 and $400, and 4 minutes for $500. The four cells that
   need Excel get 2 more minutes (6 in all), and the Daily Double memo also gets 6 minutes. These
   are double the original plan, set for the pace of this section.
   **Pause** and **+30s** sit next to it. **Every team** works the question within the limit;
   nobody buzzes in.
5. **R** or the button reveals the answer and stops the clock. A row of team chips appears under
   the answer: click each team that got it right and the cell value is added (click again to
   undo). A wrong answer costs nothing, so every team has a reason to try. The +/− buttons in the
   side panel still work for corrections. **Esc** returns to the board and marks the cell played.
   A played cell stays dark with a faint dollar value, and clicking it opens the question again.
   Awards from the first time stay on the scores, so reopening never takes points away; use the
   +/− buttons if a reopened cell needs a correction.
6. The **$500 cell in "So What? Now What?"** is the Daily Double, the one cell only the picking team
   answers. The game asks for that team and their wager, then shows **Award wager** and **Deduct
   wager** buttons.
7. Scores and played cells are saved in the browser, so an accidental refresh does not lose the
   game. The final game saves under its own key, so it never loads the midterm's scores.
   **Reset Game** clears everything. Press it before class if you clicked through the board
   while preparing, since those clicks are saved in your browser too.
8. **Final Jeopardy** (the ★ button in the banner) is the tie-breaker. It pre-selects the teams
   tied for the lead, or everyone if there is no tie, and you can change who plays. Each playing
   team wagers up to its score, or up to $500 if its score is below $500, before the question
   appears. A 2-minute clock runs while teams write their answer on paper. Reveal the answer,
   then mark each team Correct or Wrong and the wager is added or subtracted. **R** reveals,
   **Esc** returns to the board.

The instructor's timing, the full answer key with scoring notes, the tie-break rule, and the
wrap-up reminders are in `Run-of-Show-and-Answer-Key.md`.

## Coverage

| Category | Module | What it tests |
|---|---|---|
| Pick Your Test | M4 to M7 | Step zero: paired or independent, ANOVA for several means, goodness of fit for one categorical variable; a two-sample p-value in Excel |
| Reject or Not? | M4, M5 | Reading Excel t-test output, the tail that matches the question, what a p-value means, a 95% interval for a difference |
| ANOVA-thing Goes | M6 | The alternative hypothesis, what a significant F does and does not say, Tukey as the next step, reading a Tukey result; an ANOVA p-value from sums of squares |
| Chi Another Day | M7 | Degrees of freedom, expected counts, combining categories when an expected count is under 5, failing to reject; a goodness-of-fit chi-square in Excel |
| So What? Now What? | M4 to M7 | Failing to reject is not proof, Type II error, significance versus practical size, the action the evidence supports; the Daily Double memo |

Answers by cell. These are the game's own verification targets, not the lab's.

| Cell | Answer |
|---|---|
| Pick Your Test $100 to $400 | C paired t; D two-sample t; C one-way ANOVA; D goodness of fit |
| Pick Your Test $500 | p-value = .029 (SE $3.88, t = 2.24, df 49) |
| Reject or Not? $100 to $400 | C p-value < .001; D fail to reject, two-tail p .068; A contains 0; C rare if H0 is true |
| Reject or Not? $500 | -0.13 to 3.53 visits (t* 1.987, margin 1.83) |
| ANOVA-thing Goes $100 to $400 | C at least 1 differs; D not all the same mean; C Tukey HSD; A Colorado Springs is the low one |
| ANOVA-thing Goes $500 | p-value = .096 (MSTr 920, MSE 360, F = 2.56) |
| Chi Another Day $100 to $400 | B 3; 160.00 (write the number); C combine; D not shown to differ (critical 7.815) |
| Chi Another Day $500 | chi-square = 11.22 (expected 80, 60, 40, 20) |
| So What? Now What? $100 to $400 | A no evidence; C Type II; D significant but may be too small; B investigate Colorado Springs |
| So What? Now What? $500 | Daily Double memo, scored on 4 parts |
| Final Jeopardy | Margin of error $7.79 on the interval $0.91 to $16.49 |

## Course conventions the game follows

The Course Reference Guide is the permitted aid on the final, so the game uses its wording where
it differs from the repo's method sheets: MSTr and MSE for the ANOVA mean squares, and Welch df
rounded down in the Excel output. Where a question sets the convention
itself (df = 49 on the signup-page cell), the question wins and the answer says so.

## Editing the questions

All content is in the `QUESTIONS` object inside `index.html`. Each entry is keyed
`"categoryIndex-valueIndex"` (both 0-based) with `q` and `a` HTML strings. Multiple-choice options
use the `options(a, b, c, d)` helper, which prints them as A to D. Add `dailyDouble: true` to make
any cell the Daily Double, `excel: true` to give it the extra Excel time on the clock, and
`seconds: 360` to set a cell's clock directly. Category names are in `CATEGORIES`. The shared
scenario card and tables (`GYM`, `VISITS_OUTPUT`, `SATISFACTION`, `BOOKINGS`) are constants above
the question bank, so a change shows up in every cell that uses it. The time limits are in
`TIME_LIMITS` and `EXCEL_EXTRA`.

The Final Jeopardy question is the `FINAL` object just above the keyboard handler: `category`,
`q`, `a` (the short answer), and `explain`. The shipped question asks for the margin of error
($7.79), chosen because the written answer is one checkable number. A spare is in the
run-of-show.

When you change a number, add or update its line in `check-game-values.py` and run it. Keep the
rounding policy: `4_Library/method/rounding-policy.md`.

## License

Course materials in this repository are CC BY-NC-SA 4.0 and the code is MIT. See the repository
root.
