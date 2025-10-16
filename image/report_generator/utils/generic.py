"""
This module contains generic utility functions used in composing report images.
"""

import json
from typing import Any, Mapping
from decimal import Decimal


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ElementStyling:
    def __init__(self, **params):
        self.position: Position | None = params.get("position", None)
        for key in params.keys():
            self.__setattr__(key, params[key])


def style_str(styles: Mapping[str, Any] | None) -> str:
    if not styles:
        return ""
    # Filter out None values and empty strings
    pairs = [f"{k}: {v}" for k, v in styles.items() if v not in (None, "")]
    return "style='" + "; ".join(pairs) + "'"


def separate_price(price_str) -> str:
    """
    Separates the integer part of a price float into groups of three digits.
    """
    # Use Decimal to avoid scientific notation and preserve decimal part
    s = format(Decimal(str(price_str)), "f")
    sign = ""
    if s.startswith("-"):
        sign = "-"
        s = s[1:]
    if "." in s:
        int_part, frac_part = s.split(".", 1)
    else:
        int_part, frac_part = s, ""
    int_formatted = f"{int(int_part):,}" if int_part else "0"
    return sign + int_formatted + (f".{frac_part}" if frac_part != "" else "")


def get_logo_link(symbol: str) -> str:
    with open("./image/report_generator/utils/logo_links.json", "r") as fs:
        logo_links: dict = json.load(fs)

    symbol = symbol.replace(" Perpetual", "").replace("USDT", "").upper()
    return logo_links[symbol]
