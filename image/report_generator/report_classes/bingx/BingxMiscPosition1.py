from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class BingxMiscPosition1(BaseReport):
    def __init__(
        self,
        report_data: dict,
        extra_features: list[str] = [],
        drag_and_drop: bool = False,
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol()
        self.draw_signal_type_leverage_type_leverage_risk_bars()
        self.draw_pnl()
        self.draw_position_numbers()
        self.draw_entry(string_function=separate_price)
        self.draw_target(string_function=separate_price)

    def draw_signal_type_leverage_type_leverage_risk_bars(self):
        # Inline row: signal_type, leverage_type, leverage, risk bars
        st = self._get_element_styling("signal_type_leverage_type_leverage_risk_bars")

        # Signal type badge (Long/Short)
        signal_type = (self.signal_type or "").capitalize()
        is_short = signal_type == "Short"
        signal_type_color = st.color_short if is_short else st.color_long
        signal_type_box_color = st.box_color_short if is_short else st.box_color_long
        signal_type_box_radius = st.box_radius

        pos_el = self.report_html.create_inline_text(
            text=signal_type,
            font_name=st.font,
            font_size=st.font_size,
            font_color=signal_type_color,
            additional_styles={
                "background-color": signal_type_box_color,
                "border-radius": f"{signal_type_box_radius}px",
                "padding": f"{st.padding_y}px {st.padding_x}px",
                "margin-right": f"{st.spacing}px",
            },
        )

        # Leverage type badge (Cross/Isolated)
        lev_type_text = (self.report_data.get("leverage_type") or "").capitalize()
        lev_type_el = self.report_html.create_inline_text(
            text=lev_type_text,
            font_name=st.font,
            font_size=st.font_size,
            font_color=st.color,
            additional_styles={
                "background-color": getattr(st, "box_color", "#F4F4F4"),
                "border-radius": f"{signal_type_box_radius}px",
                "padding": f"{st.padding_y}px {st.padding_x}px",
                "margin-right": f"{st.spacing}px",
            },
        )

        # Leverage badge (e.g., 10X)
        lev_text = f"{self.leverage:g}X" if self.leverage else ""
        lev_el = self.report_html.create_inline_text(
            text=lev_text,
            font_name=st.font,
            font_size=st.font_size,
            font_color=st.color,
            additional_styles={
                "background-color": getattr(st, "box_color", "#F4F4F4"),
                "border-radius": f"{signal_type_box_radius}px",
                "margin-right": f"{st.spacing}px",
                "padding": f"{st.padding_y}px {st.padding_x}px",
            },
        )

        # Risk bars static image
        risk_bar_el = self.report_html.create_inline_img(
            img_src="../../../assets/bingx_risk_1.png",
            size=st.risk_bars_size,
            additional_styles={},
        )

        self.report_html.add_inline_elements(
            elements=[pos_el, lev_type_el, lev_el, risk_bar_el],
            position=st.position,
            justify_content="left",
        )

    def draw_pnl(self):
        # Left number and right percentage
        st_pnl = self._get_element_styling("pnl_usd")
        st_ratio = self._get_element_styling("pnl_percent")
        pnl = float(self.report_data.get("pnl_usd") or 0)
        pnl_str = ("+" if pnl >= 0 else "") + str(pnl)
        self.report_html.add_text(
            text=pnl_str,
            position=st_pnl.position,
            font_name=st_pnl.font,
            font_size=st_pnl.font_size,
            font_color=st_pnl.color,
        )

        ratio = float(self.report_data.get("pnl_percent") or 0)
        ratio_str = ("+" if ratio >= 0 else "") + f"{ratio:.2f}%"
        self.report_html.add_text(
            text=ratio_str,
            position=st_ratio.position,
            font_name=st_ratio.font,
            font_size=st_ratio.font_size,
            font_color=st_ratio.color,
            additional_styles={"transform": "translateX(-100%)"}
        )

    def draw_position_numbers(self):
        st_pos_amt = self._get_element_styling("position_amount")
        st_margin = self._get_element_styling("margin")
        st_risk = self._get_element_styling("risk")

        pos_amt = float(self.report_data.get("position_amount") or 0)
        margin = float(self.report_data.get("margin") or 0)
        risk_percent = self.report_data.get("risk_percent")

        self.report_html.add_text(
            text=f"{pos_amt:.2f}",
            position=st_pos_amt.position,
            font_name=st_pos_amt.font,
            font_size=st_pos_amt.font_size,
            font_color=st_pos_amt.color,
        )

        self.report_html.add_text(
            text=f"{margin:.4f}",
            position=st_margin.position,
            font_name=st_margin.font,
            font_size=st_margin.font_size,
            font_color=st_margin.color,
        )

        if risk_percent is not None:
            self.report_html.add_text(
                text=f"{float(risk_percent):.0f}%",
                position=st_risk.position,
                font_name=st_risk.font,
                font_size=st_risk.font_size,
                font_color=st_risk.color,
                additional_styles={"transform": "translateX(-100%)"}
            )
