#!/usr/bin/env python3
"""
check-values.py: recompute the verification targets in 4_Library/sample-data/README.md from the
CSVs and report any drift.

Run from the repo root:
    python 0_System/scripts/check-values.py

Standard library only for the statistics that need no distribution tables. p-values and critical
values use scipy when it is installed and are skipped (not failed) when it is not.
"""
import csv, math, os, statistics as st, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, "4_Library", "sample-data")
try:
    from scipy import stats as sps
except ImportError:
    sps = None

fails = []
def check(label, got, want, places=2):
    ok = round(got + 1e-12, places) == want
    print(f"{'ok ' if ok else 'XX '} {label}: got {round(got, places)} want {want}")
    if not ok:
        fails.append(label)

def rows(name):
    with open(os.path.join(D, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ---- Module 1: SummitGear
sg = rows("SummitGear_Data.csv"); n = len(sg)
mem = [r["Rewards Member"] == "Yes" for r in sg]
over = [float(r["Order Total ($)"]) > 100 for r in sg]
fem = [r["Gender"] == "Female" for r in sg]
check("M1 P(member)", sum(mem) / n, .34)
check("M1 P(over $100)", sum(over) / n, .49)
check("M1 P(member and over)", sum(m and o for m, o in zip(mem, over)) / n, .26)
check("M1 P(member or over)", sum(m or o for m, o in zip(mem, over)) / n, .56)
check("M1 P(over given member)", sum(m and o for m, o in zip(mem, over)) / sum(mem), .78)
check("M1 P(member given over)", sum(m and o for m, o in zip(mem, over)) / sum(over), .54)
check("M1 P(over given female)", sum(f and o for f, o in zip(fem, over)) / sum(fem), .45)
check("M1 mean order", st.mean(float(r["Order Total ($)"]) for r in sg), 100.14)
tp, fp = 10000 * .02 * .90, 10000 * .98 * .05
check("M1 P(fraud given flag)", tp / (tp + fp), .27)

# ---- Module 2: distributions
def binom_pmf(k, n_, p): return math.comb(n_, k) * p**k * (1 - p)**(n_ - k)
def pois_pmf(k, lam): return math.exp(-lam) * lam**k / math.factorial(k)
check("M2 binomial P(12 of 15)", binom_pmf(12, 15, .8), .25)
check("M2 binomial P(12 or more)", sum(binom_pmf(k, 15, .8) for k in range(12, 16)), .65)
check("M2 Poisson P(more than 15)", 1 - sum(pois_pmf(k, 12.5) for k in range(16)), .19)
sk = [float(r["Skiers per day"]) for r in rows("MtHighlands_SkierCounts.csv")]
mu, sd = st.mean(sk), st.stdev(sk)
check("M2 skier mean", mu, 747.39); check("M2 skier sd", sd, 159.63)
ncdf = lambda x: 0.5 * (1 + math.erf((x - mu) / (sd * math.sqrt(2))))
check("M2 P(more than 800)", 1 - ncdf(800), .37)
check("M2 P(450 to 770)", ncdf(770) - ncdf(450), .53)
lift = [float(r["Stop length (min)"]) for r in rows("MtHighlands_LiftStops.csv")]
a, b = min(lift), max(lift)
check("M2 uniform P(under 5)", (5 - a) / (b - a), .38)
check("M2 uniform mean", (a + b) / 2, 6.00)

# ---- Module 3: Green Valley 20
gv = rows("GreenValleyCommons_Residents.csv")
inc = [float(r["Monthly income ($)"]) for r in gv]; n20 = len(inc)
xbar, s = st.mean(inc), st.stdev(inc); se = s / math.sqrt(n20)
check("M3 mean income", xbar, 3398.90); check("M3 sd", s, 351.38); check("M3 se", se, 78.57)
t95 = sps.t.ppf(.975, n20 - 1) if sps else 2.093
check("M3 95% low", xbar - t95 * se, 3234.45); check("M3 95% high", xbar + t95 * se, 3563.35)
check("M3 n for $100 margin", math.ceil((1.96 * s / 100) ** 2), 48, 0)

# ---- Module 4: Denice
den = [float(r["Account balance ($)"]) for r in rows("DeniceToney_Balances.csv")]
md, sdd = st.mean(den), st.stdev(den); sed = sdd / math.sqrt(len(den)); t = (md - 2500) / sed
check("M4 mean", md, 2650.68); check("M4 t vs 2500", t, 1.90)
if sps: check("M4 p right tail", sps.t.sf(t, len(den) - 1), .038, 3)
gv48 = rows("GreenValleyCommons_Residents48.csv")
far = sum(float(r["Miles to their doctor"]) > 5 for r in gv48); ph = far / len(gv48)
check("M4 p-hat", ph, .48); check("M4 z", (ph - .4) / math.sqrt(.4 * .6 / len(gv48)), 1.12)

# ---- Module 5: Streamly and multitasking
ab = rows("Streamly_ABTest_CX.csv")
A = [float(r["CX score (1 to 10)"]) for r in ab if r["Variant"].startswith("A")]
B = [float(r["CX score (1 to 10)"]) for r in ab if r["Variant"].startswith("B")]
seab = math.sqrt(st.variance(A) / len(A) + st.variance(B) / len(B)); tab = (st.mean(B) - st.mean(A)) / seab
check("M5 mean A", st.mean(A), 7.44); check("M5 mean B", st.mean(B), 8.24); check("M5 t", tab, 2.53)
if sps: check("M5 p conservative df", 2 * sps.t.sf(tab, 39), .016, 3)
mt = rows("Multitasking_Example14.csv")
d = [float(r["Round 2 switching (sec)"]) - float(r["Round 1 single task (sec)"]) for r in mt]
check("M5 paired mean diff", st.mean(d), 28.14)
check("M5 paired t", st.mean(d) / (st.stdev(d) / math.sqrt(len(d))), 12.52)

# ---- Module 6: ANOVA
def anova(groups):
    k = len(groups); N = sum(len(g) for g in groups); grand = sum(map(sum, groups)) / N
    ssb = sum(len(g) * (st.mean(g) - grand) ** 2 for g in groups)
    ssw = sum(sum((x - st.mean(g)) ** 2 for x in g) for g in groups)
    return (ssb / (k - 1)) / (ssw / (N - k)), ssb, ssw
sal = rows("CareerServices_Salaries.csv")
paths = ["OR Analyst", "Accountant", "Computer Analyst", "Financial Specialist"]
F, ssb, ssw = anova([[float(r[p]) for r in sal] for p in paths])
check("M6 salary F", F, 76.51); check("M6 SSB", ssb, 3721172720, 0)
check("M6 mean OR Analyst", st.mean(float(r["OR Analyst"]) for r in sal), 81375.21)
cl = rows("Clinic_WaitTimes.csv")
Fc, _, _ = anova([[float(r[s_]) for r in cl] for s_ in ["Florida", "New York", "North Carolina"]])
check("M6 clinic F", Fc, .71)

# ---- Module 7: chi-square
obs = [38, 52, 40, 22, 18, 30]; claim = [.24, .20, .16, .14, .13, .13]
chi_mm = sum((o - 200 * c) ** 2 / (200 * c) for o, c in zip(obs, claim))
check("M7 M&M chi-square", chi_mm, 12.05)
srv = rows("SkiResort_Survey.csv")
act = lambda r: {"Snowboard": "Snowboard", "Shop": "Shop"}.get(r["Primary activity"], "Skis")  # downhill, cross-country, snowshoe = on skis
well = lambda r: "Wellness" if r["Amenity used most"] in ("Spa", "Hot tub") else "Not wellness"
tab = {}
for r in srv: tab[(act(r), well(r))] = tab.get((act(r), well(r)), 0) + 1
rt = {a: sum(v for (x, _), v in tab.items() if x == a) for a in ["Skis", "Snowboard", "Shop"]}
ct = {w: sum(v for (_, y), v in tab.items() if y == w) for w in ["Wellness", "Not wellness"]}
N = len(srv)
chi = sum((tab.get((a, w), 0) - rt[a] * ct[w] / N) ** 2 / (rt[a] * ct[w] / N) for a in rt for w in ct)
check("M7 3x2 chi-square", chi, 9.42)
check("M7 expected snowboard and wellness", rt["Snowboard"] * ct["Wellness"] / N, 9.32)

print()
if fails:
    print(f"{len(fails)} target(s) drifted: {', '.join(fails)}"); sys.exit(1)
print("All targets match 4_Library/sample-data/README.md." + ("" if sps else " (p-values skipped: scipy not installed)"))
