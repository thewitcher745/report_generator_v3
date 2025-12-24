from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class Bitget6(BaseReport):
    def __init__(
        self,
        report_data: dict,
        extra_features: list[str] = [],
        drag_and_drop: bool = False,
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_username(additional_styles={"letter-spacing": "-1px"})
        self.draw_symbol(string_function=lambda x: x.replace(" Perpetual", "").upper())
        self.draw_signal_type_leverage()
        self.draw_roi(string_function=lambda x: str(x) + "%")
        self.draw_entry(string_function=separate_price)
        self.draw_target(string_function=separate_price)
        self.draw_referral()
        self.draw_qr()
        self.draw_date(
            string_function=lambda x: f"{x.strftime('%Y-%m-%d %H:%M')} (UTC{self._format_utc_offset()})"
        )

    def _format_utc_offset(self) -> str:
        if not self.tz_delta:
            return "+0"

        total_minutes = int(self.tz_delta.total_seconds() / 60)
        sign = "+" if total_minutes >= 0 else "-"
        total_minutes = abs(total_minutes)
        hours, minutes = divmod(total_minutes, 60)
        if minutes == 0:
            return f"{sign}{hours}"
        return f"{sign}{hours}:{minutes:02d}"

    def draw_signal_type_leverage(self):
        signal_type_leverage_style = self._get_element_styling("signal_type_leverage")

        signal_type_color = (
            signal_type_leverage_style.short_color
            if self.signal_type == "short"
            else signal_type_leverage_style.long_color
        )
        perpetual_element = self.report_html.create_inline_text(
            text="Perpetual",
            font_name=signal_type_leverage_style.font,
            font_size=signal_type_leverage_style.font_size,
            font_color=signal_type_leverage_style.leverage_color,
            additional_styles={
                "letter-spacing": "-1px",
            },
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
        separator_1 = self.report_html.create_separator(
            color=signal_type_leverage_style.separator_color,
            width=signal_type_leverage_style.separator_width,
            length=signal_type_leverage_style.separator_length,
            additional_styles={
                "margin": f"0px {signal_type_leverage_style.gap / 2}px",
            },
        )
        separator_2 = self.report_html.create_separator(
            color=signal_type_leverage_style.separator_color,
            width=signal_type_leverage_style.separator_width,
            length=signal_type_leverage_style.separator_length,
            additional_styles={
                "margin": f"0px {signal_type_leverage_style.gap / 2}px",
            },
        )
        leverage_element = self.report_html.create_inline_text(
            text=str(self.leverage) + "x",
            font_name=signal_type_leverage_style.font,
            font_size=signal_type_leverage_style.font_size,
            font_color=signal_type_leverage_style.leverage_color,
        )

        self.report_html.add_inline_elements(
            elements=[
                perpetual_element,
                separator_1,
                signal_type_element,
                separator_2,
                leverage_element,
            ],
            position=signal_type_leverage_style.position,
            justify_content="left",
        )

    def draw_date(self, string_function=lambda x: x, additional_styles={}):
        if not (self.date and self.tz_delta):
            return

        date_style = self._get_element_styling("date")
        date_string = (self.date + self.tz_delta).strftime("%Y-%m-%d %H:%M")
        utc_offset = self._format_utc_offset()

        # Create date part element
        date_element = self.report_html.create_inline_text(
            text=date_string,
            font_name=date_style.font,
            font_size=date_style.font_size,
            font_color=date_style.color,
            additional_styles={
                "letter-spacing": "-2px",
            },
        )

        # Create UTC offset part element
        utc_element = self.report_html.create_inline_text(
            text=f"(UTC{utc_offset})",
            font_name=date_style.font,
            font_size=date_style.timezone_font_size,
            font_color=date_style.color,
            additional_styles={
                "margin-left": "10px",  # Small space between date and UTC
            },
        )

        # Add both elements in one line
        self.report_html.add_inline_elements(
            elements=[date_element, utc_element],
            position=date_style.position,
            justify_content="left",
        )

    def draw_qr(self):
        qr_styling = self._get_element_styling("qr")
        self.report_html.add_img(
            img_src=f"../../../qr/{self.qr}.png",
            position=qr_styling.position,
            width=qr_styling.size,
            height=qr_styling.size,
        )
