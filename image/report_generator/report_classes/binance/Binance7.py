from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class Binance7(BaseReport):
    def __init__(
        self,
        report_data: dict,
        extra_features: list[str] = [],
        drag_and_drop: bool = False,
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_username(additional_styles={"letter-spacing": "-1px"})
        self.draw_date(
            string_function=lambda x: x.strftime("%Y-%m-%d %H:%M"),
            additional_styles={"letter-spacing": "1px"},
        )
        self.draw_symbol(additional_styles={"letter-spacing": "-1px"})
        self.draw_signal_type_leverage()
        self.draw_roi()
        self.draw_entry(
            string_function=separate_price, additional_styles={"letter-spacing": "-1px"}
        )
        self.draw_target(
            string_function=separate_price, additional_styles={"letter-spacing": "-1px"}
        )
        self.draw_referral()
        self.draw_qr()

    def draw_signal_type_leverage(self):
        st = self._get_element_styling("signal_type_leverage")
        signal_type_color = (
            st.short_color if self.signal_type == "short" else st.long_color
        )

        signal_type_element = self.report_html.create_inline_text(
            text=f"{self.signal_type.capitalize()}",
            font_name=st.font,
            font_size=st.font_size,
            font_color=signal_type_color,
            additional_styles={
                "letter-spacing": "-1px",
            },
        )
        separator = self.report_html.create_separator(
            color=st.separator_color,
            width=getattr(st, "separator_width", 2),
            length=getattr(st, "separator_length", 40),
            additional_styles={
                "margin": f"0px {getattr(st, 'gap', 18) / 2}px",
            },
        )
        leverage_element = self.report_html.create_inline_text(
            text=str(self.leverage) + "x",
            font_name=st.font,
            font_size=st.font_size,
            font_color=getattr(st, "leverage_color", "#999"),
        )

        self.report_html.add_inline_elements(
            elements=[signal_type_element, separator, leverage_element],
            position=st.position,
            justify_content="left",
        )
