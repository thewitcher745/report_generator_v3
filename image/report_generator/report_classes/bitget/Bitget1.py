from ..BaseReport import BaseReport


class Bitget1(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol_signal_type()
        self.draw_roi_dollars()
        self.draw_entry()
        self.draw_target()
        self.draw_date(string_function=lambda x: x.strftime("%Y-%m-%d %H:%M"))
        self.draw_referral()
        self.draw_qr()
        self.draw_username()
        self.draw_username_id()

    def draw_symbol_signal_type(self):
        symbol_signal_type_style = self._get_element_styling("symbol_signal_type")

        # Determine colors based on signal type
        signal_type_color = (
            symbol_signal_type_style.short_color
            if self.signal_type == "short"
            else symbol_signal_type_style.long_color
        )

        # Format symbol: remove "Perpetual" and add " Perp"
        formatted_symbol = self.symbol.lower().replace("perpetual", "").strip().upper()

        # Create symbol element
        symbol_element = self.report_html.create_inline_text(
            text=formatted_symbol,
            font_name=symbol_signal_type_style.font,
            font_size=symbol_signal_type_style.font_size,
            font_color=symbol_signal_type_style.color,
            additional_styles={"margin-right": f"{symbol_signal_type_style.gap_1}px"},
        )

        # Create signal type element
        signal_type_element = self.report_html.create_inline_text(
            text=self.signal_type.capitalize(),
            font_name=symbol_signal_type_style.font,
            font_size=symbol_signal_type_style.font_size,
            font_color=signal_type_color,
        )

        # Create separator element (visual line)
        separator = self.report_html.create_separator(
            color=symbol_signal_type_style.color,
            width=symbol_signal_type_style.separator_width,
            length=symbol_signal_type_style.separator_length,
            additional_styles={
                "margin-left": f"{symbol_signal_type_style.gap_2_left}px",
                "margin-right": f"{symbol_signal_type_style.gap_2_right}px",
            },
        )

        # Create "Cross" element
        cross_element = self.report_html.create_inline_text(
            text="Cross",
            font_name=symbol_signal_type_style.font,
            font_size=symbol_signal_type_style.font_size,
            font_color=symbol_signal_type_style.color,
        )

        # Add all elements as inline elements
        self.report_html.add_inline_elements(
            elements=[
                symbol_element,
                signal_type_element,
                separator,
                cross_element,
            ],
            position=symbol_signal_type_style.position,
            justify_content="left",
        )

    def draw_roi_dollars(
        self,
        additional_styles: dict = {},
    ) -> None:
        """
        Draws the ROI of the report.
        """
        roi_styling = self._get_element_styling("roi_dollars")
        roi_string = "+" + str(self.roi_dollars)
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=roi_string,
            position=roi_styling.position,
            font_name=roi_styling.font,
            font_size=roi_styling.font_size,
            font_color=roi_styling.color,
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
        date_string = (self.date + self.tz_delta).strftime("%Y-%m-%d %H:%M")
        utc_offset = self._format_utc_offset()

        # Create date part element
        date_element = self.report_html.create_inline_text(
            text=date_string,
            font_name=date_style.font,
            font_size=date_style.font_size,
            font_color=date_style.color,
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

    def draw_username_id(self):
        # Draws the username with styling of "username_id" with an @ before it.
        username_id_styling = self._get_element_styling("username_id")
        username_id_string = "@" + self.username
        self.report_html.add_text(
            text=username_id_string,
            position=username_id_styling.position,
            font_name=username_id_styling.font,
            font_size=username_id_styling.font_size,
            font_color=username_id_styling.color,
        )
