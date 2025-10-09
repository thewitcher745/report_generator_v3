"""
This module contains the base class for all reports, including the __init__ method.
"""

import datetime

from tg.handler_functions.helpers.extra_features import get_extra_features


class BaseReport:
    def __init__(self, report_data: dict):
        """
        Initializes the BaseReport class.

        Args:
            report_data (dict): The user data, taken from the context.report_data object of the bot.
        """

        self.report_data = report_data

        # These properties always exist, taken from the signal text.
        self.image_id: str = report_data.get("image_id", "")

        self.symbol: str = report_data.get("symbol", "")
        self.signal_type: str = report_data.get("signal_type", "")
        self.leverage: int = report_data.get("leverage", 0)
        self.entry: float = report_data.get("entry", 0)
        self.target: float = report_data.get("target", 0)
        self.roi_percent = report_data.get("roi_percent", 0)
        self.qr: str = report_data.get("qr", "")
        self.referral: str = report_data.get("referral", "")

        # The following properties may or may not exist in the report_data dictionary.
        if "username" in get_extra_features(self.image_id):
            self.username: str = report_data.get("username", "")
        if "date" in get_extra_features(self.image_id):
            self.tz_delta: int = report_data.get("tz_delta", 0)
            self.date: datetime.datetime = report_data.get(
                "date", datetime.datetime.now()
            )
        if "margin" in get_extra_features(image_id=self.image_id):
            self.roi_dollars: float = report_data.get("roi_dollars", 0)

    def print_info(self):
        """
        Prints all the properties of the BaseReport class.
        """
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def draw_roi(self):
        """
        Draws the ROI on the image.
        """
        pass
