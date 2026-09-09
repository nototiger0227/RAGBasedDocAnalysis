import re
from typing import Any


MULTIPLIERS = {
    "thousand": 1_000,
    "million": 1_000_000,
    "billion": 1_000_000_000,
    "trillion": 1_000_000_000_000,
    "crore": 10_000_000,
    "lakh": 100_000,
}


def parse_financial_value(display: Any) -> float | None:
    if not display:
        return None

    display = display.strip()

    if display.upper() == "NOT_FOUND":
        return None

    lower = display.lower().replace(",", "")

    # Percentages
    if "%" in lower:
        match = re.search(r"\d+(?:\.\d+)?", lower)
        return float(match.group()) if match else None

    multiplier = 1

    for unit, factor in MULTIPLIERS.items():
        if unit in lower:
            multiplier = factor
            break

    match = re.search(r"\d+(?:\.\d+)?", lower)

    if not match:
        return None

    return float(match.group()) * multiplier


def metric_response(display: Any) -> dict:
    display_str = str(display) if display is not None else None

    return {
        "display": display_str,
        "value": parse_financial_value(display_str)
    }