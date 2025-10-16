"""
This module contains the timezone deltas for the datetime strings in the reports.
"""

import datetime


tz_deltas = {
    "binance": datetime.timedelta(hours=2),
    "bingx": datetime.timedelta(hours=3),
    "bitget": datetime.timedelta(hours=-3),
    "lbank": datetime.timedelta(hours=3, minutes=30),
    "mexc": datetime.timedelta(hours=-1),
    "okx": datetime.timedelta(hours=-2),
    "kcex": datetime.timedelta(hours=3),
}


def get_tz_delta(exchange: str) -> datetime.timedelta:
    return tz_deltas.get(exchange.lower(), datetime.timedelta(hours=0))
