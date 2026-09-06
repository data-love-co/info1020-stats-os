---
name: demand-simulator
description: >
  Module 2 AI Block. Builds a demand-planning simulator: given an average arrival rate it names
  the distribution (Poisson), simulates arrivals per period, reports the probability of exceeding
  a capacity both exactly and by simulation, and lays out the staffing trade-off. Triggers on "run
  AI Block 2", "walk-ins per hour", "how many staff do we need", "simulate demand", "Poisson",
  "busy hour", "chance of more than 15".
---

# demand-simulator: Module 2 AI Block

The student has computed P(more than 15 walk-ins) = .19 by hand in tab 3 with POISSON.DIST. You
build the simulator, get the same number two ways, and lay out the staffing choice. They check you
against tab 3.

## Phase 0: get the situation from the student

Ask for, or confirm:

- **What arrives, per what period.** Course value: registration walk-ins, per hour.
- **The average rate.** Course value: 12.5 per hour.
- **The capacity to test.** Course value: 15 per hour (what the current desk can serve).

Then **name the distribution and say why, before computing**: counts of independent arrivals in
a fixed window with no upper limit is Poisson. Say what would make it wrong (arrivals that bunch,
a rate that changes across the day) and note the mean is the only parameter, sd = SQRT(12.5) =
3.54.

If the student instead describes a fixed number of trials with a yes-or-no outcome (15 students,
each enrolls with probability .80), the distribution is binomial; name it and switch. If they
describe a measurement (skier counts), it is the normal with the sample mean and sd; use
`MtHighlands_SkierCounts.csv` and `NORM.DIST`.

## Phase 1: exact answer

Compute the exact Poisson probabilities and show the Excel equivalent:

```
P(exactly 8)        = POISSON.DIST(8, 12.5, FALSE)      = .06
P(15 or fewer)      = POISSON.DIST(15, 12.5, TRUE)      = .81
P(more than 15)     = 1 - POISSON.DIST(15, 12.5, TRUE)  = .19
P(more than 17)     = 1 - POISSON.DIST(17, 12.5, TRUE)  = .08
P(more than 20)     = 1 - POISSON.DIST(20, 12.5, TRUE)  = .02
```

Watch the off-by-one: "more than 15" is the complement of "15 or fewer," not of "16 or fewer."

## Phase 2: simulate

Run at least 10,000 simulated hours (Python `random` or `numpy`, seeded so it is repeatable).
Report the simulated share over 15 next to the exact .19 and say they agree to two decimals. Show
the distribution as a short table (0 to 25 walk-ins) or a text histogram. Label the simulation as
**simulated**, per the workspace rules.

## Phase 3: the staffing trade-off

Do not pick the staffing level. Show the table and let the student choose:

| Staff for | Chance an hour exceeds it | Meaning |
|---|---|---|
| 13 (about the mean) | .37 | queue forms one hour in three |
| 15 | .19 | one hour in five |
| 17 | .08 | one hour in twelve |
| 20 | .02 | one hour in fifty |

Say what a manager sentence must contain: the level chosen, the risk accepted at that level, and
the assumption (Poisson at 12.5 per hour, checked against the actual rate on the first busy day).
Then stop.

## Phase 4: verify and cite

Call `util_verify_and_cite` with target **P(more than 15) = .19, sd = 3.54** and the classic error
to check: did the tool state the distribution before computing, and did it use the binomial with
an invented n? Write to `2_Outputs/.agents/M2/Demand-Simulator.md`.

## Guardrails

- Name the distribution and its parameter before any number.
- Exact and simulated must both appear; the simulation is labeled simulated.
- Two decimals, no leading zero.
- Never choose the staffing level for the student.
