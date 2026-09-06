# The four AI rules

These are the rules for every AI Block in INFO 1020, and they are the rules for the rest of a
career that will involve AI tools. They appear in the syllabus, on every module's AI Block slide,
and in the So-What tab of every workbook.

## 1. Verify

The tool can be confidently wrong. Every number it produces gets checked against the student's own
math before anyone believes it. In this course, "your own math" means the Excel workbook: the
student runs the course dataset through whatever the agent built and compares against the values
in their solved tabs. `4_Library/sample-data/README.md` lists what every dataset should produce.

If the build and the workbook disagree, the build is wrong until proven otherwise. The most common
reasons: the tool used z where the course uses t, it pooled variances where the course uses Welch,
it picked the tail after seeing the data, it ignored the expected-count condition, or it rounded
an intermediate value.

## 2. Cite

Name the tool, give an APA reference list entry for it, and say in one or two sentences what it
was used for. The citation goes in the So-What tab with the prompt and the output. Format:

> GitHub. (2026). *GitHub Copilot* [Large language model]. https://github.com/copilot
> Used to build a confidence-interval calculator and draft its interpretation sentence; all
> numbers verified against tab 3 of my workbook.

Other tools: `Anthropic. (2026). Claude [Large language model]. https://claude.ai`,
`OpenAI. (2026). ChatGPT [Large language model]. https://chatgpt.com`,
`Google. (2026). Gemini [Large language model]. https://gemini.google.com`.

## 3. Add value

The student scopes the problem and interprets the result by hand. The AI only builds. Concretely:
the student states which numbers, which question, which distribution or test, and which tail,
before the agent writes a line of code. Afterward, the student writes the manager sentence in
their own words. An agent may list what the sentence must contain. It may not write it.

## 4. Never on quizzes or exams

No AI tool, in any capacity, on the module quizzes, the midterm, or the final. This is the course
rule and it is the Honor Code. An agent that recognizes a quiz question (ten items, numeric
answers, a Canvas due date, "question 4 of 10") declines in one sentence and points to the module
workbook and notes guide.

## What an agent does when a student asks it to break rule 3 or 4

Say no in one sentence, without a lecture, and offer the thing that is allowed: explain the
concept, walk through the method sheet, show what a manager sentence must contain, or check the
student's own sentence for the classic errors (probability language on a confidence interval,
"proves" on a hypothesis test, a p-value with no effect size).
