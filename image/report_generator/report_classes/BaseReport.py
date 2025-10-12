"""
This module contains the base class for all reports, including the __init__ method.
It also created the background, and adds the fonts to the report_html object.
"""

import datetime

from image.report_generator.utils.elements import ReportHTML
from static.styling_dict import styling_dict


class BaseReport:
    def __init__(self, report_data: dict, extra_features: list = []):
        """
        Initializes the BaseReport class.

        Args:
            report_data (dict): The user data, taken from the context.report_data object of the bot.
        """

        self.report_data = report_data

        self.image_id: str = report_data.get("image_id", "")
        if self.image_id not in styling_dict:
            raise ValueError(f"Image ID {self.image_id} not found in styling_dict.")
        self.styling = styling_dict.get(self.image_id, {})

        # These properties always exist, taken from the signal text.
        self.symbol: str = report_data.get("symbol", "")
        self.signal_type: str = report_data.get("signal_type", "")
        self.leverage: int = report_data.get("leverage", 0)
        self.entry: float = report_data.get("entry", 0)
        self.target: float = report_data.get("target", 0)
        self.roi_percent = report_data.get("roi_percent", 0)
        self.qr: str = report_data.get("qr", "")
        self.referral: str = report_data.get("referral", "")

        # The following properties may or may not exist in the report_data dictionary.
        self.username: str | None = (
            report_data.get("username", None) if "username" in extra_features else None
        )
        self.tz_delta: int | None = (
            report_data.get("tz_delta", None) if "date" in extra_features else None
        )
        self.date: datetime.datetime | None = (
            report_data.get("date", None) if "date" in extra_features else None
        )
        self.roi_dollars: float | None = (
            report_data.get("roi_dollars", None) if "margin" in extra_features else None
        )

        self.report_html = ReportHTML()
        self.add_report_fonts()
        self.draw_background()

    def print_info(self):
        """
        Prints all the properties of the BaseReport class.
        """
        omitted_keys = ["styling", "fonts", "report_html", "report_data"]
        for key, value in self.__dict__.items():
            if value and key not in omitted_keys:
                print(f"{key}: {value}")

    def add_report_fonts(self):
        """
        Adds the fonts used in the report to the report_html object.
        """
        for element_styling in self.styling.values():
            if hasattr(element_styling, "font") and element_styling.font:
                font_filename = element_styling.font.split("/")[-1]
                self.report_html.add_font(font_filename)

    def draw_background(self):
        """
        Draws the background of the report.
        """
        img_src: str = f"../../../background_images/{self.image_id}.png"
        self.report_html.add_background(img_src)

    def _get_element_styling(self, element_name: str):
        """
        Returns the styling for the given element.
        """
        try:
            return self.styling.get(element_name, None)
        except KeyError:
            raise ValueError(f"Element {element_name} not found in styling.")
