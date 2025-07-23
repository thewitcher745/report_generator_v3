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
