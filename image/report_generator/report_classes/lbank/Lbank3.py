from ..BaseReport import BaseReport


class Lbank3(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol_signal_type_leverage()
        self.draw_roi()
        self.draw_entry()
        self.draw_target()
        self.draw_date()
        self.draw_referral()
        self.draw_qr()

    def draw_symbol_signal_type_leverage(self):
        symbol_signal_type_leverage_style = self._get_element_styling(
            "symbol_signal_type_leverage"
        )

        signal_type_color = (
            symbol_signal_type_leverage_style.short_color
            if self.signal_type == "short"
            else symbol_signal_type_leverage_style.long_color
        )

        # Format symbol: remove "Perpetual" and add " Perp"
        formatted_symbol = (
            self.symbol.lower().replace("perpetual", "").strip().upper() + " Perp"
        )

        symbol_element = self.report_html.create_inline_text(
            text=formatted_symbol,
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=symbol_signal_type_leverage_style.symbol_color,
        )

        separator_1 = self.report_html.create_separator(
            color=symbol_signal_type_leverage_style.separator_color,
            width=symbol_signal_type_leverage_style.separator_width,
            length=symbol_signal_type_leverage_style.separator_length,
            additional_styles={
                "margin": f"0px {symbol_signal_type_leverage_style.gap / 2}px",
            },
        )

        signal_type_element = self.report_html.create_inline_text(
            text=f"Open {self.signal_type.capitalize()}",
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=signal_type_color,
        )

        separator_2 = self.report_html.create_separator(
            color=symbol_signal_type_leverage_style.separator_color,
            width=symbol_signal_type_leverage_style.separator_width,
            length=symbol_signal_type_leverage_style.separator_length,
            additional_styles={
                "margin": f"0px {symbol_signal_type_leverage_style.gap / 2}px",
            },
        )

        leverage_element = self.report_html.create_inline_text(
            text=f"{self.leverage}X",
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=symbol_signal_type_leverage_style.leverage_color,
        )

        self.report_html.add_inline_elements(
            elements=[
                symbol_element,
                separator_1,
                signal_type_element,
                separator_2,
                leverage_element,
            ],
            position=symbol_signal_type_leverage_style.position,
            justify_content="left",
        )
