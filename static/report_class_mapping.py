"""
This dict contains a mapping of each image id to its relevant report class.
"""

from image.report_generator.report_classes.BaseReport import BaseReport
from image.report_generator.report_classes.okx.Okx2 import Okx2
from image.report_generator.report_classes.bybit.Bybit4 import Bybit4
from image.report_generator.report_classes.bybit.Bybit5 import Bybit5
from image.report_generator.report_classes.bybit.BybitTodaysPnl import BybitTodaysPnl
from image.report_generator.report_classes.bybit.BybitCumulativePnl import (
    BybitCumulativePnl,
)
from image.report_generator.report_classes.bitget.Bitget1 import Bitget1
from image.report_generator.report_classes.bitget.Bitget5 import Bitget5
from image.report_generator.report_classes.bitget.Bitget6 import Bitget6
from image.report_generator.report_classes.bingx.Bingx10 import Bingx10
from image.report_generator.report_classes.bingx.BingxMiscPosition1 import (
    BingxMiscPosition1,
)
from image.report_generator.report_classes.bingx.BingxMiscPosition2 import (
    BingxMiscPosition2,
)
from image.report_generator.report_classes.mexc.Mexc5 import Mexc5
from image.report_generator.report_classes.mexc.Mexc6 import Mexc6
from image.report_generator.report_classes.mexc.Mexc7 import Mexc7
from image.report_generator.report_classes.mexc.Mexc8 import Mexc8
from image.report_generator.report_classes.binance.Binance1 import Binance1
from image.report_generator.report_classes.binance.Binance2 import Binance2
from image.report_generator.report_classes.binance.Binance3 import Binance3
from image.report_generator.report_classes.binance.Binance4 import Binance4
from image.report_generator.report_classes.binance.Binance5 import Binance5
from image.report_generator.report_classes.binance.Binance6 import Binance6
from image.report_generator.report_classes.binance.Binance7 import Binance7
from image.report_generator.report_classes.binance.Binance8 import Binance8
from image.report_generator.report_classes.kcex.Kcex1 import Kcex1
from image.report_generator.report_classes.lbank.Lbank3 import Lbank3

MAPPING: dict[str, type[BaseReport]] = {
    "okx_2": Okx2,
    "bybit_4": Bybit4,
    "bybit_5": Bybit5,
    "bybit_todays_pnl": BybitTodaysPnl,
    "bybit_cumulative_pnl": BybitCumulativePnl,
    "bitget_1": Bitget1,
    "bitget_5": Bitget5,
    "bitget_6": Bitget6,
    "bingx_10": Bingx10,
    "bingx_misc_position_1": BingxMiscPosition1,
    "bingx_misc_position_2": BingxMiscPosition2,
    "mexc_5": Mexc5,
    "mexc_6": Mexc6,
    "mexc_7": Mexc7,
    "mexc_8": Mexc8,
    "binance_1": Binance1,
    "binance_2": Binance2,
    "binance_3": Binance3,
    "binance_4": Binance4,
    "binance_5": Binance5,
    "binance_6": Binance6,
    "binance_7": Binance7,
    "binance_8": Binance8,
    "kcex_1": Kcex1,
    "lbank_3": Lbank3,
}
