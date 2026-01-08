from ..BaseReport import BaseReport


class Lbank1(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol_perp_futures()
        self.draw_close_signal_leverage()
        self.draw_roi(string_function=lambda x: f"+{x}%")
        self.draw_entry()
        self.draw_target()
        self.draw_referral()
        self.draw_qr()
        self.draw_date(string_function=lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))

    def draw_symbol_perp_futures(self):
        style = self._get_element_styling("symbol_perp_futures")

        formatted_symbol = (
            self.symbol.lower().replace("perpetual", "").strip().upper() + " Perp"
        )

        symbol_element = self.report_html.create_inline_text(
            text=formatted_symbol,
            font_name=style.symbol_font,
            font_size=style.symbol_font_size,
            font_color=style.symbol_color,
        )

        futures_element = self.report_html.create_inline_text(
            text="Futures",
            font_name=style.pill_font,
            font_size=style.pill_font_size,
            font_color=style.pill_text_color,
            additional_styles={
                "padding": f"{style.pill_padding_y}px {style.pill_padding_x}px",
                "background-color": style.pill_bg_color,
                "border-radius": f"{style.pill_radius}px",
            },
        )

        self.report_html.add_inline_elements(
            elements=[symbol_element, futures_element],
            position=style.position,
            justify_content="left",
            additional_styles={
                "gap": f"{style.gap}px",
            },
        )

    def draw_close_signal_leverage(self):
        style = self._get_element_styling("close_signal_leverage")

        signal_type_color = (
            style.short_color if self.signal_type == "short" else style.long_color
        )

        signal_type_element = self.report_html.create_inline_text(
            text="Close " + self.signal_type.capitalize(),
            font_name=style.font,
            font_size=style.font_size,
            font_color=signal_type_color,
        )

        separator = self.report_html.create_inline_text(
            text="|",
            font_name=style.font,
            font_size=style.font_size,
            font_color=style.separator_color,
            additional_styles={
                "margin": f"0px {style.separator_margin_x}px",
            },
        )

        leverage_element = self.report_html.create_inline_text(
            text=f"{int(self.leverage)}X",
            font_name=style.font,
            font_size=style.font_size,
            font_color=style.leverage_color,
        )

        self.report_html.add_inline_elements(
            elements=[signal_type_element, separator, leverage_element],
            position=style.position,
            justify_content="left",
        )
