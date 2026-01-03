from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class Binance8(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_avatar()
        self.draw_username(additional_styles={"letter-spacing": "-0.4px"})
        self.draw_date(
            string_function=lambda x: x.strftime("%Y-%m-%d %H:%M:%S"),
            additional_styles={"letter-spacing": "1px"},
        )
        self.draw_symbol()
        self.draw_signal_type_leverage()
        self.draw_roi(additional_styles={"letter-spacing": "9px"})
        self.draw_entry(string_function=separate_price)
        self.draw_target(string_function=separate_price)
        self.draw_referral()
        self.draw_qr()
        

    def draw_signal_type_leverage(self):
        signal_type_color = (
            self._get_element_styling("signal_type").short_color
            if self.signal_type == "short"
            else self._get_element_styling("signal_type").long_color
        )
        signal_type_element = self.report_html.create_inline_text(
            text=f"{self.signal_type.capitalize()}",
            font_name=self._get_element_styling("signal_type").font,
            font_size=self._get_element_styling("signal_type").font_size,
            font_color=signal_type_color,
            additional_styles={
                "letter-spacing": "-2px",
            },
        )
        separator = self.report_html.create_separator(
            color=self._get_element_styling("signal_type").separator_color,
            width=self._get_element_styling("signal_type").separator_width,
            length=self._get_element_styling("signal_type").separator_length,
            additional_styles={
                "margin": f"0px {self._get_element_styling('signal_type').gap / 2}px",
            },
        )
        leverage_element = self.report_html.create_inline_text(
            text=str(self.leverage) + "x",
            font_name=self._get_element_styling("leverage").font,
            font_size=self._get_element_styling("leverage").font_size,
            font_color=self._get_element_styling("leverage").color,
        )

        self.report_html.add_inline_elements(
            elements=[signal_type_element, separator, leverage_element],
            position=self._get_element_styling("signal_type").position,
            justify_content="left",
            additional_styles={
                "letter-spacing": "1px",
            },
        )
