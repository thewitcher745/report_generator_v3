from ..BaseReport import BaseReport


class Binance1(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol_signal_type_leverage()
        self.draw_roi()
        self.draw_entry()
        self.draw_target()
        self.draw_referral()
        self.draw_qr()

    def draw_symbol_signal_type_leverage(self):
        symbol_signal_type_leverage_style = self._get_element_styling(
            "symbol_signal_type_leverage"
        )

        signal_type_color = (
            symbol_signal_type_leverage_style.short_font_color
            if self.signal_type == "short"
            else symbol_signal_type_leverage_style.long_font_color
        )

        signal_type_element = self.report_html.create_inline_text(
            text=self.signal_type.capitalize(),
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=signal_type_color,
        )

        separator_1 = self.report_html.create_separator(
            color=symbol_signal_type_leverage_style.separator_color,
            width=symbol_signal_type_leverage_style.separator_width,
            length=symbol_signal_type_leverage_style.separator_length,
            additional_styles={
                "margin-left": f"{symbol_signal_type_leverage_style.gap_1_left}px",
                "margin-right": f"{symbol_signal_type_leverage_style.gap_1_right}px",
            },
        )

        leverage_element = self.report_html.create_inline_text(
            text=f"{self.leverage}x",
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=symbol_signal_type_leverage_style.color,
        )

        separator_2 = self.report_html.create_separator(
            color=symbol_signal_type_leverage_style.separator_color,
            width=symbol_signal_type_leverage_style.separator_width,
            length=symbol_signal_type_leverage_style.separator_length,
            additional_styles={
                "margin-left": f"{symbol_signal_type_leverage_style.gap_2_left}px",
                "margin-right": f"{symbol_signal_type_leverage_style.gap_2_right}px",
            },
        )

        symbol_element = self.report_html.create_inline_text(
            text=self.symbol,
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=symbol_signal_type_leverage_style.color,
        )

        self.report_html.add_inline_elements(
            elements=[
                signal_type_element,
                separator_1,
                leverage_element,
                separator_2,
                symbol_element,
            ],
            position=symbol_signal_type_leverage_style.position,
            justify_content="left",
        )
