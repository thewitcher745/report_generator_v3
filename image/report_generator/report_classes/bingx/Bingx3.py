from ..BaseReport import BaseReport


class Bingx3(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol_signal_type_leverage()
        self.draw_roi(additional_styles={"letter-spacing": "1.5px"})
        self.draw_entry()
        self.draw_target()
        self.draw_referral(additional_styles={"letter-spacing": "-2px"})
        self.draw_qr()
        self.draw_avatar()
        self.draw_username(additional_styles={"letter-spacing": "-2px"})
        self.draw_date(string_function=lambda date: date.strftime("%d/%m %H:%M"))

    def draw_symbol_signal_type_leverage(self):
        symbol_signal_type_leverage_style = self._get_element_styling(
            "symbol_signal_type_leverage"
        )

        signal_type_color = (
            symbol_signal_type_leverage_style.short_font_color
            if self.signal_type == "short"
            else symbol_signal_type_leverage_style.long_font_color
        )

        symbol_element = self.report_html.create_inline_text(
            text=f"{self.symbol.replace(' Perpetual', '').upper()}",
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=symbol_signal_type_leverage_style.color,
            additional_styles={"letter-spacing": "0.8px"},
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

        signal_type_element = self.report_html.create_inline_text(
            text=f"{self.signal_type.capitalize()}",
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=signal_type_color,
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

        leverage_element = self.report_html.create_inline_text(
            text=f"{self.leverage:.0f}X",
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=symbol_signal_type_leverage_style.color,
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
