"""
This file contains the templates with the QR codes and the referrals used by the users of the bot.
"""

TEMPLATES = {
    "binance": {
        "Board Main": {
            "qr": "binance_1",
            "referral": "237419134",
            "username": "User-89p2j",
        },
        "Board Free": {
            "qr": "binance_1",
            "referral": "928356471",
            "username": "User-89p2j",
        },
        "CAN Main": {
            "qr": "binance_2",
            "referral": "986438986",
            "username": "User-33c8d",
        },
        "CAN Free": {
            "qr": "binance_6",
            "referral": "92435420",
            "username": "User-28c7w",
        },
        "Turk Main": {
            "qr": "binance_3",
            "referral": "39164953",
            "username": "User-27c4m",
        },
        "Turk Free": {
            "qr": "binance_4",
            "referral": "891972154",
            "username": "User-64q9n",
        },
        "Extra 1": {
            "qr": "binance_7",
            "referral": "9746251829",
            "username": "User-27c4mn",
        },
        "Extra 2": {
            "qr": "binance_8",
            "referral": "8463691712",
            "username": "User-34o2r",
        },
    },
    "bybit": {},
    "bitget": {
        "Board Main": {
            "qr": "bitget_1",
            "referral": "2BI76BMK",
            "username": "BGUSER-2BI76BMK",
        },
        "Board Free": {
            "qr": "bitget_1",
            "referral": "8LR12MLD",
            "username": "BGUSER-8LR12MLD",
        },
        "CAN Main": {
            "qr": "bitget_4",
            "referral": "1HN38KYX",
            "username": "BGUSER-1HN38KYX",
        },
        "CAN Free": {
            "qr": "bitget_5",
            "referral": "1WC67QCZ",
            "username": "BGUSER-1WC67QCZ",
        },
        "Turk Main": {
            "qr": "bitget_5",
            "referral": "SOV2XR",
            "username": "ta***1@gmail.com",
        },
        "Turk Free": {
            "qr": "bitget_4",
            "referral": "3VH98ACX",
            "username": "BGUSER-3VH98ACX",
        },
    },
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
            "qr": "bitget_1",
            "referral": "XJLYOF",
            "username": "al**7@gmail.com",
            "avatar": "bingx_board",
        },
        "Board Free": {
            "qr": "bitget_2",
            "referral": "XJLYOF",
            "username": "al**7@gmail.com",
            "avatar": "bingx_board",
        },
        "CAN Main": {
            "qr": "bitget_1",
            "referral": "YQOTZM",
            "username": "CAN PREMIUM",
            "avatar": "bingx_can",
        },
        "CAN Free": {
            "qr": "bitget_2",
            "referral": "HRB7WN",
            "username": "CAN PREMIUM",
            "avatar": "bingx_can",
        },
        "Turk Main": {
            "qr": "bitget_3",
            "referral": "OTYPQG",
            "username": "ta***1@gmail.com",
            "avatar": "bingx_turk",
        },
        "Turk Free": {
            "qr": "bitget_4",
            "referral": "WMT6QJ",
            "username": "ta***1@gmail.com",
            "avatar": "bingx_turk",
        },
    },
    "okx": {
        "Board Main": {"qr": "okx_1", "referral": "45618387"},
        "Board Free": {"qr": "okx_1", "referral": "15698429"},
        "CAN Main": {"qr": "okx_1", "referral": "46021351"},
        "CAN Free": {"qr": "okx_1", "referral": "19480578"},
        "Turk Main": {"qr": "okx_1", "referral": "34679461"},
        "Turk Free": {"qr": "okx_1", "referral": "15486230"},
    },
    "lbank": {
        "Board Main": {"qr": "lbank_1", "referral": "2SH6L"},
        "Board Free": {"qr": "lbank_1", "referral": "3CL4A"},
        "CAN Main": {"qr": "lbank_1", "referral": "3MG8F"},
        "CAN Free": {"qr": "lbank_1", "referral": "5KN7R"},
        "Turk Main": {"qr": "lbank_1", "referral": "9LS6N"},
        "Turk Free": {"qr": "lbank_1", "referral": "7NT9L"},
    },
    "kcex": {
        "Board Main": {"qr": "kcex_1", "referral": "421HBE"},
        "Board Free": {"qr": "kcex_2", "referral": "496KBR"},
        "CAN Main": {"qr": "kcex_1", "referral": "673HEQ"},
        "CAN Free": {"qr": "kcex_2", "referral": "743KEM"},
        "Turk Main": {"qr": "kcex_1", "referral": "276OLN"},
        "Turk Free": {"qr": "kcex_2", "referral": "962HRN"},
    },
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
