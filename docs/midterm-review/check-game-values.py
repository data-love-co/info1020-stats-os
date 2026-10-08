#!/usr/bin/env python3
"""Recompute every number quoted in the midterm review Jeopardy game from the course CSVs.

Run from the repo root:  python3 docs/midterm-review/check-game-values.py

The game's answers are deliberately NOT the lab values in 4_Library/sample-data/README.md.
They are new cuts on the same scenarios, so this script is their verification target.
No dependencies beyond the standard library (t critical values use the incomplete beta).
"""
import csv
import math
import os
import statistics as st
import sys
from math import comb, erf, exp, factorial, lgamma, sqrt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "4_Library", "sample-data")


def rows(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


def norm_inv(p, mu, sd):
    lo, hi = mu - 10 * sd, mu + 10 * sd
    for _ in range(200):
        mid = (lo + hi) / 2
        if phi((mid - mu) / sd) < p:
            lo = mid
        else:
            hi = mid
    return mid


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
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    bt = exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * _betacf(a, b, x) / a
    return 1 - bt * _betacf(b, a, 1 - x) / b


def t_inv_2t(alpha, df):
    """Excel T.INV.2T: the two-tailed critical value."""
    def two_tail(t):
        return _betai(df / 2, 0.5, df / (df + t * t))
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if two_tail(mid) > alpha:
            lo = mid
        else:
            hi = mid
    return mid


def poisson_cdf(k, lam):
    return sum(exp(-lam) * lam ** i / factorial(i) for i in range(k + 1))


def binom(k, n, p):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


checks = []


def check(label, got, want, places=2):
    ok = round(got, places) == want
    checks.append(ok)
    print(f"{'ok ' if ok else 'BAD'} {label}: got {round(got, places)} want {want}")


# ---------- Read the Table: SummitGear by channel and membership ----------
sg = rows("SummitGear_Data.csv")
n = len(sg)
online = [r["Channel"] == "Online" for r in sg]
member = [r["Rewards Member"] == "Yes" for r in sg]
returned = [int(r["Items Returned"]) >= 1 for r in sg]
both = sum(o and m for o, m in zip(online, member))
check("$100 online and member count", both, 51, 0)
check("$100 P(online and member)", both / n, .20)
check("$200 P(member given online)", both / sum(online), .31)
store_member = sum((not o) and m for o, m in zip(online, member))
check("$200 P(member given in-store)", store_member / (n - sum(online)), .40)
check("$300 P(online or member)", (sum(online) + sum(member) - both) / n, .79)
ret_store = sum(r and not o for r, o in zip(returned, online))
ret_online = sum(r and o for r, o in zip(returned, online))
check("$400 P(returned given in-store)", ret_store / (n - sum(online)), .22)
check("$400 P(returned given online)", ret_online / sum(online), .10)
true_flags, false_flags = 200 * .95, 9800 * .01
check("$500 true flags", true_flags, 190, 0)
check("$500 false flags", false_flags, 98, 0)
check("$500 P(fraud given flagged), new detector", true_flags / (true_flags + false_flags), .66)

# ---------- Pick the Distribution ----------
check("$100 Poisson sd at 8 per hour", sqrt(8), 2.83)
check("$100 P(exactly 8)", exp(-8) * 8 ** 8 / factorial(8), .14)
check("$200 binomial EV 25 at .60", 25 * .6, 15.00)
check("$200 binomial sd", sqrt(25 * .6 * .4), 2.45)
check("$200 P(exactly 15)", binom(15, 25, .6), .16)
check("$200 P(18 or more)", sum(binom(k, 25, .6) for k in range(18, 26)), .15)
check("$300 uniform 3 to 15: P(under 5)", (5 - 3) / 12, .17)
check("$300 P(over 10)", (15 - 10) / 12, .42)
check("$300 mean", (3 + 15) / 2, 9.00)
check("$400 P(more than 30) at 25 per hour", 1 - poisson_cdf(30, 25), .14)
check("$400 teammate's P(more than 31)", 1 - poisson_cdf(31, 25), .10)
check("$400 P(more than 35)", 1 - poisson_cdf(35, 25), .02)
sk = [float(r["Skiers per day"]) for r in rows("MtHighlands_SkierCounts.csv")]
mu, sd = st.mean(sk), st.stdev(sk)
check("$500 skier mean (input)", mu, 747.39)
check("$500 skier sd (input)", sd, 159.63)
check("$500 P(fewer than 500)", phi((500 - mu) / sd), .06)
check("$500 95th percentile", norm_inv(.95, mu, sd), 1010, 0)

# ---------- Mind the Margin ----------
tot = [float(r["Order Total ($)"]) for r in sg]
pmu, psd = st.mean(tot), st.stdev(tot)
se100 = psd / sqrt(100)
check("$100 SE at n = 100", se100, 3.70)
check("$100 P(sample mean over $105)", 1 - phi((105 - pmu) / se100), .09)
gv = rows("GreenValleyCommons_Residents48.csv")
inc = [float(r["Monthly income ($)"]) for r in gv]
n48 = len(inc)
m48, s48 = st.mean(inc), st.stdev(inc)
se48 = s48 / sqrt(n48)
t95 = t_inv_2t(.05, n48 - 1)
check("$300 mean income, 48 residents", m48, 3429.25)
check("$300 sd", s48, 345.78)
check("$300 SE", se48, 49.91)
check("$300 t* at df 47", t95, 2.012, 3)
me = t95 * se48
check("$400 margin of error", me, 100.40)
check("$400 95% low", m48 - me, 3328.85)
check("$400 95% high", m48 + me, 3529.65)
t90 = t_inv_2t(.10, n48 - 1)
check("$400 90% low (for the record)", m48 - t90 * se48, 3345.51)
check("$400 90% high (for the record)", m48 + t90 * se48, 3512.99)
men = sum(r["Male"] == "y" for r in gv)
check("$500 men of 48", men, 22, 0)
ph = men / n48
pme = 1.96 * sqrt(ph * (1 - ph) / n48)
check("$500 p-hat", ph, .46)
check("$500 proportion margin", pme, .14)
check("$500 proportion low", ph - pme, .32)
check("$500 proportion high", ph + pme, .60)
check("$500 n for a $75 margin", math.ceil((1.96 * 345.78 / 75) ** 2), 82, 0)

# ---------- The Manager Sentence inputs ----------
check("Manager $400 P(more than 25) at 25 per hour", 1 - poisson_cdf(25, 25), .45)

# ---------- Final Jeopardy ----------
tf, ff = 500 * .90, 9500 * .05
check("Final: true flags at 5% base rate", tf, 450, 0)
check("Final: false flags", ff, 475, 0)
check("Final: P(fraud given flagged)", tf / (tf + ff), .49)
check("Spare: n for a $50 margin with sd 351.38", math.ceil((1.96 * 351.38 / 50) ** 2), 190, 0)

bad = checks.count(False)
print()
print("All game values match." if not bad else f"{bad} value(s) do not match the game text. Fix the game or this script.")
sys.exit(1 if bad else 0)
