# Portable prompts: the seven AI Blocks for any chat tool

Paste-ready versions of every AI Block for a tool that cannot read this folder: Copilot on
github.com, Claude on the web, ChatGPT, Gemini. Each prompt is self-contained. No file paths, no
skill names.

**How to use these**

1. Copy the prompt for your module into the chat.
2. Replace anything in `[SQUARE BRACKETS]` with your own words. The brackets are where you
   scope the problem by hand; that is the "add value" rule.
3. Upload or paste the data file when the prompt says so. The course files are in
   `4_Library/sample-data/`.
4. Compare the output with your workbook using the targets in
   `4_Library/sample-data/README.md`.
5. Fill the paste template in `1_Modules/<module>/` and put it in the So-What tab.
6. Write the manager sentence yourself.

The rounding and "do not write my recommendation" lines inside these prompts are the point. Do
not trim them.

---

## Rounding block (included in every prompt)

```
Round like this, because I am graded on it: probabilities, proportions and test
statistics to two decimals with no leading zero (.34, t = 2.53); p-values to three
decimals with no leading zero (p = .038), and p < .001 below that; money to the cent;
critical values to three decimals. Show each value unrounded once, then rounded.
```

---

## 1. Base-rate explainer (Module 1)

No file needed.

```
I am a business statistics student. Build me a base-rate explainer and check it
against my numbers.

The situation: [DESCRIBE THE FLAG OR TEST IN ONE SENTENCE, e.g. "an online
retailer's fraud detector flags orders for review"].
Base rate: [2]% of all cases actually have the condition.
Catch rate: the detector flags [90]% of true cases.
False-alarm rate: it also flags [5]% of cases that do not have the condition.

Do this in order:
1. Say back the three rates in a plain sentence so I can confirm them.
2. Build a tree of 10,000 cases: how many have the condition, how many of those
   are flagged, how many do not, how many of those are flagged anyway. Show every
   count. Do not round the counts.
3. Compute P(condition given flagged) as a fraction of the flagged count, and
   P(condition given not flagged).
4. Explain the result to a finance manager in four to six sentences. Lead with
   the counts, not the probability. Say in one sentence why a rare condition
   makes most flags wrong. Say what the number is NOT: it is not the detector's
   accuracy, and it is not the share of the time the detector is wrong.
5. Give me a small calculator (a table or a short function) that takes the three
   rates and returns the tree and P(condition given flagged). Show it on two
   other base rates so I can see the base rate move the answer.
6. List what my one-line recommendation to the manager must contain. Do not
   write the recommendation; I write it.

[ROUNDING BLOCK]
```

Verify: P(fraud given flagged) = .27, 180 true flags, 490 false flags, 670 flags in all. The
classic error: a tool that says "90% accurate, so a flag is 90% likely fraud."

---

## 2. Demand-planning simulator (Module 2)

No file needed for the walk-ins. Upload the skier-counts file only for the optional normal run.

```
I am a business statistics student. Build me a demand-planning simulator and check
it against my numbers.

The situation: [DESCRIBE WHAT ARRIVES AND PER WHAT PERIOD, e.g. "walk-ins at a
university registration desk, per hour"].
Average rate: [12.5] per [hour].
Capacity I want to test: [15] per [hour].

Do this in order:
1. Before computing anything, name the probability distribution that fits this
   situation and say why in two sentences. Say what would make it the wrong
   choice. State its parameter(s) and its standard deviation.
2. Compute exactly: P(exactly 8), P(15 or fewer), P(more than 15), P(more than
   17), P(more than 20). Next to each, write the Excel function that gives the
   same number (POISSON.DIST or BINOM.DIST with TRUE or FALSE).
3. Simulate at least 10,000 periods with a fixed random seed. Report the simulated
   share over the capacity next to the exact value and say whether they agree.
   Label the simulation as simulated.
4. Show a staffing trade-off table: for capacity levels [13, 15, 17, 20], the
   chance a period exceeds it and what that means in plain words ("a queue forms
   one hour in five").
5. List what my staffing recommendation must contain. Do not choose the staffing
   level and do not write the recommendation; I do.

[ROUNDING BLOCK]
```

Verify: P(more than 15) = .19, sd = 3.54. The classic error: the binomial with an invented n, or
"more than 15" computed as 1 minus P(16 or fewer).

---

## 3. Confidence-interval calculator (Module 3)

Upload `GreenValleyCommons_Residents.csv`, or give the summary numbers.

```
I am a business statistics student. Build me a confidence-interval calculator and
check it against my numbers.

The parameter I am estimating, in words: [THE TRUE MEAN MONTHLY INCOME OF
RESIDENTS OF GREEN VALLEY COMMONS].
Data: the attached file, column [Monthly income ($)]. (Or: n = [20], mean =
[3398.90], sd = [351.38].)
Confidence level: [95]%.
Also a proportion: [8] of [20] residents are [male].

Do this in order:
1. For the mean: say whether you are using t or z and why, before any number.
   Then show n, mean, sd, standard error, the critical value with its degrees of
   freedom, the margin of error, and the interval. Next to each, the Excel
   function (STDEV.S, T.INV.2T, CONFIDENCE.T). Show the 90% interval too.
2. For the proportion: BEFORE computing, check that n times p-hat and n times
   (1 minus p-hat) are both at least 10 and print the check. If it fails, do not
   print an interval; say "not reportable at this n" and go to step 3.
3. Sample size: how many would I need for a margin of error of [$100] on the mean
   at 95%? Show the formula and round UP.
4. Write exactly one interpretation sentence for the mean interval, in the form
   "We are 95% confident that the true [parameter] is between [low] and [high],
   based on a sample of [n]." Then show me the two wrong sentences people write
   (one about individuals, one about probability) and say why each is wrong.
5. Give me the calculator as a small function or a four-input table with the
   condition check built in.
6. List what my one-line recommendation must contain. Do not write it.

[ROUNDING BLOCK]
```

Verify: $3,234.45 to $3,563.35 (t* = 2.093, SE $78.57); the gender proportion interval not
reportable at n = 20; 48 residents for a $100 margin. The classic errors: z for the mean, "95% of
residents earn between," an interval reported despite a failed condition.

---

## 4. One-sample hypothesis-test readout (Module 4)

Upload `DeniceToney_Balances.csv`, or give the summary numbers.

```
I am a business statistics student. Build me a hypothesis-test readout for one
sample and check it against my numbers. Do NOT look at the data until you have
recorded the tail in step 1.

1. Record these before opening the data:
   Parameter in words: [THE TRUE MEAN BALANCE OF MID-TIER ACCOUNTS].
   Claimed value (H0): [2500].
   Tail, chosen from the business question: [RIGHT-TAILED, because the manager
   funds the promotion only if the mean is ABOVE 2500].
   Alpha: [.05].
2. Now the data: the attached file, column [Account balance ($)]. (Or: n = [16],
   mean = [2650.68], sd = [317.11].)
3. Write out all seven steps: parameter; H0; Ha with the tail; the statistic and
   its degrees of freedom; alpha, the critical value, and a description of the
   rejection picture; the computed statistic and p-value; the decision and its
   interpretation in business language. Next to each computed value, the Excel
   function (AVERAGE, STDEV.S, T.INV, T.DIST.RT, T.DIST.2T).
4. Then run the two-tailed version against [2800] and show that the two-tailed p
   is double the one-tailed p for the same statistic, and why.
5. Give the 95% confidence interval for the mean and explain in two sentences why
   the claimed value can sit inside a two-sided interval while a one-sided test
   still rejects it.
6. Say what the result does NOT prove. Never write "accept H0" and never write
   "proves."
7. List what my one-line recommendation must contain. Do not write it.

[ROUNDING BLOCK]
```

Verify: t = 1.90, p = .038, t* = 1.753, reject; two-tailed against $2,800: t = -1.88, p = .079.
The classic errors: tail picked after the data, "accept H0," "proves."

---

## 5. A/B test readout (Module 5)

Upload `Streamly_ABTest_CX.csv`. Then, in a new chat, `Multitasking_Example14.csv` without the
word "paired" anywhere in your message.

```
I am a business statistics student. Build me an A/B test readout and check it
against my numbers.

Data: the attached file. Group column: [Variant]. Score column: [CX score
(1 to 10)]. (For a file with two score columns and no group column, use the two
columns.)
The business question: [IS THE NEW ONBOARDING FLOW BETTER OR WORSE THAN THE
CURRENT ONE] (so the tail is [TWO-TAILED]). Alpha [.05].
My practical threshold: the difference would have to be at least [0.5] points to
be worth shipping.

Do this in order:
1. Step zero: decide whether the two groups are paired (the same unit measured
   twice, linked row by row) or independent (different units), and give the
   evidence for your decision from the data itself: the row identifier, the
   column names, and whether the differences are much less variable than either
   column. If you cannot tell, ask me; do not guess.
2. State the parameter in words, H0, Ha with the tail, alpha.
3. Run the right test. For independent groups use the Welch t-test (do not pool
   variances) and report the p-value two ways: with the conservative degrees of
   freedom (smaller n minus 1) and with the Welch degrees of freedom. For paired
   data, analyze the column of differences. Show every intermediate value and
   the Excel function next to it (T.TEST with type 3 or type 1, T.INV.2T).
4. Report the difference, its standard error, the statistic, the degrees of
   freedom, the p-value, and the 95% confidence interval for the difference,
   together.
5. Place my practical threshold against the interval and tell me which of these
   applies: whole interval above the threshold (ship); interval straddles it
   (iterate or extend); whole interval below (hold); interval includes zero and
   is narrow (hold, no meaningful effect); interval includes zero and is wide
   (inconclusive).
6. List what my ship-or-hold recommendation must contain. Do not write it.

[ROUNDING BLOCK]
```

Verify: Streamly t = 2.53, p = .016 conservative, .014 Welch, 95% CI .16 to 1.44. Multitasking:
paired, t = 12.52, p < .001. The classic errors: pooled by default, pairing missed, p without the
interval.

---

## 6. Group-comparison readout (Module 6)

Upload `CareerServices_Salaries.csv`. Then, in a new chat, `Clinic_WaitTimes.csv`.

```
I am a business statistics student. Build me a group-comparison readout and check
it against my numbers.

Data: the attached file, one column per group: [OR Analyst, Accountant, Computer
Analyst, Financial Specialist]. What is measured: [STARTING SALARY IN DOLLARS].
Alpha [.05].

Do this in order, and do NOT run pairwise t-tests at any point:
1. State H0 (all group means equal) and Ha (at least one differs). If I had asked
   for pairwise t-tests instead, tell me the family-wise error rate for six tests
   at .05 and why ANOVA comes first.
2. Report n, mean, and standard deviation per group and the grand mean. Then the
   spread check: largest sd divided by smallest sd, and say whether it is under
   the rule of thumb of 2. If it is borderline, say so and proceed; do not hide
   it.
3. Build the one-way ANOVA table by hand from the group summaries: SS between and
   within, degrees of freedom, mean squares, F. Give the critical F and the
   p-value with their Excel functions (F.INV.RT, F.DIST.RT). Decide.
4. Only if H0 is rejected: run Tukey HSD. Show q, HSD, and every pair's difference
   with whether it exceeds HSD. Turn the pairs into tiers.
5. If H0 is NOT rejected: stop. Write "no difference detected," explain in two
   sentences why that is not the same as "no difference," and do not run any
   follow-up test.
6. Give me the readout as a reusable function or table that takes any number of
   columns.
7. List what my recommendation must contain. Do not write it.

[ROUNDING BLOCK]
```

Verify: salaries F = 76.51, p < .001, HSD $3,344.70, every pair differs except OR Analyst vs
Computer Analyst; clinics F = .71, p = .494, no follow-up. The classic errors: six t-tests, Tukey
after a failed F, the spread check hidden.

---

## 7. Segment-association audit (Module 7)

Upload `SkiResort_Survey.csv`, all 73 raw rows.

```
I am a business statistics student. Build me a segment-association audit and
check it against my numbers.

Data: the attached file, one row per guest. Column A: [Primary activity]. Column
B: [Amenity used most]. The business question: [IS THE AMENITY A GUEST USES MOST
RELATED TO THE ACTIVITY THEY CAME FOR]. Alpha [.05].

Do this in order:
1. Say why this is a question about counts (chi-square), not about means (t or
   F). State H0 (independent) and Ha (related).
2. Build the table of counts from the raw rows, with row and column totals. Show
   the Excel function that does one cell (COUNTIFS).
3. Compute the expected count for every cell (row total times column total
   divided by n) to two decimals.
4. BEFORE any test, check that every expected count is at least 5. Print how many
   cells fail. If any fail, do not compute chi-square on this table.
5. If the check failed, propose ONE way to combine categories that a manager
   would recognize, give the business reason for each merge, and say explicitly
   that you did not try several groupings and keep the one with the smallest p.
   Rebuild the table, recompute expected counts, and reprint the check.
6. Run the chi-square test of independence on the table that passes: the
   contribution of every cell, the statistic, the degrees of freedom, the
   critical value, and the p-value, with the Excel functions (CHISQ.INV.RT,
   CHISQ.DIST.RT, CHISQ.TEST). Decide.
7. Name the cell that drives the result, in business terms, with its observed
   and expected counts. Give one caution about the sample.
8. List what my one-line recommendation must contain. Do not write it.

[ROUNDING BLOCK]
```

Verify: the 5 x 5 fails (20 cells under 5); combined 3 x 2 (on skis / snowboard / shop by
wellness / not wellness): chi-square = 9.42, df = 2, p = .009; snowboarders and wellness expected
9.32, observed 4. The classic errors: testing the 5 x 5 anyway, combining without a reason,
combining to chase p.

---

## The citation, for every block

```
GitHub. (2026). GitHub Copilot [Large language model]. https://github.com/copilot
Anthropic. (2026). Claude [Large language model]. https://claude.ai
OpenAI. (2026). ChatGPT [Large language model]. https://chatgpt.com
Google. (2026). Gemini [Large language model]. https://gemini.google.com
```

Use the line for the tool you used, then one or two sentences on what you used it for and what
you verified by hand.
