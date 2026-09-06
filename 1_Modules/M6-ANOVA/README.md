# Module 6: ANOVA: comparing several groups

**In the lab:** Lab 6A: DU Career Services, four career paths, 20 salaries each. Lab 6B: Atlas Family Health, wait times in three states, and the answer is no.

Method sheet: `4_Library/method/m6-*.md`. Verification targets:
`4_Library/sample-data/README.md`, Module 6 section.

## AI Block 6

**You build:** A group-comparison readout. Given three or more columns, it returns k, the group means, the spread check, the ANOVA table, F, p, whether a follow-up is warranted, which pairs differ by Tukey if so, and what a recommendation must contain.

**Inputs you give the tool:** CareerServices_Salaries.csv. Then Clinic_WaitTimes.csv.

**Data file:** CareerServices_Salaries.csv, Clinic_WaitTimes.csv (in `4_Library/sample-data/`).

**Verify against:** Salaries: F = 76.51, p < .001, HSD $3,344.70, every pair differs except OR Analyst vs Computer Analyst. Clinics: F = .71, p = .494, no follow-up.

**The guardrail this block teaches:** Did it run one ANOVA or six t-tests? Did it run Tukey on the salaries and refuse to on the clinics? Did it report the spread ratio (2.19) instead of hiding it?

## How to run it

- With an agent that can read this folder: say **"run AI Block 6"** (skill `group-comparison-readout`).
- With a chat tool: paste prompt 6 from `4_Library/portable-prompts/Portable-Prompts.md`
  and upload the data file.

Then fill `AI-Block-6-Template.md` and paste it into the So-What tab. The manager sentence
is yours to write; the tool does not write it.

## The four rules

Verify. Cite. Add value. Never on quizzes or exams.
