from ..BaseReport import BaseReport


class Mexc6(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol()
        self.draw_signal_type_leverage()
        self.draw_roi()
        self.draw_entry(string_function=lambda entry: f"${entry}")
        self.draw_target(string_function=lambda target: f"${target}")
        self.draw_referral(additional_styles={"letter-spacing": "-2px"})
        self.draw_qr()
        self.draw_date()

    def draw_signal_type_leverage(self):
        symbol_signal_type_leverage_style = self._get_element_styling(
            "signal_type_leverage"
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

        leverage_element = self.report_html.create_inline_text(
            text=f"/{self.leverage}X",
            font_name=symbol_signal_type_leverage_style.font,
            font_size=symbol_signal_type_leverage_style.font_size,
            font_color=symbol_signal_type_leverage_style.color,
        )

        self.report_html.add_inline_elements(
            elements=[
                signal_type_element,
                leverage_element,
            ],
            position=symbol_signal_type_leverage_style.position,
            justify_content="left",
        )
