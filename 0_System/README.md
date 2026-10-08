# 0_System: the engine

| File | What it does |
|---|---|
| `bootstrap/setup.mjs` | Creates `CLAUDE.md` from `AGENTS.md` (symlink on Mac and Linux, copy on Windows) and checks Node, git, and Python. Safe to re-run. `node 0_System/bootstrap/setup.mjs` |
| `scripts/base-rate-simulator.py` | Builds the Module 1 base-rate tree, reports P(condition given flagged) and P(condition given not flagged), and can compare scenarios side by side. `python 0_System/scripts/base-rate-simulator.py` |
| `scripts/scan-skills.py` | Rebuilds `.agents/skills/skills.json` from the SKILL.md files on disk. `python 0_System/scripts/scan-skills.py` |
| `scripts/check-values.py` | Recomputes every verification target in `4_Library/sample-data/README.md` from the CSVs and reports drift. `python 0_System/scripts/check-values.py` |

Nothing here needs an API key. Python 3 is used by the three scripts and by the skills when they
compute; Node is used only by `setup.mjs`.
