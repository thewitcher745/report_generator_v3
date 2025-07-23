"""
This file will contain the keyboards put under each message or prompt.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# Get exchange keyboard
GET_EXCHANGE = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ByBit", callback_data="bybit"),
            InlineKeyboardButton("Binance", callback_data="binance"),
        ],
        [
            InlineKeyboardButton("BitGet", callback_data="bitget"),
            InlineKeyboardButton("MEXC", callback_data="mexc"),
        ],
        [
            InlineKeyboardButton("BingX", callback_data="bingx"),
            InlineKeyboardButton("OKX", callback_data="okx"),
        ],
        [
            InlineKeyboardButton("LBANK", callback_data="lbank"),
        ],
    ]
)


# Get image selection keyboard for a selected exchange
def GET_IMAGE(exchange):
    if exchange == "binance":
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Binance 1", callback_data="binance_1"),
                    InlineKeyboardButton("Binance 2", callback_data="binance_2"),
                ],
                [
                    InlineKeyboardButton("Binance 3", callback_data="binance_3"),
                    InlineKeyboardButton("Binance 4", callback_data="binance_4"),
                ],
                [
                    InlineKeyboardButton("Binance 5", callback_data="binance_5"),
                ],
            ]
        )

    elif exchange == "bybit":
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ByBit 4", callback_data="bybit_4"),
                    InlineKeyboardButton("ByBit 5", callback_data="bybit_5"),
                ]
            ]
        )

    elif exchange == "bitget":
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BitGet 1", callback_data="bitget_1"),
                    InlineKeyboardButton("BitGet 2", callback_data="bitget_2"),
                ],
                [
                    InlineKeyboardButton("BitGet 3", callback_data="bitget_3"),
                    InlineKeyboardButton("BitGet 4", callback_data="bitget_4"),
                ],
            ]
        )

    elif exchange == "mexc":
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("MEXC 1", callback_data="mexc_1"),
                    InlineKeyboardButton("MEXC 1 Turk", callback_data="mexc_2"),
                    InlineKeyboardButton("MEXC 1 Turk - Kapat", callback_data="mexc_3"),
                ],
                [
                    InlineKeyboardButton("MEXC 2", callback_data="mexc_4"),
                    InlineKeyboardButton("MEXC 3", callback_data="mexc_5"),
                    InlineKeyboardButton("MEXC 4", callback_data="mexc_6"),
                ],
            ]
        )

    elif exchange == "bingx":
        return InlineKeyboardMarkup(
            [
                [
                    # InlineKeyboardButton("BingX 1", callback_data="bingx_3"),
                    InlineKeyboardButton("BingX 1 - CAN", callback_data="bingx_1"),
                ],
                [
                    InlineKeyboardButton("BingX 1 - Ashan", callback_data="bingx_2"),
                ],
                [
                    InlineKeyboardButton("BingX 2", callback_data="bingx_5"),
                    InlineKeyboardButton("BingX 2 - CAN", callback_data="bingx_4"),
                ],
                [
                    InlineKeyboardButton("BingX 2 - Ashan", callback_data="bingx_6"),
                ],
                [
                    InlineKeyboardButton("BingX 3", callback_data="bingx_9"),
                    InlineKeyboardButton("BingX 3 - CAN", callback_data="bingx_7"),
                ],
                [
                    InlineKeyboardButton("BingX 3 - Board", callback_data="bingx_8"),
                ],
            ]
        )

    elif exchange == "okx":
        return InlineKeyboardMarkup(
            [[InlineKeyboardButton("OKX 1", callback_data="okx_1")]]
        )

    elif exchange == "lbank":
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("LBANK 1", callback_data="lbank_1"),
                    InlineKeyboardButton("LBANK 2", callback_data="lbank_2"),
                ]
            ]
        )
