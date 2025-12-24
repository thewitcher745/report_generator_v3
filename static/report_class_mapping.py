"""
This dict contains a mapping of each image id to its relevant report class.
"""

from image.report_generator.report_classes.BaseReport import BaseReport
from image.report_generator.report_classes.okx.Okx2 import Okx2
from image.report_generator.report_classes.bitget.Bitget5 import Bitget5
from image.report_generator.report_classes.bitget.Bitget6 import Bitget6
from image.report_generator.report_classes.bingx.Bingx10 import Bingx10
from image.report_generator.report_classes.mexc.Mexc7 import Mexc7
from image.report_generator.report_classes.mexc.Mexc8 import Mexc8
from image.report_generator.report_classes.binance.Binance6 import Binance6
from image.report_generator.report_classes.binance.Binance7 import Binance7
from image.report_generator.report_classes.kcex.Kcex1 import Kcex1

MAPPING: dict[str, type[BaseReport]] = {
    "okx_2": Okx2,
    "bitget_5": Bitget5,
    "bitget_6": Bitget6,
    "bingx_10": Bingx10,
    "mexc_7": Mexc7,
    "mexc_8": Mexc8,
    "binance_6": Binance6,
    "binance_7": Binance7,
    "kcex_1": Kcex1,
}
