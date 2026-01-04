"""
Central registry for custom extra features.
Each feature defines:
- prompt: Text shown to the user
- keyboard_id: Identifier for which keyboard to show ("DATE" | "TYPED")
- sanitize: Callable that converts user text -> stored value
- example (optional): Callable that returns an additional example text to send

Add new features here to have them automatically handled by the bot.
"""

from __future__ import annotations
from typing import Callable, Dict, Any, Optional, cast
import datetime

# Sanitizers


def sanitize_string(text: str) -> str:
    return text.strip()


def sanitize_float(text: str) -> float:
    return float(text.replace(",", "").strip())


def sanitize_percent(text: str) -> float:
    t = text.strip().replace("%", "").replace(",", "")
    return float(t)


def sanitize_symbol(text: str) -> str:
    # Keep quote currency (e.g., CHZUSDT); remove trailing " Perpetual" if present
    return text.upper().replace(" PERPETUAL", "").replace(" Perpetual", "").strip()


def sanitize_choice(valid: set[str]):
    def _inner(text: str) -> str:
        v = text.strip().lower()
        # Accept only known values; otherwise return as-is lowercased
        return v if v in valid else v

    return _inner


def sanitize_leverage_value(text: str) -> float:
    # Accept formats like "10", "10x", "10X"
    return float(text.strip().lower().replace("x", ""))


# Helper to generate a current datetime example string
def current_datetime_example() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Registry
EXTRA_FEATURES_CONFIG: Dict[str, Dict[str, Any]] = {
    # Generic/common ones
    "margin": {
        "prompt": "❓ Please enter the margin, since this image requires it:",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_float,
    },
    "username": {
        "prompt": "❓ Please enter the username, since this image requires it:",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_string,
    },
    # Date/time strings (YYYY-MM-DD HH:MM:SS)
    "input_date": {
        "prompt": "❓ Please enter a date and time. Format: YYYY-MM-DD HH:MM:SS",
        "keyboard_id": "DATE",
        "sanitize": sanitize_string,
        "example": current_datetime_example,
    },
    "period_start": {
        "prompt": "❓ Please enter the period start (YYYY-MM-DD HH:MM:SS):",
        "keyboard_id": "DATE",
        "sanitize": sanitize_string,
        "example": current_datetime_example,
    },
    "period_end": {
        "prompt": "❓ Please enter the period end (YYYY-MM-DD HH:MM:SS):",
        "keyboard_id": "DATE",
        "sanitize": sanitize_string,
        "example": current_datetime_example,
    },
    # Numbers
    "pnl_usd": {
        "prompt": "❓ Please enter the PnL in USD:",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_float,
    },
    "pnl_percent": {
        "prompt": "❓ Please enter the PnL in percent (e.g. 12.34):",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_float,
    },
    "input_symbol": {
        "prompt": "❓ Please enter the pair name (e.g. CHZUSDT):",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_symbol,
    },
    "input_signal_type": {
        "prompt": "❓ Please enter the signal type (long/short):",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_choice({"long", "short"}),
    },
    "leverage_type": {
        "prompt": "❓ Please enter the leverage type (cross/isolated):",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_choice({"cross", "isolated"}),
    },
    "input_leverage": {
        "prompt": "❓ Please enter the leverage (e.g. 10x):",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_leverage_value,
    },
    "risk_percent": {
        "prompt": "❓ Please enter the risk percent (e.g. 16):",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_percent,
    },
    "input_entry_price": {
        "prompt": "❓ Please enter the entry price:",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_float,
    },
    "input_target_price": {
        "prompt": "❓ Please enter the target/mark price:",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_float,
    },
    "liq_price": {
        "prompt": "❓ Please enter the liquidation price:",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_float,
    },
    "position_size": {
        "prompt": "❓ Please enter the position size:",
        "keyboard_id": "TYPED",
        "sanitize": sanitize_float,
    }
}


def get_feature_prompt(feature: str) -> str:
    return EXTRA_FEATURES_CONFIG[feature]["prompt"]


def get_feature_keyboard(update, context, feature: str):
    """Return the keyboard markup for the feature using keyboards helper.
    DATE -> keyboards.GET_DATE()
    TYPED -> keyboards.GET_TYPED_VALUE()
    """
    from tg.handler_functions.helpers import keyboards  # local import to avoid cycle

    keyboard_id = EXTRA_FEATURES_CONFIG[feature]["keyboard_id"]
    if keyboard_id == "DATE":
        return keyboards.GET_DATE()
    # Default typed value keyboard
    return keyboards.GET_TYPED_VALUE()


def sanitize_feature_value(feature: str, text: str):
    sanitizer: Callable[[str], Any] = EXTRA_FEATURES_CONFIG[feature]["sanitize"]
    return sanitizer(text)


def get_feature_example(feature: str) -> Optional[str]:
    example_cb = EXTRA_FEATURES_CONFIG[feature].get("example")
    if callable(example_cb):
        cb = cast(Callable[[], str], example_cb)
        return cb()
    return None
