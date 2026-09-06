# Module 1: Probability for business decisions

**In the lab:** Lab 1A and 1B: SummitGear Outfitters, 250 orders. COUNTIF and COUNTIFS for marginal, joint and conditional probabilities; the contingency table; independence; the fraud-flag base-rate tree.

Method sheet: `4_Library/method/m1-*.md`. Verification targets:
`4_Library/sample-data/README.md`, Module 1 section.

## AI Block 1

**You build:** A base-rate explainer. Given a base rate, a catch rate, and a false-alarm rate, it builds the tree of 10,000, computes P(fraud given flagged), and explains to a finance manager in plain language why a flagged order is usually not fraud.

**Inputs you give the tool:** The three rates from tab 4: 2% of orders are fraudulent, the detector catches 90% of fraud, and it flags 5% of legitimate orders. No data file needed.

**Data file:** none (three given rates) (in `4_Library/sample-data/`).

**Verify against:** P(fraud given flagged) = .27; 180 true flags, 490 false flags, 670 flags in all.

**The guardrail this block teaches:** Check every number in the explanation against tab 4. A tool that says "the detector is 90% accurate, so a flag is 90% likely to be fraud" has confused P(flag given fraud) with P(fraud given flag). That is the whole lesson.

## How to run it

- With an agent that can read this folder: say **"run AI Block 1"** (skill `base-rate-explainer`).
- With a chat tool: paste prompt 1 from `4_Library/portable-prompts/Portable-Prompts.md`
  and upload the data file.

Then fill `AI-Block-1-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
