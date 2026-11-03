#!/usr/bin/env python3
"""
check-values.py: recompute the verification targets in 4_Library/sample-data/README.md from the
CSVs and report any drift.

Run from the repo root:
    python 0_System/scripts/check-values.py

Standard library only, including the distributions. t, chi-square and F come from the incomplete
beta and gamma functions implemented below, so nothing is skipped when scipy is missing; scipy is
used as a cross-check when it happens to be installed.

The distribution code self-tests against values the course already publishes before any target is
checked. If that self-test fails, every number after it would be suspect, so the script stops.

Rounding is half up, matching 4_Library/method/rounding-policy.md. Python's built-in round() is
half to even, which disagrees on exactly the values this file cares about: the Module 6 grand mean
is 75716.165, which the course reports as $75,716.17 and round() reports as $75,716.16.
"""
import csv, math, os, statistics as st, sys
from decimal import Decimal, ROUND_HALF_UP
from statistics import NormalDist

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, "4_Library", "sample-data")
try:
    from scipy import stats as sps
except ImportError:
    sps = None

# --------------------------------------------------------------------------- distributions
def _betacf(a, b, x):
    MAXIT, EPS, FPMIN = 400, 3e-16, 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < FPMIN: d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS: break
    return h

def betainc(a, b, x):
    """Regularised incomplete beta."""
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lb = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lb + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1 - x) / b

def gammainc(s, x):
    """Regularised lower incomplete gamma."""
    if x <= 0: return 0.0
    if x < s + 1:
        term = 1.0 / s
        total = term
        for n in range(1, 2000):
            term *= x / (s + n)
            total += term
            if abs(term) < abs(total) * 1e-16: break
        return total * math.exp(-x + s * math.log(x) - math.lgamma(s))
    FPMIN = 1e-300
    b, c = x + 1 - s, 1 / FPMIN
    d = 1 / b
    h = d
    for i in range(1, 2000):
        an = -i * (i - s)
        b += 2
        d = an * d + b
        if abs(d) < FPMIN: d = FPMIN
        c = b + an / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-16: break
    return 1.0 - math.exp(-x + s * math.log(x) - math.lgamma(s)) * h

def _solve(f, target, lo, hi):
    for _ in range(300):
        mid = (lo + hi) / 2
        if f(mid) > target: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def t_sf(t, df):                       # T.DIST.RT
    p = 0.5 * betainc(df / 2.0, 0.5, df / (df + t * t))
    return p if t > 0 else 1 - p
def t_sf2(t, df): return 2 * t_sf(abs(t), df)            # T.DIST.2T
def t_inv(p, df): return _solve(lambda x: t_sf(x, df), 1 - p, 0.0, 200.0)      # T.INV
def t_inv_2t(a, df): return _solve(lambda x: t_sf(x, df), a / 2, 0.0, 200.0)   # T.INV.2T
def chi2_sf(x, df): return 1 - gammainc(df / 2.0, x / 2.0)                     # CHISQ.DIST.RT
def chi2_inv_rt(p, df): return _solve(lambda x: chi2_sf(x, df), p, 0.0, 10000.0)
def f_sf(f, d1, d2): return betainc(d2 / 2.0, d1 / 2.0, d2 / (d2 + d1 * f))    # F.DIST.RT
def f_inv_rt(p, d1, d2): return _solve(lambda x: f_sf(x, d1, d2), p, 0.0, 100000.0)

# --------------------------------------------------------------------------- harness
fails, wanted = [], []

def r(x, places=2):
    return float(Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP))

def check(label, got, want, places=2, in_readme=True):
    """in_readme=False for derived checks whose value is not a row in the table."""
    ok = r(got, places) == want
    print(f"{'ok ' if ok else 'XX '} {label}: got {r(got, places)} want {want}")
    if not ok: fails.append(label)
    if in_readme: wanted.append((label, want, places))

def rows(name):
    with open(os.path.join(D, name), newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

# --------------------------------------------------------------------------- self-test
print("Distribution self-test (course-published values)")
_st = [
    ("T.INV.2T(.05, 19) = 2.093", t_inv_2t(.05, 19), 2.093, 3),
    ("T.INV(.95, 15) = 1.753", t_inv(.95, 15), 1.753, 3),
    # Round trips, which are exact by construction. Do not put a data-derived
    # p-value here: feeding the rounded t of 1.88 returns .080 while the exact
    # t of -1.8835 returns .079, and that gap is the input rounding, not the code.
    ("T.DIST.2T round trip at .05, df 15", t_sf2(t_inv_2t(.05, 15), 15), .05, 3),
    ("CHISQ.DIST.RT round trip at .05, df 5", chi2_sf(chi2_inv_rt(.05, 5), 5), .05, 3),
    ("F.DIST.RT round trip at .05, df 3 and 76", f_sf(f_inv_rt(.05, 3, 76), 3, 76), .05, 3),
    ("T.INV.2T(.05, 39) = 2.023", t_inv_2t(.05, 39), 2.023, 3),
    ("F.INV.RT(.05, 3, 76) = 2.72", f_inv_rt(.05, 3, 76), 2.72, 2),
    ("F.INV.RT(.05, 2, 57) = 3.16", f_inv_rt(.05, 2, 57), 3.16, 2),
    ("CHISQ.INV.RT(.05, 5) = 11.07", chi2_inv_rt(.05, 5), 11.07, 2),
    ("CHISQ.INV.RT(.05, 2) = 5.99", chi2_inv_rt(.05, 2), 5.99, 2),
    ("NORM.S.INV(.975) = 1.960", NormalDist().inv_cdf(.975), 1.960, 3),
]
_bad = [lbl for lbl, got, want, pl in _st if r(got, pl) != want]
for lbl, got, want, pl in _st:
    print(f"{'ok ' if r(got, pl) == want else 'XX '} {lbl}  (got {r(got, pl)})")
if _bad:
    print("\nThe distribution code is wrong; every target below would be unreliable.")
    sys.exit(2)
if sps:
    _x = [abs(t_inv_2t(.05, 19) - sps.t.ppf(.975, 19)), abs(chi2_sf(12.05, 5) - sps.chi2.sf(12.05, 5)),
          abs(f_sf(.71, 2, 57) - sps.f.sf(.71, 2, 57))]
    print(f"    scipy cross-check agrees to {max(_x):.2e}")
print()

# --------------------------------------------------------------------------- Module 1
sg = rows("SummitGear_Data.csv"); n = len(sg)
mem = [x["Rewards Member"] == "Yes" for x in sg]
over = [float(x["Order Total ($)"]) > 100 for x in sg]
fem = [x["Gender"] == "Female" for x in sg]
both = sum(m and o for m, o in zip(mem, over))
check("M1 P(member)", sum(mem) / n, .34)
check("M1 P(over $100)", sum(over) / n, .49)
check("M1 P(female)", sum(fem) / n, .52)
check("M1 P(online)", sum(x["Channel"] == "Online" for x in sg) / n, .66)
check("M1 P(age 60 or over)", sum(int(x["Age"]) >= 60 for x in sg) / n, .08)
check("M1 P(member and over)", both / n, .26)
check("M1 P(member or over)", sum(m or o for m, o in zip(mem, over)) / n, .56)
check("M1 P(over given member)", both / sum(mem), .78)
check("M1 P(member given over)", both / sum(over), .54)
check("M1 P(over given female)", sum(f and o for f, o in zip(fem, over)) / sum(fem), .45)
check("M1 P(over given male)", sum((not f) and o for f, o in zip(fem, over)) / (n - sum(fem)), .53)
check("M1 P(at least one item returned)", sum(int(x["Items Returned"]) >= 1 for x in sg) / n, .14)
check("M1 mean order", st.mean(float(x["Order Total ($)"]) for x in sg), 100.14)
tp, fp = 10000 * .02 * .90, 10000 * .98 * .05
check("M1 true flags", tp, 180, 0); check("M1 false flags", fp, 490, 0)
check("M1 P(fraud given flag)", tp / (tp + fp), .27)

# --------------------------------------------------------------------------- Module 2
def binom_pmf(k, n_, p): return math.comb(n_, k) * p**k * (1 - p)**(n_ - k)
def pois_pmf(k, lam): return math.exp(-lam) * lam**k / math.factorial(k)
check("M2 binomial P(12 of 15)", binom_pmf(12, 15, .8), .25)
check("M2 binomial P(12 or more)", sum(binom_pmf(k, 15, .8) for k in range(12, 16)), .65)
check("M2 binomial sd", math.sqrt(15 * .8 * .2), 1.55)
check("M2 Poisson P(exactly 8)", pois_pmf(8, 12.5), .06)
check("M2 Poisson P(15 or fewer)", sum(pois_pmf(k, 12.5) for k in range(16)), .81)
check("M2 Poisson P(more than 15)", 1 - sum(pois_pmf(k, 12.5) for k in range(16)), .19)
check("M2 Poisson sd", math.sqrt(12.5), 3.54)
sk = [float(x["Skiers per day"]) for x in rows("MtHighlands_SkierCounts.csv")]
mu, sd = st.mean(sk), st.stdev(sk)
nd = NormalDist(mu, sd)
check("M2 skier mean", mu, 747.39); check("M2 skier sd", sd, 159.63)
check("M2 P(more than 800)", 1 - nd.cdf(800), .37)
check("M2 P(450 to 770)", nd.cdf(770) - nd.cdf(450), .53)
check("M2 90th percentile", nd.inv_cdf(.90), 952, 0)
check("M2 25th percentile", nd.inv_cdf(.25), 640, 0)
lift = [float(x["Stop length (min)"]) for x in rows("MtHighlands_LiftStops.csv")]
a, b = min(lift), max(lift)
check("M2 uniform P(under 5)", (5 - a) / (b - a), .38)
check("M2 uniform P(over 4)", (b - 4) / (b - a), .75)
check("M2 uniform mean", (a + b) / 2, 6.00)

# --------------------------------------------------------------------------- Module 3
gv = rows("GreenValleyCommons_Residents.csv")
inc = [float(x["Monthly income ($)"]) for x in gv]; n20 = len(inc)
xbar, s = st.mean(inc), st.stdev(inc); se = s / math.sqrt(n20)
t95, t90 = t_inv_2t(.05, n20 - 1), t_inv_2t(.10, n20 - 1)
check("M3 mean income", xbar, 3398.90); check("M3 sd", s, 351.38); check("M3 se", se, 78.57)
check("M3 t* 95% df 19", t95, 2.093, 3)
check("M3 margin of error", t95 * se, 164.45)
check("M3 95% low", xbar - t95 * se, 3234.45); check("M3 95% high", xbar + t95 * se, 3563.35)
check("M3 90% low", xbar - t90 * se, 3263.04); check("M3 90% high", xbar + t90 * se, 3534.76)
check("M3 share within 5 miles", sum(float(x["Miles to their doctor"]) <= 5 for x in gv) / n20, .50)
check("M3 share male", sum(x["Male"].strip().lower() in ("1", "yes", "y", "true") for x in gv) / n20, .40)
check("M3 n for $100 margin", math.ceil((1.96 * s / 100) ** 2), 48, 0)
check("M3 n for $150 margin", math.ceil((1.96 * s / 150) ** 2), 22, 0)

# --------------------------------------------------------------------------- Module 4
den = [float(x["Account balance ($)"]) for x in rows("DeniceToney_Balances.csv")]
nd4 = len(den); md, sdd = st.mean(den), st.stdev(den)
sed = sdd / math.sqrt(nd4); t4 = (md - 2500) / sed; t4b = (md - 2800) / sed
tc4 = t_inv_2t(.05, nd4 - 1)
check("M4 mean", md, 2650.68); check("M4 sd", sdd, 317.11); check("M4 se", sed, 79.28)
check("M4 t vs 2500", t4, 1.90)
check("M4 p right tail", t_sf(t4, nd4 - 1), .038, 3)
check("M4 critical t right tail", t_inv(.95, nd4 - 1), 1.753, 3)
check("M4 t vs 2800", t4b, -1.88)
check("M4 p two tails vs 2800", t_sf2(t4b, nd4 - 1), .079, 3)
check("M4 95% low", md - tc4 * sed, 2481.70); check("M4 95% high", md + tc4 * sed, 2819.66)
gv48 = rows("GreenValleyCommons_Residents48.csv")
far = sum(float(x["Miles to their doctor"]) > 5 for x in gv48); ph = far / len(gv48)
check("M4 p-hat", ph, .48)
check("M4 z", (ph - .4) / math.sqrt(.4 * .6 / len(gv48)), 1.12)

# --------------------------------------------------------------------------- Module 5
ab = rows("Streamly_ABTest_CX.csv")
A = [float(x["CX score (1 to 10)"]) for x in ab if x["Variant"].startswith("A")]
B = [float(x["CX score (1 to 10)"]) for x in ab if x["Variant"].startswith("B")]
seab = math.sqrt(st.variance(A) / len(A) + st.variance(B) / len(B))
diff = st.mean(B) - st.mean(A); tab = diff / seab
dfc = min(len(A), len(B)) - 1
tc5 = t_inv_2t(.05, dfc)
check("M5 mean A", st.mean(A), 7.44); check("M5 mean B", st.mean(B), 8.24)
check("M5 sd A", st.stdev(A), 1.60); check("M5 sd B", st.stdev(B), 1.21)
check("M5 difference", diff, .80)
check("M5 standard error", seab, .317, 3)
check("M5 t", tab, 2.53)
check("M5 conservative df", dfc, 39, 0)
check("M5 p conservative df", t_sf2(tab, dfc), .016, 3)
vA, vB = st.variance(A) / len(A), st.variance(B) / len(B)
dfw = (vA + vB) ** 2 / (vA ** 2 / (len(A) - 1) + vB ** 2 / (len(B) - 1))
check("M5 p Welch df", t_sf2(tab, dfw), .014, 3)
check("M5 t* 95% df 39", tc5, 2.023, 3)
check("M5 interval low", diff - tc5 * seab, .16, 2)
check("M5 interval high", diff + tc5 * seab, 1.44, 2)
mt = rows("Multitasking_Example14.csv")
d = [float(x["Round 2 switching (sec)"]) - float(x["Round 1 single task (sec)"]) for x in mt]
sedp = st.stdev(d) / math.sqrt(len(d))
check("M5 paired mean diff", st.mean(d), 28.14)
check("M5 paired sd", st.stdev(d), 8.41)
check("M5 paired se", sedp, 2.25)
check("M5 paired t", st.mean(d) / sedp, 12.52)

# --------------------------------------------------------------------------- Module 6
def anova(groups):
    k = len(groups); N = sum(len(g) for g in groups)
    grand = sum(map(sum, groups)) / N
    ssb = sum(len(g) * (st.mean(g) - grand) ** 2 for g in groups)
    ssw = sum(sum((x - st.mean(g)) ** 2 for x in g) for g in groups)
    msb, msw = ssb / (k - 1), ssw / (N - k)
    return dict(k=k, N=N, grand=grand, ssb=ssb, ssw=ssw, dfb=k - 1, dfw=N - k,
                msb=msb, msw=msw, F=msb / msw)

sal = rows("CareerServices_Salaries.csv")
paths = ["OR Analyst", "Accountant", "Computer Analyst", "Financial Specialist"]
grp = {p: [float(x[p]) for x in sal] for p in paths}
a6 = anova([grp[p] for p in paths])
for p, want in [("OR Analyst", 81375.21), ("Computer Analyst", 83253.65),
                ("Accountant", 71370.22), ("Financial Specialist", 66865.57)]:
    check(f"M6 mean {p}", st.mean(grp[p]), want)
check("M6 grand mean", a6["grand"], 75716.17)
sds = [st.stdev(grp[p]) for p in paths]
check("M6 spread ratio", max(sds) / min(sds), 2.19)
check("M6 SSB", a6["ssb"], 3721172720, 0); check("M6 SSW", a6["ssw"], 1232181262, 0)
check("M6 df between", a6["dfb"], 3, 0); check("M6 df within", a6["dfw"], 76, 0)
check("M6 MSB", a6["msb"], 1240390907, 0); check("M6 MSW", a6["msw"], 16212911, 0)
check("M6 salary F", a6["F"], 76.51)
check("M6 F* at .05", f_inv_rt(.05, a6["dfb"], a6["dfw"]), 2.72)
check("M6 salary p under .001", 1 if f_sf(a6["F"], a6["dfb"], a6["dfw"]) < .001 else 0, 1, 0, in_readme=False)
Q = 3.7149  # studentized range, k = 4, df = 76; Excel has no function, the workbook gives it
hsd = Q * math.sqrt(a6["msw"] / 20)
check("M6 Tukey HSD", hsd, 3344.74)
gap = st.mean(grp["Computer Analyst"]) - st.mean(grp["OR Analyst"])
check("M6 Computer vs OR Analyst gap", gap, 1878.43)
check("M6 that pair does not differ", 1 if gap < hsd else 0, 1, 0, in_readme=False)
others = [abs(st.mean(grp[x]) - st.mean(grp[y])) for i, x in enumerate(paths) for y in paths[i + 1:]
          if {x, y} != {"Computer Analyst", "OR Analyst"}]
check("M6 the other five pairs all differ", 1 if all(g > hsd for g in others) else 0, 1, 0, in_readme=False)
check("M6 family-wise error of six tests", 1 - .95 ** 6, .26)
cl = rows("Clinic_WaitTimes.csv")
states = ["Florida", "New York", "North Carolina"]
cg = {s_: [float(x[s_]) for x in cl] for s_ in states}
a6c = anova([cg[s_] for s_ in states])
for s_, want in [("Florida", 14.50), ("New York", 15.25), ("North Carolina", 13.95)]:
    check(f"M6 clinic mean {s_}", st.mean(cg[s_]), want)
check("M6 clinic grand mean", a6c["grand"], 14.57)
check("M6 clinic F", a6c["F"], .71)
check("M6 clinic F* at .05", f_inv_rt(.05, a6c["dfb"], a6c["dfw"]), 3.16)
check("M6 clinic p", f_sf(a6c["F"], a6c["dfb"], a6c["dfw"]), .494, 3)

# --------------------------------------------------------------------------- Module 7
obs = [38, 52, 40, 22, 18, 30]; claim = [.24, .20, .16, .14, .13, .13]
exp = [200 * c for c in claim]
chi_mm = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
check("M7 M&M expected blue", exp[0], 48.00); check("M7 M&M expected green", exp[1], 40.00)
check("M7 M&M contribution blue", (obs[0] - exp[0]) ** 2 / exp[0], 2.08)
check("M7 M&M contribution green", (obs[1] - exp[1]) ** 2 / exp[1], 3.60)
check("M7 M&M chi-square", chi_mm, 12.05)
check("M7 M&M critical at .05", chi2_inv_rt(.05, 5), 11.07)
check("M7 M&M critical at .01", chi2_inv_rt(.01, 5), 15.09)
check("M7 M&M p", chi2_sf(chi_mm, 5), .034, 3)

srv = rows("SkiResort_Survey.csv")
N7 = len(srv)
acts = sorted({x["Primary activity"] for x in srv})
amen = sorted({x["Amenity used most"] for x in srv})
full = {(a_, w_): sum(x["Primary activity"] == a_ and x["Amenity used most"] == w_ for x in srv)
        for a_ in acts for w_ in amen}
rowt = {a_: sum(v for (p_, _), v in full.items() if p_ == a_) for a_ in acts}
colt = {w_: sum(v for (_, q_), v in full.items() if q_ == w_) for w_ in amen}
under5 = sum(1 for a_ in acts for w_ in amen if rowt[a_] * colt[w_] / N7 < 5)
check("M7 full table cells", len(acts) * len(amen), 25, 0)
check("M7 full table cells with expected under 5", under5, 20, 0)

act = lambda x: {"Snowboard": "Snowboard", "Shop": "Shop"}.get(x["Primary activity"], "Skis")
well = lambda x: "Wellness" if x["Amenity used most"] in ("Spa", "Hot tub") else "Not wellness"
tab = {}
for x in srv:
    tab[(act(x), well(x))] = tab.get((act(x), well(x)), 0) + 1
rt = {a_: sum(v for (p_, _), v in tab.items() if p_ == a_) for a_ in ["Skis", "Snowboard", "Shop"]}
ct = {w_: sum(v for (_, q_), v in tab.items() if q_ == w_) for w_ in ["Wellness", "Not wellness"]}
for key, want in [(("Skis", "Wellness"), 23), (("Skis", "Not wellness"), 15),
                  (("Snowboard", "Wellness"), 4), (("Snowboard", "Not wellness"), 13),
                  (("Shop", "Wellness"), 13), (("Shop", "Not wellness"), 5)]:
    check(f"M7 observed {key[0]} / {key[1]}", tab.get(key, 0), want, 0)
check("M7 snowboarders", rt["Snowboard"], 17, 0)
check("M7 snowboarder share", rt["Snowboard"] / N7, .23)
check("M7 expected snowboard and wellness", rt["Snowboard"] * ct["Wellness"] / N7, 9.32)
chi7 = sum((tab.get((a_, w_), 0) - rt[a_] * ct[w_] / N7) ** 2 / (rt[a_] * ct[w_] / N7)
           for a_ in rt for w_ in ct)
check("M7 3x2 chi-square", chi7, 9.42)
check("M7 3x2 critical at .05", chi2_inv_rt(.05, 2), 5.99)
check("M7 3x2 p", chi2_sf(chi7, 2), .009, 3)

# --------------------------------------------------------------------------- README cross-check
# The checks above compare the CSVs against values written in THIS script, so they catch a
# dataset that moved. They do not catch a typo in the README table, which is the other way a
# target goes wrong and the way the Module 6 Tukey HSD went wrong ($3,344.70 for $3,344.74).
# So: every value this script asserts must also appear, as written, in the README.
print()
print("README cross-check (every asserted value appears in the table)")
with open(os.path.join(D, "README.md"), encoding="utf-8") as f:
    readme = f.read()

def forms(v, places):
    """The ways the README might legitimately write this number."""
    plain = f"{v:,.{places}f}" if places else f"{int(round(v)):,d}"
    out = {plain, plain.replace(",", "")}
    for t in list(out):
        if t.startswith("0."):           # probabilities drop the leading zero
            out.add(t[1:])
        out.add("$" + t)
    return out

missing = []
for label, want, places in wanted:
    if not any(t in readme for t in forms(want, places)):
        missing.append((label, want))
if missing:
    for label, want in missing:
        print(f"XX  {label}: this script asserts {want}, which is not in the README table")
    print(f"\n{len(missing)} value(s) in the script are not in the README. One of the two is wrong.")
else:
    print(f"ok  all {len(wanted)} asserted values found in the table")

# --------------------------------------------------------------------------- report
print()
if fails or missing:
    if fails:
        print(f"{len(fails)} target(s) drifted from the data: {', '.join(fails)}")
    if missing:
        print(f"{len(missing)} target(s) disagree with the README table.")
    sys.exit(1)
print(f"All {len(wanted)} targets match the data and the README table.")
