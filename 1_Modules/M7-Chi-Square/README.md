# Module 7: Chi-square: goodness of fit and independence

**In the lab:** Lab 7A: one 200-piece bag of M&Ms against the published mix. Lab 7B: Bob Tinglestad, 73 ski-resort guests, activity by amenity, from raw rows to a tested table.

Method sheet: `4_Library/method/m7-*.md`. Verification targets:
`4_Library/sample-data/README.md`, Module 7 section.

## AI Block 7

**You build:** A segment-association audit. Given two categorical columns, one row per customer, it builds the table, checks expected counts, combines categories on business meaning if it must and says how, runs the test, names the cell that drives it, and lists what the manager sentence must contain.

**Inputs you give the tool:** SkiResort_Survey.csv, all 73 raw rows, both columns.

**Data file:** SkiResort_Survey.csv (in `4_Library/sample-data/`).

**Verify against:** 5 x 5 fails the expected-count condition (20 cells under 5). Combined 3 x 2: chi-square = 9.42, df = 2, p = .009; snowboarders and wellness expected 9.32, observed 4.

**The guardrail this block teaches:** Did it check expected counts before testing, or run the 5 x 5 anyway? If it combined, did it explain the grouping in business terms? Does its chi-square on the 3 x 2 come out at 9.42?

## How to run it

- With an agent that can read this folder: say **"run AI Block 7"** (skill `segment-association-audit`).
- With a chat tool: paste prompt 7 from `4_Library/portable-prompts/Portable-Prompts.md`
  and upload the data file.

Then fill `AI-Block-7-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
