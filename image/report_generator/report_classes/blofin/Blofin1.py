from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class Blofin1(BaseReport):
    def __init__(
        self,
        report_data: dict,
        extra_features: list[str] = [],
        drag_and_drop: bool = False,
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_date(
            string_function=lambda x: x.strftime("%m-%d %H:%M:%S"),
            additional_styles={"letter-spacing": "-0.2px"},
        )
        self.draw_symbol(
            string_function=lambda x: (
                x.lower().replace("perpetual", "").strip().upper() + " Perp"
            ),
            additional_styles={"letter-spacing": "-0.5px"},
        )
        self.draw_signal_type_leverage()
        self.draw_roi(string_function=lambda x: f"+{x:.2f}%")
        self.draw_entry(
            string_function=separate_price, additional_styles={"letter-spacing": "0px"}
        )
        self.draw_target(
            string_function=separate_price, additional_styles={"letter-spacing": "0px"}
        )
        self.draw_referral()
        self.draw_qr()

    def draw_signal_type_leverage(self):
        st = self._get_element_styling("signal_type_leverage")
        font_color = st.short_color if self.signal_type == "short" else st.long_color

        signal_type_element = self.report_html.create_inline_text(
            text=f"{'Buy' if self.signal_type.lower() == 'long' else 'Sell'}",
            font_name=st.font,
            font_size=st.font_size,
            font_color=font_color,
            additional_styles={"letter-spacing": "-1px", "margin-right": "5px"},
        )
        leverage_element = self.report_html.create_inline_text(
            text=str(self.leverage) + "X",
            font_name=st.font,
            font_size=st.font_size,
            font_color=font_color,
        )

        self.report_html.add_inline_elements(
            elements=[signal_type_element, leverage_element],
            position=st.position,
            justify_content="left",
        )
