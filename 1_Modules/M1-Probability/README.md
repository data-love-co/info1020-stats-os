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
- With the script-based simulator in this repo:
  `python 0_System/scripts/base-rate-simulator.py`

Then fill `AI-Block-1-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## Script-based simulator

The simulator in `0_System/scripts/base-rate-simulator.py` gives instructors a reusable calculator
for the tree of 10,000 and the two posterior probabilities.

### Default fraud-detector example

`python 0_System/scripts/base-rate-simulator.py`

This runs the course example by default: 2% base rate, 90% catch rate, 5% false-alarm rate. The
output shows 180 true flags, 490 false flags, 670 flags in all, `P(condition given flagged) = .27`,
and `P(condition given not flagged) = .00`, with each posterior shown once unrounded and then
rounded to the course format.

```text
Decision tree for 10,000 cases
- Cases with the condition: 200
  - Flagged: 180
  - Not flagged: 20
- Cases without the condition: 9,800
  - Flagged anyway: 490
  - Not flagged: 9,310
- Total flagged: 670

P(condition given flagged) = 180 / 670 = .2686567164179104477611940299 -> .27
P(condition given not flagged) = 20 / 9,330 = .002143622722400857449088960343 -> .00
```

### Custom rates

`python 0_System/scripts/base-rate-simulator.py --base-rate 3% --catch-rate 85% --false-alarm-rate 4%`

The script accepts decimal rates such as `.03` or percentage strings such as `3%`. Counts are shown
as raw counts, with no rounding.

### Side-by-side comparison

```text
python 0_System/scripts/base-rate-simulator.py \
  --compare "Higher base rate" 10% 90% 5% \
  --compare "Lower base rate" .5% 90% 5%
```

This prints the main scenario plus a comparison table so an instructor can show how the posterior
moves when the base rate changes. The teaching point is the same as in class: when the condition is
rare, even a modest false-alarm rate on the much larger no-condition group can make most flags
wrong.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
