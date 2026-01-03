from ..BaseReport import BaseReport


class Bybit4(BaseReport):
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

        # Determine colors based on signal type
        signal_type_color = (
            symbol_signal_type_leverage_style.short_font_color
            if self.signal_type == "short"
            else symbol_signal_type_leverage_style.long_font_color
        )

        box_color = (
            symbol_signal_type_leverage_style.short_box_color
            if self.signal_type == "short"
            else symbol_signal_type_leverage_style.long_box_color
        )

        # Format symbol: remove "Perpetual" and add " Perp"
        formatted_symbol = self.symbol.lower().replace("perpetual", "").strip().upper()

        # Create symbol element with larger font
        symbol_element = self.report_html.create_inline_text(
            text=formatted_symbol,
            font_name=symbol_signal_type_leverage_style.symbol_font,
            font_size=symbol_signal_type_leverage_style.symbol_font_size,
            font_color="white",  # White color for symbol as shown in image
            additional_styles={
                "margin-right": f"{symbol_signal_type_leverage_style.gap}px"
            },
        )
        
        # Create signal type text
        signal_type_leverage_element = self.report_html.create_inline_text(
            text=f"{self.signal_type.capitalize()} {self.leverage:.1f}X",
            font_name=symbol_signal_type_leverage_style.signal_type_leverage_font,
            font_size=symbol_signal_type_leverage_style.signal_type_leverage_font_size,
            font_color=signal_type_color,
            additional_styles={
                "padding": f"{symbol_signal_type_leverage_style.box_padding_y}px {symbol_signal_type_leverage_style.box_padding_x}px",
                "background-color": box_color,
                "border-radius": f"{symbol_signal_type_leverage_style.box_radius}px",
            },
        )

        # Add all elements as inline elements
        self.report_html.add_inline_elements(
            elements=[
                symbol_element,
                signal_type_leverage_element,
            ],
            position=symbol_signal_type_leverage_style.position,
            justify_content="left",
        )
