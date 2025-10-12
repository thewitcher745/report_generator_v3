"""
This module contains the base class for all reports, including the __init__ method.
It also created the background, and adds the fonts to the report_html object.
"""

import datetime
from typing import Callable

from image.report_generator.utils.elements import ReportHTML
from image.report_generator.utils.generic import separate_price
from static.styling_dict import styling_dict


class BaseReport:
    def __init__(
        self, report_data: dict, extra_features: list = [], drag_and_drop: bool = False
    ):
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
        self.input_date: str = (
            report_data.get("input_date", "") if "input_date" in extra_features else ""
        )

        self.report_html = ReportHTML(drag_and_drop=drag_and_drop)
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
        # Don't add duplicates
        added_fonts = set()
        for element_styling in self.styling.values():
            if hasattr(element_styling, "font") and element_styling.font:
                font_filename = element_styling.font.split("/")[-1]
                if font_filename not in added_fonts:
                    self.report_html.add_font(font_filename)
                    added_fonts.add(font_filename)

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

    def draw_roi(
        self,
        string_function: Callable[[float], str] = lambda x: f"+{x}%",
        additional_styles: dict = {},
    ) -> None:
        """
        Draws the ROI of the report.
        """
        roi_styling = self._get_element_styling("roi")
        roi_string = string_function(self.roi_percent)
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=roi_string,
            position=roi_styling.position,
            font_name=roi_styling.font,
            font_size=roi_styling.font_size,
            font_color=roi_styling.color,
        )

    def draw_symbol(
        self,
        string_function: Callable[[str], str] = lambda x: x,
        additional_styles: dict = {},
    ) -> None:
        """
        Draws the symbol of the report.
        """
        symbol_styling = self._get_element_styling("symbol")
        symbol_string = string_function(self.symbol)
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=symbol_string,
            position=symbol_styling.position,
            font_name=symbol_styling.font,
            font_size=symbol_styling.font_size,
            font_color=symbol_styling.color,
        )

    def draw_signal_type(
        self,
        string_function: Callable[[str], str] = lambda x: x.capitalize(),
        additional_styles: dict = {},
    ) -> None:
        """
        Draws the signal type of the report.
        """
        signal_type_styling = self._get_element_styling("signal_type")
        signal_type_string = string_function(self.signal_type)
        color = (
            signal_type_styling.short_color
            if self.signal_type == "short"
            else signal_type_styling.long_color
        )
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=signal_type_string,
            position=signal_type_styling.position,
            font_name=signal_type_styling.font,
            font_size=signal_type_styling.font_size,
            font_color=color,
        )

    def draw_date(
        self,
        string_function: Callable[[datetime.datetime], str] = lambda x: x.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        additional_styles: dict = {},
    ):
        if self.date:
            date_styling = self._get_element_styling("date")
            date_string = string_function(self.date)
            self.report_html.add_text(
                additional_styles=additional_styles,
                text=date_string,
                position=date_styling.position,
                font_name=date_styling.font,
                font_size=date_styling.font_size,
                font_color=date_styling.color,
            )

    def draw_entry(
        self,
        string_function: Callable[[float], str] = lambda x: separate_price(x),
        additional_styles: dict = {},
    ):
        entry_styling = self._get_element_styling("entry")
        entry_string = string_function(self.entry)
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=entry_string,
            position=entry_styling.position,
            font_name=entry_styling.font,
            font_size=entry_styling.font_size,
            font_color=entry_styling.color,
        )

    def draw_target(
        self,
        string_function: Callable[[float], str] = lambda x: separate_price(x),
        additional_styles: dict = {},
    ):
        target_styling = self._get_element_styling("target")
        target_string = string_function(self.target)
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=target_string,
            position=target_styling.position,
            font_name=target_styling.font,
            font_size=target_styling.font_size,
            font_color=target_styling.color,
        )

    def draw_referral(
        self,
        string_function: Callable[[str], str] = lambda x: x,
        additional_styles: dict = {},
    ):
        if self.referral:
            referral_styling = self._get_element_styling("referral")
            referral_string = string_function(self.referral)
            self.report_html.add_text(
                additional_styles=additional_styles,
                text=referral_string,
                position=referral_styling.position,
                font_name=referral_styling.font,
                font_size=referral_styling.font_size,
                font_color=referral_styling.color,
            )

    def draw_qr(self):
        qr_styling = self._get_element_styling("qr")
        self.report_html.add_img(
            img_src=f"../../../qr/{self.qr}",
            position=qr_styling.position,
            width=qr_styling.size,
            height=qr_styling.size,
        )

    def save_html(self):
        """
        Saves the HTML of the report to a file.
        """
        self.report_html.save_html()
