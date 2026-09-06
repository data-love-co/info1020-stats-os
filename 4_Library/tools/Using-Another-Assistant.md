# Which tool you need

The workspace is plain text, so it is not tied to one company's product. What changes between
tools is how much is automatic, not whether you can do the AI Blocks. You will never be asked to
pay for a tool in this course.

## Two tiers

**Tier 1: a chat window.** Copilot on github.com, Claude on the web, ChatGPT, Gemini. You paste
the prompt from `4_Library/portable-prompts/Portable-Prompts.md`, upload or paste the data file,
and the tool computes and explains. Every AI Block works this way. You carry the verification and
citation by hand using the module's paste template.

**Tier 2: an agent that can read this folder.** Claude Code (CLI, desktop, or VS Code extension)
or GitHub Copilot agent mode in VS Code. You say "run AI Block 3" and the skill does the full
routine: builds, runs the course data, writes the output to `2_Outputs/`, and hands you the
verification and citation block. The project skill also needs this tier, because it reads your
data file from the folder.

| If you have | Tier | Cost | Notes |
|---|---|---|---|
| GitHub Copilot Student (verified through GitHub Education) | 1 and 2 | Free | Unlimited code completions; a monthly allowance of chat credits. Agent mode in VS Code reads `AGENTS.md`. See `Get-GitHub-Copilot-Free.md` |
| GitHub Copilot Free (anyone) | 1 and 2 | Free | Smaller monthly allowance; enough for the AI Blocks if you are not wasteful |
| Claude (free tier) | 1 | Free | Paste prompts; upload the CSV. Cannot read the folder |
| Claude Code (paid plan or API) | 2 | Paid | The smoothest Tier 2 experience; not required |
| ChatGPT (free tier) | 1 | Free | Paste prompts; upload the CSV |
| Gemini (free tier) | 1 | Free | Paste prompts; upload the CSV |

## Making a chat allowance last

Both free Copilot plans meter chat. Four habits: one complete question per message, a new chat for
each new topic, "Ask" mode rather than agent mode for anything small, and if chat pauses for the
month, switch to another free tool for that block. Code completions never use credits.

## What every tool must be told

Whatever the tool, the AI Block prompt gives it four things, because the student decides them:
the numbers or the file, the question in words, the distribution or test and the tail, and the
rounding policy. A tool that had to guess any of those has been given a bad prompt, not a hard
problem.
