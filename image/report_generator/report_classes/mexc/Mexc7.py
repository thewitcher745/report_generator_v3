from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class Mexc7(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_date(
            string_function=lambda x: x.strftime("Shared on %Y-%m-%d %H:%M:%S"),
            additional_styles={"letter-spacing": "0px"},
        )
        self.draw_symbol()
        self.draw_signal_type_leverage()
        self.draw_roi(additional_styles={"letter-spacing": "1px"})
        self.draw_roi_dollars(additional_styles={"letter-spacing": "1px"})
        self.draw_entry(
            string_function=lambda x: "$" + separate_price(x),
            additional_styles={"letter-spacing": "2px"},
        )
        self.draw_target(
            string_function=lambda x: "$" + separate_price(x),
            additional_styles={"letter-spacing": "2px"},
        )
        self.draw_input_date()
        self.draw_referral(additional_styles={"letter-spacing": "3px"})
        self.draw_qr()

    def draw_roi_dollars(self, additional_styles: dict[str, str] = {}):
        roi_dollars_styling = self._get_element_styling("roi_dollars")
        roi_dollars_string = f"{self.roi_dollars} USDT"
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=roi_dollars_string,
            position=roi_dollars_styling.position,
            font_name=roi_dollars_styling.font,
            font_size=roi_dollars_styling.font_size,
            font_color=roi_dollars_styling.color,
        )

    def draw_signal_type_leverage(self):
        signal_type_element = self.report_html.create_inline_text(
            text=f"Close {self.signal_type.capitalize()}",
            font_name=self._get_element_styling("signal_type_leverage").font,
            font_size=self._get_element_styling("signal_type_leverage").font_size,
            font_color=self._get_element_styling(
                "signal_type_leverage"
            ).signal_type_color,
        )
        separator = self.report_html.create_separator(
            color=self._get_element_styling("signal_type_leverage").separator_color,
            width=self._get_element_styling("signal_type_leverage").separator_width,
            length=self._get_element_styling("signal_type_leverage").separator_length,
            additional_styles={
                "margin": f"0px {self._get_element_styling('signal_type_leverage').gap / 2}px",
            },
        )
        leverage_element = self.report_html.create_inline_text(
            text=str(self.leverage) + "X",
            font_name=self._get_element_styling("signal_type_leverage").font,
            font_size=self._get_element_styling("signal_type_leverage").font_size,
            font_color=self._get_element_styling("signal_type_leverage").leverage_color,
        )

        self.report_html.add_inline_elements(
            elements=[signal_type_element, separator, leverage_element],
            position=self._get_element_styling("signal_type_leverage").position,
            justify_content="left",
            additional_styles={
                "letter-spacing": "1px",
            },
        )

    def draw_input_date(self):
        input_date_styling = self._get_element_styling("input_date")
        self.report_html.add_text(
            additional_styles={"letter-spacing": "1px"},
            text=self.input_date,
            position=input_date_styling.position,
            font_name=input_date_styling.font,
            font_size=input_date_styling.font_size,
            font_color=input_date_styling.color,
        )
