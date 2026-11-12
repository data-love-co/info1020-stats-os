#!/usr/bin/env python3
"""Recompute every number quoted in the final review Jeopardy game.

Run from the repo root:  python docs/final-review/check-game-values.py

The final game uses a fictional scenario (Fourteener Fitness) with every given on screen, so there
is no CSV to read. This script checks three things:
  1. The given tables are internally consistent (the Excel outputs match their own inputs).
  2. Every computed answer, critical value, and p-value in the game matches its recomputation.
  3. No computed answer is a number the labs or the midterm game already produced
     (4_Library/sample-data/README.md and docs/midterm-review/check-game-values.py).
No dependencies beyond the standard library: t and F tails use the regularized incomplete beta,
chi-square tails the regularized incomplete gamma, and the Tukey check the studentized range by
numerical integration.
"""
import math
import os
import re
import sys
from math import erf, exp, lgamma, log, sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


# ---------- distributions ----------
def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


def _betacf(a, b, x):
    maxit, eps, fpmin = 300, 3e-14, 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1 / (d if abs(d) >= fpmin else fpmin)
    h = d
    for m in range(1, maxit + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        d = 1 / (d if abs(d) >= fpmin else fpmin)
        c = 1 + aa / c
        c = c if abs(c) >= fpmin else fpmin
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        d = 1 / (d if abs(d) >= fpmin else fpmin)
        c = 1 + aa / c
        c = c if abs(c) >= fpmin else fpmin
        de = d * c
        h *= de
        if abs(de - 1) < eps:
            break
    return h


def _betai(a, b, x):
    """Regularized incomplete beta I_x(a, b)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    bt = exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * log(x) + b * log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * _betacf(a, b, x) / a
    return 1 - bt * _betacf(b, a, 1 - x) / b


def _gammq(a, x):
    """Regularized upper incomplete gamma Q(a, x)."""
    if x <= 0:
        return 1.0
    if x < a + 1:
        ap, total, delta = a, 1 / a, 1 / a
        for _ in range(1000):
            ap += 1
            delta *= x / ap
            total += delta
            if abs(delta) < abs(total) * 1e-15:
                break
        return 1 - total * exp(-x + a * log(x) - lgamma(a))
    tiny = 1e-300
    b = x + 1 - a
    c, d = 1 / tiny, 1 / b
    h = d
    for i in range(1, 1000):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = 1 / (d if abs(d) > tiny else tiny)
        c = b + an / c
        c = c if abs(c) > tiny else tiny
        de = d * c
        h *= de
        if abs(de - 1) < 1e-15:
            break
    return exp(-x + a * log(x) - lgamma(a)) * h


def t_dist_2t(t, df):
    """Excel T.DIST.2T."""
    return _betai(df / 2, 0.5, df / (df + t * t))


def t_dist_rt(t, df):
    """Excel T.DIST.RT."""
    p2 = t_dist_2t(t, df) / 2
    return p2 if t >= 0 else 1 - p2


def f_dist_rt(f, d1, d2):
    """Excel F.DIST.RT."""
    return _betai(d2 / 2, d1 / 2, d2 / (d2 + d1 * f))


def chisq_dist_rt(x, df):
    """Excel CHISQ.DIST.RT."""
    return _gammq(df / 2, x / 2)


def invert_tail(tail, alpha, hi=100.0):
    """Value whose right-tail area is alpha, for a decreasing tail function."""
    lo = 0.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if tail(mid) > alpha:
            lo = mid
        else:
            hi = mid
    return mid


def _simpson(f, a, b, n):
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += f(a + i * h) * (4 if i % 2 else 2)
    return total * h / 3


def ptukey(q, k, df):
    """P(Q <= q) for the studentized range with k groups and df error degrees of freedom."""
    def range_cdf(w):
        dens = lambda z: exp(-z * z / 2) / sqrt(2 * math.pi) * (phi(z) - phi(z - w)) ** (k - 1)
        return k * _simpson(dens, -8.0, 8.0, 160)
    logc = (df / 2) * log(df) - lgamma(df / 2) - (df / 2 - 1) * log(2)

    def outer(s):
        if s <= 0:
            return 0.0
        return exp(logc + (df - 1) * log(s) - df * s * s / 2) * range_cdf(q * s)
    return _simpson(outer, 0.0, 3.0, 120)


def qtukey(alpha, k, df):
    lo, hi = 1.0, 8.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if ptukey(mid, k, df) < 1 - alpha:
            lo = mid
        else:
            hi = mid
    return mid


# ---------- check helpers ----------
checks = []


def check(label, got, want, places=2):
    ok = round(got, places) == round(want, places)
    checks.append(ok)
    print(f"{'ok ' if ok else 'BAD'} {label}: got {round(got, places)} want {want}")


def check_true(label, cond):
    checks.append(bool(cond))
    print(f"{'ok ' if cond else 'BAD'} {label}")


# The course reference values for the distribution code, before the game is trusted to it.
check("self-test: T.INV.2T(.05, 39) from the Streamly lab", invert_tail(lambda t: t_dist_2t(t, 39), .05), 2.023, 3)
check("self-test: F.INV.RT(.05, 3, 76) from Career Services", invert_tail(lambda f: f_dist_rt(f, 3, 76), .05), 2.72)
check("self-test: CHISQ.INV.RT(.05, 5) from the M&M lab", invert_tail(lambda x: chisq_dist_rt(x, 5), .05), 11.07)
check("self-test: q(.05, 4, 76) from Career Services", qtukey(.05, 4, 76), 3.7149, 3)

answers = {}  # computed answers shown in the game, for the net-new check

# ---------- Pick Your Test $500: signup pages ----------
nA, mA, sA = 50, 62.40, 18.20
nB, mB, sB = 50, 71.10, 20.50
se = sqrt(sA ** 2 / nA + sB ** 2 / nB)
t = (mB - mA) / se
p = t_dist_2t(t, min(nA, nB) - 1)
check("Pick $500 difference", mB - mA, 8.70)
check("Pick $500 SE", se, 3.88)
check("Pick $500 t", t, 2.24)
check("Pick $500 two-tailed p, df 49", p, .029, 3)
answers.update({"Pick $500 p": .029, "Pick $500 SE": 3.88, "Pick $500 t": 2.24})
check("Key: one-tailed p (no-credit answer)", p / 2, .015, 3)
check("Key: larger s over smaller s", sB / sA, 1.13)
check("Key: pooled t-test p with df 98 (half-credit answer)", t_dist_2t(t, nA + nB - 2), .027, 3)

# ---------- Reject or Not?: the morning and evening output table ----------
v1, v2 = 20.3 / 45, 19.0 / 48
se_v = sqrt(v1 + v2)
t_v = (11.80 - 10.10) / se_v
welch_df = (v1 + v2) ** 2 / (v1 ** 2 / 44 + v2 ** 2 / 47)
check("Output table: Welch df rounded down", math.floor(welch_df), 90, 0)
check("Output table: t Stat", t_v, 1.85)
check("Output table: P one-tail", t_dist_rt(t_v, 90), .034, 3)
check("Output table: t Critical one-tail", invert_tail(lambda x: t_dist_rt(x, 90), .05), 1.662, 3)
check("Output table: P two-tail", t_dist_2t(t_v, 90), .068, 3)
t_star = invert_tail(lambda x: t_dist_2t(x, 90), .05)
check("Output table: t Critical two-tail", t_star, 1.987, 3)
check("Reject $500 SE given on screen", se_v, .92)
margin = t_star * 0.92
check("Reject $500 margin", margin, 1.83)
check("Reject $500 low", 1.70 - margin, -0.13)
check("Reject $500 high", 1.70 + margin, 3.53)
check("Reject $500 low, from the unrounded SE", 1.70 - t_star * se_v, -0.13)
check("Reject $500 high, from the unrounded SE", 1.70 + t_star * se_v, 3.53)
check_true("Reject $300: the 95% interval contains 0", 1.70 - margin < 0 < 1.70 + margin)
answers.update({"Reject $500 low": -0.13, "Reject $500 high": 3.53, "Reject $500 margin": 1.83})
check("Reject $400: 1 minus .011 as a percent", (1 - .011) * 100, 98.9, 1)

# ---------- ANOVA-thing Goes: satisfaction by location ----------
means = {"Golden": 8.10, "Boulder": 7.90, "Fort Collins": 7.70, "Colorado Springs": 6.10}
sds = {"Golden": 1.30, "Boulder": 1.25, "Fort Collins": 1.40, "Colorado Springs": 1.35}
n_g, k = 12, 4
grand = sum(means.values()) / k
ssb = n_g * sum((m - grand) ** 2 for m in means.values())
ssw = (n_g - 1) * sum(s ** 2 for s in sds.values())
df_b, df_w = k - 1, k * n_g - k
msb, msw = ssb / df_b, ssw / df_w
F = msb / msw
check("ANOVA table: SS between", ssb, 30.12)
check("ANOVA table: SS within", ssw, 77.39)
check("ANOVA table: SS total", ssb + ssw, 107.51)
check("ANOVA table: df between", df_b, 3, 0)
check("ANOVA table: df within", df_w, 44, 0)
check("ANOVA table: df total", k * n_g - 1, 47, 0)
check("ANOVA table: MS between", msb, 10.04)
check("ANOVA table: MS within", msw, 1.76)
check("ANOVA table: F", F, 5.71)
check("ANOVA table: P-value as printed", f_dist_rt(F, df_b, df_w), .0022, 4)
check("ANOVA $200: p", f_dist_rt(F, df_b, df_w), .002, 3)
check("ANOVA table: F crit", invert_tail(lambda f: f_dist_rt(f, df_b, df_w), .05), 2.816, 3)
q_crit = qtukey(.05, k, df_w)
hsd = q_crit * sqrt(msw / n_g)
names = list(means)
check("Key: Tukey HSD", hsd, 1.45)
check("Key: Tukey q", q_crit, 3.776, 3)
for i in range(k):
    for j in range(i + 1, k):
        a, b = names[i], names[j]
        should_differ = "Colorado Springs" in (a, b)
        differs = abs(means[a] - means[b]) > hsd
        check_true(f"ANOVA $400 Tukey (HSD {hsd:.4f}, q {q_crit:.4f}): {a} vs {b} "
                   f"{'differs' if should_differ else 'does not differ'}", differs == should_differ)
check("ANOVA $300 aside, family-wise error of 6 t-tests (run-of-show only)", 1 - .95 ** 6, .26)

# ---------- ANOVA-thing Goes $500: spend by tier ----------
ssb2, ssw2, k2, n2 = 1840, 9720, 3, 10
dfb2, dfw2 = k2 - 1, k2 * n2 - k2
check("ANOVA $500 df between", dfb2, 2, 0)
check("ANOVA $500 df within", dfw2, 27, 0)
check("ANOVA $500 MSTr (whole dollars)", ssb2 / dfb2, 920, 0)
check("ANOVA $500 MSE (whole dollars)", ssw2 / dfw2, 360, 0)
F2 = (ssb2 / dfb2) / (ssw2 / dfw2)
check("ANOVA $500 F", F2, 2.56)
check("ANOVA $500 p", f_dist_rt(F2, dfb2, dfw2), .096, 3)
f_crit2 = invert_tail(lambda f: f_dist_rt(f, dfb2, dfw2), .05)
check("Spare question: F crit for df 2 and 27", f_crit2, 3.354, 3)
answers.update({"ANOVA $500 p": .096, "ANOVA $500 F": 2.56, "ANOVA $500 MSTr": 920,
                "ANOVA $500 MSE": 360, "Spare F crit": 3.354})

# ---------- Chi Another Day: bookings against last year's mix ----------
shares = [.40, .30, .20, .10]
obs = [138, 128, 92, 42]
check("Chi table: bookings add to 400", sum(obs), 400, 0)
check("Chi $100 df", len(obs) - 1, 3, 0)
exp400 = [s * 400 for s in shares]
check("Chi $200 expected yoga", exp400[0], 160.00)
chi1 = sum((o - e) ** 2 / e for o, e in zip(obs, exp400))
check("Chi $400 chi-square", chi1, 5.46)
check("Chi $400 p", chisq_dist_rt(chi1, 3), .141, 3)
crit3 = invert_tail(lambda x: chisq_dist_rt(x, 3), .05)
check("Chi $400 critical value", crit3, 7.815, 3)
check("Chi $300 Pilates expected count", .01 * 400, 4, 0)
cs = [58, 74, 42, 26]
check("Chi $500 bookings add to 200", sum(cs), 200, 0)
exp200 = [s * 200 for s in shares]
for name, e, want in zip(["yoga", "spin", "strength", "climbing"], exp200, [80, 60, 40, 20]):
    check(f"Chi $500 expected {name}", e, want)
parts = [(o - e) ** 2 / e for o, e in zip(cs, exp200)]
for name, c, want in zip(["yoga", "spin", "strength", "climbing"], parts, [6.05, 3.27, 0.10, 1.80]):
    check(f"Chi $500 contribution {name}", c, want)
chi2 = sum(parts)
check("Chi $500 chi-square", chi2, 11.22)
check("Chi $500 p (run-of-show)", chisq_dist_rt(chi2, 3), .011, 3)
answers.update({"Chi $200 expected": 160, "Chi $400 critical": 7.815, "Chi $500 chi-square": 11.22,
                "Chi $500 p": .011})

# ---------- So What? Now What? Daily Double: paired app test ----------
dbar, t_dd, n_dd = 0.9, 3.10, 30
check("DD p, two-tailed, df 29", t_dist_2t(t_dd, n_dd - 1), .004, 3)
se_dd = dbar / t_dd
t29 = invert_tail(lambda x: t_dist_2t(x, n_dd - 1), .05)
check("DD interval low", dbar - t29 * se_dd, 0.31)
check("DD interval high", dbar + t29 * se_dd, 1.49)

# ---------- Final Jeopardy ----------
lo_fj, hi_fj = 0.91, 16.49
check("Final: margin of error", (hi_fj - lo_fj) / 2, 7.79)
t49 = invert_tail(lambda x: t_dist_2t(x, 49), .05)
check("Final: the interval is the signup-page interval, low", 8.70 - t49 * se, 0.91)
check("Final: the interval is the signup-page interval, high", 8.70 + t49 * se, 16.49)
check_true("Final: 0 lies outside the interval (a two-tailed test rejects)", lo_fj > 0)
check("Final key: full width (no-credit answer)", hi_fj - lo_fj, 15.58)
check("Final key: point estimate (no-credit answer)", (hi_fj + lo_fj) / 2, 8.70)
answers["Final margin"] = 7.79

# ---------- Run-of-show timing: the 25 clocks, read from the game itself ----------
with open(os.path.join(HERE, "index.html"), encoding="utf-8") as f:
    page = f.read()
TIME_LIMITS = {int(k): int(v) for k, v in
               re.findall(r"(\d+): (\d+)", re.search(r"const TIME_LIMITS = \{(.*?)\};", page).group(1))}
EXCEL_EXTRA = int(re.search(r"const EXCEL_EXTRA = (\d+);", page).group(1))
DD_SECONDS = int(re.search(r"seconds: (\d+),", page).group(1))
FINAL_SECONDS = int(re.search(r"timerStart\((\d+), 'Write your answer'\)", page).group(1))
check("Clock $100 (1 minute)", TIME_LIMITS[100], 60, 0)
check("Clock $200 (1.5 minutes)", TIME_LIMITS[200], 90, 0)
check("Clock $300 (2 minutes)", TIME_LIMITS[300], 120, 0)
check("Clock $400 (2 minutes)", TIME_LIMITS[400], 120, 0)
check("Clock $500 (4 minutes)", TIME_LIMITS[500], 240, 0)
check("Clock Excel cells (6 minutes)", TIME_LIMITS[500] + EXCEL_EXTRA, 360, 0)
check("Clock Daily Double (6 minutes)", DD_SECONDS, 360, 0)
check("Clock Final Jeopardy (2 minutes)", FINAL_SECONDS, 120, 0)
clock = sum(TIME_LIMITS.values()) * 5 + 4 * EXCEL_EXTRA + (DD_SECONDS - TIME_LIMITS[500])
check("Run-of-show: the 25 clocks in minutes", clock / 60, 62.5, 1)
check("Run-of-show: gameplay with 45 seconds per reveal, in minutes", (clock + 25 * 45) / 60, 81, 0)

# ---------- Net new: no computed answer is a lab or midterm value ----------
taken = set()
num = re.compile(r"(?<![\w.])-?\$?\d[\d,]*\.?\d*|(?<![\w\d])-?\.\d+")
for rel in ("4_Library/sample-data/README.md", "docs/midterm-review/check-game-values.py"):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        for tok in num.findall(f.read()):
            tok = tok.replace("$", "").replace(",", "")
            try:
                taken.add(round(float(tok), 4))
            except ValueError:
                pass
for label, value in answers.items():
    check_true(f"net new: {label} = {value} is not a lab or midterm value", round(value, 4) not in taken)

bad = checks.count(False)
print()
print("All game values match." if not bad else f"{bad} value(s) do not match the game text. Fix the game or this script.")
sys.exit(1 if bad else 0)
