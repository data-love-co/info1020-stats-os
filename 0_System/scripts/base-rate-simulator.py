#!/usr/bin/env python3
"""
base-rate-simulator.py: build a base-rate decision tree and posterior probabilities.

Run from the repo root:
    python 0_System/scripts/base-rate-simulator.py
    python 0_System/scripts/base-rate-simulator.py --base-rate 2% --catch-rate 90% --false-alarm-rate 5%
    python 0_System/scripts/base-rate-simulator.py \
        --compare "Fraud detector" 2% 90% 5% \
        --compare "Higher base rate" 10% 90% 5% \
        --compare "Lower base rate" .5% 90% 5%
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


def format_probability(value, places=2):
    rounded = value.quantize(Decimal("1").scaleb(-places), rounding=ROUND_HALF_UP)
    text = format(rounded, f".{places}f")
    if abs(rounded) < 1:
        if text.startswith("0"):
            text = text[1:]
        elif text.startswith("-0"):
            text = "-" + text[2:]
    return text


def format_probability_unrounded(value):
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    if abs(value) < 1:
        if text.startswith("0"):
            text = text[1:]
        elif text.startswith("-0"):
            text = "-" + text[2:]
    return text


def format_rate(value):
    percent = value * Decimal("100")
    text = format(percent, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return f"{text}%"


def calculate_base_rate_tree(base_rate, catch_rate, false_alarm_rate, cases=10_000):
    """
    Return raw tree counts and posterior probabilities for a base-rate problem.

    Inputs are decimal rates from 0 to 1 inclusive. Counts are returned without rounding.
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

    try:
        primary = calculate_base_rate_tree(
            parse_rate(args.base_rate),
            parse_rate(args.catch_rate),
            parse_rate(args.false_alarm_rate),
            args.cases,
        )
    except Exception as exc:
        parser.error(str(exc))

    print_scenario(args.label, primary)

    scenarios = [(args.label, primary)]
    if args.compare:
        for label, base_rate, catch_rate, false_alarm_rate in args.compare:
            try:
                result = calculate_base_rate_tree(
                    parse_rate(base_rate),
                    parse_rate(catch_rate),
                    parse_rate(false_alarm_rate),
                    args.cases,
                )
            except Exception as exc:
                parser.error(f"{label}: {exc}")
            scenarios.append((label, result))
        print()
        print("Scenario comparison")
        print("===================")
        print_comparison(scenarios)


if __name__ == "__main__":
    main()
