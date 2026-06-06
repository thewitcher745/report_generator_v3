from ..BaseReport import BaseReport


class Blofin1(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol()
        self.draw_signal_type_leverage()
        self.draw_roi()
        self.draw_entry()
        self.draw_target()
        self.draw_date()
        self.draw_referral()
        self.draw_qr()

    def draw_signal_type_leverage(self):
        signal_type_leverage_style = self._get_element_styling("signal_type_leverage")

        # Determine colors based on signal type
        signal_type_color = (
            signal_type_leverage_style.short_font_color
            if self.signal_type == "short"
            else signal_type_leverage_style.long_font_color
        )

        box_color = (
            signal_type_leverage_style.short_box_color
            if self.signal_type == "short"
            else signal_type_leverage_style.long_box_color
        )

        # Format symbol: remove "Perpetual" and add " Perp"
        formatted_symbol = self.symbol.lower().replace("perpetual", "").strip().upper()

        # Create symbol element with larger font
        symbol_element = self.report_html.create_inline_text(
            text=formatted_symbol,
            font_name=signal_type_leverage_style.symbol_font,
            font_size=signal_type_leverage_style.symbol_font_size,
            font_color="white",  # White color for symbol as shown in image
            additional_styles={"margin-right": f"{signal_type_leverage_style.gap}px"},
        )

        # Create signal type text
        signal_type_leverage_element = self.report_html.create_inline_text(
            text=f"{self.signal_type.capitalize()} {self.leverage:.1f}X",
            font_name=signal_type_leverage_style.signal_type_leverage_font,
            font_size=signal_type_leverage_style.signal_type_leverage_font_size,
            font_color=signal_type_color,
            additional_styles={
                "padding": f"{signal_type_leverage_style.box_padding_y}px {signal_type_leverage_style.box_padding_x}px",
                "background-color": box_color,
                "border-radius": f"{signal_type_leverage_style.box_radius}px",
            },
        )

        # Add all elements as inline elements
        self.report_html.add_inline_elements(
            elements=[
                symbol_element,
                signal_type_leverage_element,
            ],
            position=signal_type_leverage_style.position,
            justify_content="left",
        )
