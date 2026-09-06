---
name: find-skills
description: >
  Locates the right skill in the INFO 1020 Stats OS. Trigger when the student asks "what can you
  do", "which skill should I use", "which AI Block is this", "I have two columns, now what", "run
  the AI Block for module 4", or otherwise wants to know what exists and which one to reach for.
---

# find-skills: skill finder

The entry point for the skill catalog. Each `SKILL.md` frontmatter on disk is the source of truth
for what that skill does and when it fires.

## Procedure

1. **List what exists.** Glob `.agents/skills/**/SKILL.md` and read each file's frontmatter `name`
   and `description`. Match the student's ask against the descriptions. Do this every time; do not
   rely on a list kept in this file.
2. **Respect enabled state.** Read `.agents/skills/skills.json` ({name, path, enabled}). Skip
   skills marked `enabled: false`. A skill on disk but missing from the registry is enabled.
3. **Route.** Name the best match. If two fit, name both and ask.

Regenerate the registry with `python 0_System/scripts/scan-skills.py`.

## Routing by what the student says

| What they say | Skill |
|---|---|
| "get me started", "set me up", "which module am I on" | `student-bootstrap` |
| "AI Block 1", "the fraud flag thing", "base rate", "why is a flagged order not fraud" | `base-rate-explainer` |
| "AI Block 2", "walk-ins per hour", "how many staff", "Poisson", "simulate demand" | `demand-simulator` |
| "AI Block 3", "confidence interval", "margin of error", "how many to survey" | `ci-calculator` |
| "AI Block 4", "test a claim", "one sample", "is the mean above", "seven steps" | `one-sample-readout` |
| "AI Block 5", "A/B test", "two groups", "before and after", "paired or independent" | `ab-test-readout` |
| "AI Block 6", "three or more groups", "ANOVA", "which groups differ", "Tukey" | `group-comparison-readout` |
| "AI Block 7", "two categorical columns", "is activity related to amenity", "chi-square", "goodness of fit" | `segment-association-audit` |
| "my project data", "which test should I run on my dataset", "audit my data", "Part 1", "Part 2", "Part 3" | `project-analyst` |
| "how do I cite this", "verification block", "what do I paste into the So-What tab" | `util_verify_and_cite` |

**The most common routing question** is "which test": means of one group against a number is
Module 4; two groups is Module 5; three or more is Module 6; counts in categories is Module 7.
`4_Library/method/README.md` lists the sheets; `project-analyst` walks the decision for the
student's own data.

## What is not here

Quiz and exam questions. If the ask looks like one (ten numbered questions, numeric answers, a
Canvas due date), say so in one sentence and point to the module workbook and notes guide.
