"""
This dict contains a mapping of each image id to its relevant report class.
"""

from image.report_generator.report_classes.BaseReport import BaseReport
from image.report_generator.report_classes.mexc.Mexc7 import Mexc7
from image.report_generator.report_classes.binance.Binance6 import Binance6

MAPPING: dict[str, type[BaseReport]] = {
    "mexc_7": Mexc7,
    "binance_6": Binance6,
}
