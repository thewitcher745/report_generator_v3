"""
This file contains the templates with the QR codes and the referrals used by the users of the bot.
"""

TEMPLATES = {
    "binance": {
        "Board Main": {"qr": "binance_1", "referral": "237419134"},
        "Board Free": {"qr": "binance_1", "referral": "928356471"},
        "CAN Main": {"qr": "binance_2", "referral": "986438986"},
        "CAN Free": {"qr": "binance_6", "referral": "92435420"},
        "Turk Main": {"qr": "binance_3", "referral": "39164953"},
        "Turk Free": {"qr": "binance_4", "referral": "891972154"},
        "Extra 1": {"qr": "binance_7", "referral": "9746251829"},
        "Extra 2": {"qr": "binance_8", "referral": "8463691712"},
    },
    "bybit": {},
    "bitget": {},
    "mexc": {
        "Board Main": {"qr": "binance_1", "referral": "69r4f"},
        "Board Free": {"qr": "binance_5", "referral": "67x8w"},
        "CAN Main": {"qr": "binance_2", "referral": "34n5e"},
        "CAN Free": {"qr": "binance_6", "referral": "46k7u"},
        "Turk Main": {"qr": "binance_3", "referral": "58r3m"},
        "Turk Free": {"qr": "binance_4", "referral": "53h6r"},
        "Extra 1": {"qr": "binance_4", "referral": "79g2q"},
    },
    "bingx": {
        "Board Main": {
            "qr": "binance_2",
            "referral": "NKE6GL",
            "username": "al**7@gmail.com",
            "avatar": "bingx_board",
        },
        "Board Free": {
            "qr": "binance_6",
            "referral": "HRB7WN",
            "username": "al**7@gmail.com",
            "avatar": "bingx_board",
        },
        "CAN Main": {
            "qr": "binance_2",
            "referral": "NKE6GL",
            "username": "CAN PREMIUM",
            "avatar": "bingx_can",
        },
        "CAN Free": {
            "qr": "binance_6",
            "referral": "HRB7WN",
            "username": "CAN PREMIUM",
            "avatar": "bingx_can",
        },
        "Turk Main": {
            "qr": "binance_3",
            "referral": "SOV2XR",
            "username": "ta***1@gmail.com",
            "avatar": "bingx_turk",
        },
        "Turk Free": {
            "qr": "binance_4",
            "referral": "WMT6QJ",
            "username": "ta***1@gmail.com",
            "avatar": "bingx_turk",
        },
    },
    "okx": {},
    "lbank": {},
}


def get_templates_for_exchange(exchange: str) -> dict[str, dict[str, str]]:
    """
    Returns the templates for the given exchange.

    Args:
        exchange (str): The exchange to get the templates for.

    Returns:
        dict[str, dict[str, str]]: The templates for the given exchange.
    """

    return TEMPLATES[exchange]


def get_template(exchange: str, template_name: str) -> dict[str, str]:
    """
    Returns the template for the given exchange and template name.

    Args:
        exchange (str): The exchange to get the template for.
        template_name (str): The template name to get.

    Returns:
        dict[str, str]: The template for the given exchange and template name.
    """
    return TEMPLATES[exchange][template_name]
