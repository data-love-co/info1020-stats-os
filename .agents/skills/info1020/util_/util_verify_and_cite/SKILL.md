---
name: util_verify_and_cite
description: >
  Produces the verification checklist and the citation block a student pastes into the So-What tab
  after an AI Block. Every module skill calls this at the end of a run. Also triggers directly on
  "how do I cite this", "what do I paste into the workbook", "verification block", "did it get it
  right".
---

# util_verify_and_cite: the last step of every AI Block

You are handed what the skill built and what it computed. You produce two things and hand the
student one paste-ready block. You do not write the manager sentence.

## Step 1: verification checklist

Read the verification target for the module from `4_Library/sample-data/README.md` (or the target
the calling skill passes). Then fill this in with the actual values, one line per item:

```
MY VERIFICATION
Target from my workbook: <the course value, rounded per policy>
Tool's value: <what the build produced, rounded per policy>
Match? <yes, or no and why: t vs z / tail chosen after the data / pooled vs Welch /
        expected counts not checked / rounded an intermediate value / wrong denominator>
Assumption the tool stated: <the distribution or test it named, and when it named it>
One classic error it did or did not make: <one sentence; see the module's guardrail>
```

If the build and the target disagree, say plainly that the build is wrong until proven otherwise,
name the most likely cause from the module's classic-mistakes list, and offer to fix the build.
Do not adjust the target to match the build.

## Step 2: citation block

APA reference list entry for the tool, then one or two sentences on what it was used for. Ask
which tool they are on if the session does not make it obvious.

```
CITATION
GitHub. (2026). GitHub Copilot [Large language model]. https://github.com/copilot
Anthropic. (2026). Claude [Large language model]. https://claude.ai
OpenAI. (2026). ChatGPT [Large language model]. https://chatgpt.com
Google. (2026). Gemini [Large language model]. https://gemini.google.com

Used to <what the skill built, in the student's words if they gave them>. All numbers verified
against tab <n> of my workbook.
```

Use only the line for the tool actually used.

## Step 3: what the manager sentence must contain

List the two to four items from `4_Library/method/manager-sentence.md` for this module: the
decision verb, the evidence in business units, the honest confidence, and what it does not prove.
Then stop. The student writes the sentence. If they paste one back and ask you to check it, check
it against the classic-errors list on that sheet and say what to fix, not what to write.

## Output

Show the two blocks in chat, and write them to `2_Outputs/.agents/M<n>/Verify-and-Cite.md` so the
student can copy from a file if the chat window is awkward.
