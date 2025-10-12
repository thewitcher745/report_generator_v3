"""
This module contains generic utility functions used in composing report images.
"""

from typing import Any, Mapping


def style_str(styles: Mapping[str, Any] | None) -> str:
    if not styles:
        return ""
    # Filter out None values and empty strings
    pairs = [f"{k}: {v}" for k, v in styles.items() if v not in (None, "")]
    return "style='" + "; ".join(pairs) + "'"
