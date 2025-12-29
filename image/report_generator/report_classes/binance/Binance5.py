from ..BaseReport import BaseReport


class Binance5(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol(
            additional_styles={
                "letter-spacing": "0.2px",
                "left": "50%",
                "translate": "-50% 0",
            }
        )
        self.draw_signal_type(additional_styles={"left": "50%", "translate": "-50% 0"})
        self.draw_roi(
            additional_styles={"left": "50%", "translate": "-50% 0"},
            string_function=lambda roi: f"+{roi}".replace(".", ","),
        )
        self.draw_entry(
            additional_styles={"left": "28.9%", "translate": "-50% 0"},
            string_function=lambda entry: f"{entry}".replace(".", ","),
        )
        self.draw_target(
            additional_styles={"left": "70%", "translate": "-50% 0"},
            string_function=lambda target: f"{target}".replace(".", ","),
        )
        self.draw_referral(additional_styles={"letter-spacing": "-2px"})
        self.draw_qr()
        self.draw_date(
            additional_styles={"left": "50%", "translate": "-50% 0"},
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

    def draw_date(self, string_function=lambda x: x, additional_styles={}):
        if not (self.date and self.tz_delta):
            return

        date_style = self._get_element_styling("date")
        utc_offset = self._format_utc_offset()
        
        date_string = (
            "Shared on "
            + (self.date + self.tz_delta).strftime("%Y-%m-%d at %H:%M")
            + f"(UTC{utc_offset})"
        )

        # Create date part element
        self.report_html.add_text(
            text=date_string,
            font_name=date_style.font,
            font_size=date_style.font_size,
            font_color=date_style.color,
            position=date_style.position,
            additional_styles=additional_styles,
        )
