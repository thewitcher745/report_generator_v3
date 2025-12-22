from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class Mexc8(BaseReport):
    def __init__(
        self,
        report_data: dict,
        extra_features: list[str] = [],
        drag_and_drop: bool = False,
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol(
            string_function=lambda x: x.lower().replace("perpetual", "").strip().upper()
            + " Perpetual",
        )
        self.draw_signal_type_leverage()
        self.draw_roi()
        self.draw_entry(string_function=lambda x: "$" + separate_price(x))
        self.draw_target(string_function=lambda x: "$" + separate_price(x))
        self.draw_gen_date()
        self.draw_referral()
        self.draw_qr_code()

    def draw_gen_date(self):
        if self.date and self.tz_delta:
            date_styling = self._get_element_styling("date")
            date_string = (self.date + self.tz_delta).strftime(
                "Shared on %Y-%m-%d %H:%M:%S"
            )
            self.report_html.add_text(
                text=date_string,
                position=date_styling.position,
                font_name=date_styling.font,
                font_size=date_styling.font_size,
                font_color=date_styling.color,
            )

    def draw_signal_type_leverage(self):
        signal_type_leverage_style = self._get_element_styling("signal_type_leverage")
        signal_type_color = (
            signal_type_leverage_style.short_color
            if self.signal_type == "short"
            else signal_type_leverage_style.long_color
        )
        signal_type_element = self.report_html.create_inline_text(
            text=f"{self.signal_type.capitalize()}",
            font_name=signal_type_leverage_style.font,
            font_size=signal_type_leverage_style.font_size,
            font_color=signal_type_color,
            additional_styles={
                "letter-spacing": "-1px",
            },
        )
        separator = self.report_html.create_separator(
            color=signal_type_leverage_style.separator_color,
            width=2,
            length=40,
            additional_styles={
                "margin": "0 18px",
            },
        )
        leverage_element = self.report_html.create_inline_text(
            text=str(self.leverage) + "X",
            font_name=signal_type_leverage_style.font,
            font_size=signal_type_leverage_style.font_size,
            font_color="#999",
        )

        self.report_html.add_inline_elements(
            elements=[signal_type_element, separator, leverage_element],
            position=signal_type_leverage_style.position,
            justify_content="left",
        )

    def draw_qr_code(self):
        qr_styling = self._get_element_styling("qr_code")
        self.report_html.add_img(
            img_src=f"../../../qr/{self.qr}.png",
            position=qr_styling.position,
            width=qr_styling.size,
            height=qr_styling.size,
        )
