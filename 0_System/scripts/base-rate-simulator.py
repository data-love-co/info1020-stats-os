#!/usr/bin/env python3
"""
base-rate-simulator.py: build a base-rate decision tree and posterior probabilities.

Run from the repo root:
    python 0_System/scripts/base-rate-simulator.py
    python 0_System/scripts/base-rate-simulator.py --base-rate 2% --catch-rate 90% --false-alarm-rate 5%
    python 0_System/scripts/base-rate-simulator.py --compare "Higher base rate" 10% 90% 5% --compare "Lower base rate" .5% 90% 5%

Keep each command on one line. A backslash continues a line in bash but not in
PowerShell, so a wrapped command fails on Windows.
"""

import argparse
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28


def parse_rate(text):
    """Accept decimal rates like .02 or percentage strings like 2%."""
    cleaned = text.strip()
    if cleaned.endswith("%"):
        cleaned = cleaned[:-1].strip()
        return Decimal(cleaned) / Decimal("100")
    return Decimal(cleaned)


def validate_rate(name, value):
    if value < 0 or value > 1:
        raise ValueError(f"{name} must be between 0 and 1 inclusive; got {value}")


def format_count(value):
    text = format(value, ",f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text


def strip_leading_zero(text):
    """.27 rather than 0.27: a probability cannot exceed 1, so the zero is noise."""
    if text.startswith("0."):
        return text[1:]
    if text.startswith("-0."):
        return "-" + text[2:]
    return text


def format_probability(value, places=2):
    quantum = Decimal("1").scaleb(-places)
    rounded = value.quantize(quantum, rounding=ROUND_HALF_UP)
    # A small probability is not a zero one. Report the bound instead, the same
    # way the course reports a p-value below .001 as an inequality.
    if rounded == 0 and value > 0:
        return "< " + strip_leading_zero(format(quantum, f".{places}f"))
    if rounded == 1 and value < 1:
        return "> " + strip_leading_zero(format(1 - quantum, f".{places}f"))
    text = format(rounded, f".{places}f")
    if abs(rounded) < 1:
        text = strip_leading_zero(text)
    return text


def format_probability_unrounded(value):
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    if abs(value) < 1:
        text = strip_leading_zero(text)
    return text


def format_rate(value):
    percent = value * Decimal("100")
    text = format(percent, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return f"{text}%"


def is_whole(*values):
    return all(value == value.to_integral_value() for value in values)


def whole_number_cases(base_rate, catch_rate, false_alarm_rate, cases):
    """
    Grow the tree by powers of ten until every branch is a whole number of cases.

    The tree of 10,000 only teaches if the branches are countable things. A base
    rate of .5% splits 10,000 into 497.5 false flags, and half a flag is not
    something a manager can picture. Every rate here is a finite decimal, so
    some power of ten always clears it.
    """
    for step in range(0, 13):
        scaled = cases * (Decimal(10) ** step)
        has = scaled * base_rate
        without = scaled - has
        if is_whole(has, without, has * catch_rate, without * false_alarm_rate):
            return scaled
    return cases


def calculate_base_rate_tree(
    base_rate, catch_rate, false_alarm_rate, cases=10_000, requested_cases=None
):
    """
    Return raw tree counts and posterior probabilities for a base-rate problem.

    Inputs are decimal rates from 0 to 1 inclusive. The tree grows to the
    smallest power-of-ten multiple of `cases` that keeps every branch whole, so
    the counts stay countable. Counts are returned without rounding.
    """
    base_rate = Decimal(base_rate)
    catch_rate = Decimal(catch_rate)
    false_alarm_rate = Decimal(false_alarm_rate)
    cases = Decimal(cases)

    validate_rate("base_rate", base_rate)
    validate_rate("catch_rate", catch_rate)
    validate_rate("false_alarm_rate", false_alarm_rate)
    if cases <= 0:
        raise ValueError(f"cases must be positive; got {cases}")

    requested_cases = Decimal(cases if requested_cases is None else requested_cases)
    cases = whole_number_cases(base_rate, catch_rate, false_alarm_rate, cases)

    has_condition = cases * base_rate
    without_condition = cases - has_condition

    flagged_condition = has_condition * catch_rate
    not_flagged_condition = has_condition - flagged_condition

    flagged_without_condition = without_condition * false_alarm_rate
    not_flagged_without_condition = without_condition - flagged_without_condition

    total_flagged = flagged_condition + flagged_without_condition
    total_not_flagged = not_flagged_condition + not_flagged_without_condition

    probability_condition_given_flagged = (
        flagged_condition / total_flagged if total_flagged else Decimal("0")
    )
    probability_condition_given_not_flagged = (
        not_flagged_condition / total_not_flagged if total_not_flagged else Decimal("0")
    )

    return {
        "cases": cases,
        "requested_cases": requested_cases,
        "base_rate": base_rate,
        "catch_rate": catch_rate,
        "false_alarm_rate": false_alarm_rate,
        "has_condition": has_condition,
        "without_condition": without_condition,
        "flagged_condition": flagged_condition,
        "not_flagged_condition": not_flagged_condition,
        "flagged_without_condition": flagged_without_condition,
        "not_flagged_without_condition": not_flagged_without_condition,
        "total_flagged": total_flagged,
        "total_not_flagged": total_not_flagged,
        "probability_condition_given_flagged": probability_condition_given_flagged,
        "probability_condition_given_not_flagged": probability_condition_given_not_flagged,
    }


def print_scenario(label, result):
    print(label)
    print("=" * len(label))
    print(
        "Rates confirmed: "
        f"{format_rate(result['base_rate'])} of cases have the condition, "
        f"the detector flags {format_rate(result['catch_rate'])} of true cases, "
        f"and it flags {format_rate(result['false_alarm_rate'])} of cases without the condition."
    )
    print()
    if result["cases"] != result["requested_cases"]:
        print(
            f"Tree grown from {format_count(result['requested_cases'])} to "
            f"{format_count(result['cases'])} cases so every branch is a whole number."
        )
    print(f"Decision tree for {format_count(result['cases'])} cases")
    print(
        f"- Cases with the condition: {format_count(result['has_condition'])}\n"
        f"  - Flagged: {format_count(result['flagged_condition'])}\n"
        f"  - Not flagged: {format_count(result['not_flagged_condition'])}"
    )
    print(
        f"- Cases without the condition: {format_count(result['without_condition'])}\n"
        f"  - Flagged anyway: {format_count(result['flagged_without_condition'])}\n"
        f"  - Not flagged: {format_count(result['not_flagged_without_condition'])}"
    )
    print(f"- Total flagged: {format_count(result['total_flagged'])}")
    print(f"- Total not flagged: {format_count(result['total_not_flagged'])}")
    print()
    print(
        "P(condition given flagged) = "
        f"{format_count(result['flagged_condition'])} / {format_count(result['total_flagged'])} = "
        f"{format_probability_unrounded(result['probability_condition_given_flagged'])} -> "
        f"{format_probability(result['probability_condition_given_flagged'])}"
    )
    print(
        "P(condition given not flagged) = "
        f"{format_count(result['not_flagged_condition'])} / {format_count(result['total_not_flagged'])} = "
        f"{format_probability_unrounded(result['probability_condition_given_not_flagged'])} -> "
        f"{format_probability(result['probability_condition_given_not_flagged'])}"
    )
    print()
    print(
        "Teaching note: when the condition is rare, even a small false-alarm rate is applied to "
        "many more cases without the condition, so false flags can outnumber true flags."
    )


def print_comparison(results):
    rows = [
        [
            label,
            format_rate(result["base_rate"]),
            format_rate(result["catch_rate"]),
            format_rate(result["false_alarm_rate"]),
            format_count(result["flagged_condition"]),
            format_count(result["flagged_without_condition"]),
            format_count(result["total_flagged"]),
            format_probability(result["probability_condition_given_flagged"]),
            format_probability(result["probability_condition_given_not_flagged"]),
        ]
        for label, result in results
    ]
    headers = [
        "Scenario",
        "Base rate",
        "Catch rate",
        "False alarm",
        "True flags",
        "False flags",
        "Total flagged",
        "P(cond|flagged)",
        "P(cond|not flagged)",
    ]
    widths = [
        max(len(headers[i]), *(len(row[i]) for row in rows))
        for i in range(len(headers))
    ]

    def print_row(values):
        print(" | ".join(value.ljust(width) for value, width in zip(values, widths)))

    print_row(headers)
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print_row(row)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Build a base-rate decision tree and posterior probabilities."
    )
    parser.add_argument("--base-rate", default="2%", help="Base rate, for example 2%% or .02")
    parser.add_argument("--catch-rate", default="90%", help="Catch rate, for example 90%% or .90")
    parser.add_argument(
        "--false-alarm-rate",
        default="5%",
        help="False-alarm rate, for example 5%% or .05",
    )
    parser.add_argument(
        "--cases",
        default=10_000,
        type=int,
        help="Number of cases in the tree, default 10000",
    )
    parser.add_argument(
        "--label",
        default="Fraud detector scenario",
        help="Label for the main scenario",
    )
    parser.add_argument(
        "--compare",
        action="append",
        nargs=4,
        metavar=("LABEL", "BASE_RATE", "CATCH_RATE", "FALSE_ALARM_RATE"),
        help="Add a scenario to compare side by side",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    specs = [(args.label, args.base_rate, args.catch_rate, args.false_alarm_rate)]
    if args.compare:
        specs.extend(args.compare)

    parsed = []
    for label, base_rate, catch_rate, false_alarm_rate in specs:
        try:
            rates = (parse_rate(base_rate), parse_rate(catch_rate), parse_rate(false_alarm_rate))
            validate_rate("base_rate", rates[0])
            validate_rate("catch_rate", rates[1])
            validate_rate("false_alarm_rate", rates[2])
        except Exception as exc:
            parser.error(f"{label}: {exc}")
        parsed.append((label, rates))

    if args.cases <= 0:
        parser.error(f"cases must be positive; got {args.cases}")

    # One tree size for every scenario on the run. A scenario that needs a
    # bigger tree to stay whole drags the others up with it, because counts in
    # the comparison table only mean anything if every row counts the same
    # number of cases.
    common_cases = max(
        whole_number_cases(rates[0], rates[1], rates[2], Decimal(args.cases))
        for _, rates in parsed
    )

    scenarios = []
    for label, rates in parsed:
        try:
            result = calculate_base_rate_tree(
                rates[0], rates[1], rates[2], common_cases, requested_cases=args.cases
            )
        except Exception as exc:
            parser.error(f"{label}: {exc}")
        scenarios.append((label, result))

    print_scenario(scenarios[0][0], scenarios[0][1])

    if len(scenarios) > 1:
        print()
        print("Scenario comparison")
        print("===================")
        print_comparison(scenarios)


if __name__ == "__main__":
    main()
