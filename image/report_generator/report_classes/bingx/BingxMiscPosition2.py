from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class BingxMiscPosition2(BaseReport):
    def __init__(
        self,
        report_data: dict,
        extra_features: list[str] = [],
        drag_and_drop: bool = False,
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol_logo()
        self.draw_signal_type_leverage_type_leverage()
        self.draw_pnl()
        self.draw_risk()
        self.draw_entry(additional_styles={"letter-spacing": "0.8px"})
        self.draw_target(additional_styles={"letter-spacing": "0.8px"})
        self.draw_position_numbers()
        self.draw_liq_price()

    def draw_symbol_logo(self):
        st = self._get_element_styling("symbol_logo")

        # Symbol inline text element
        symbol_el = self.report_html.create_inline_text(
            text=self.symbol,
            font_name=st.font,
            font_size=st.font_size,
            font_color=st.color,
            additional_styles={
                "letter-spacing": "0.6px",
                "margin-right": f"{st.spacing}px",
            },
        )

        # Logo inline img element
        logo_el = self.report_html.create_inline_img(
            img_src="../../../assets/bingx_logo.png",
            size=st.logo_size,
            additional_styles={},
        )

        self.report_html.add_inline_elements(
            elements=[symbol_el, logo_el],
            position=st.position,
            justify_content="left",
        )

    def draw_signal_type_leverage_type_leverage(self):
        # Inline row: signal_type, leverage_type, leverage
        st = self._get_element_styling("signal_type_leverage_type_leverage")

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
                "padding": f"{st.signal_type_padding_y}px {st.signal_type_padding_x}px",
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
                "padding": f"{st.leverage_type_padding_y}px {st.leverage_type_padding_x}px",
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
                "padding": f"{st.leverage_padding_y}px {st.leverage_padding_x}px",
            },
        )
        self.report_html.add_inline_elements(
            elements=[pos_el, lev_type_el, lev_el],
            position=st.position,
            justify_content="left",
        )

    def draw_pnl(self):
        # Inline USD amount and percentage with different font sizes
        st_pnl = self._get_element_styling("pnl")
        pnl_usd = float(self.report_data.get("pnl_usd") or 0)
        usd_str = "+" + str(pnl_usd)
        usd_el = self.report_html.create_inline_text(
            text=usd_str,
            font_name=st_pnl.font,
            font_size=st_pnl.usd_font_size,
            font_color=st_pnl.color,
        )

        pnl_percent = float(self.report_data.get("pnl_percent") or 0)
        ratio_str = "(+" + f"{pnl_percent:.2f}%)"
        percent_el = self.report_html.create_inline_text(
            text=ratio_str,
            font_name=st_pnl.font,
            font_size=st_pnl.percent_font_size,
            font_color=st_pnl.color,
            additional_styles={
                "position": "relative",
                "top": f"{st_pnl.percent_y_shift}px",
            },
        )

        self.report_html.add_inline_elements(
            elements=[usd_el, percent_el],
            position=st_pnl.position,
            justify_content="left",
            additional_styles={"transform": "translateX(-100%)"},
        )

    def draw_position_numbers(self):
        st_pos_amt = self._get_element_styling("position_amount")
        st_margin = self._get_element_styling("margin")

        pos_amt = float(self.report_data.get("position_amount") or 0)
        margin = float(self.report_data.get("margin") or 0)

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
            additional_styles={
                "background": f"linear-gradient(to right, {st_margin.border_color} 0%, {st_margin.border_color} 50%, transparent 50%, transparent 100%) repeat-x left bottom",
                "background-size": f"{st_margin.border_dash_length}px {st_margin.border_width}px",
                "padding": f"{st_margin.padding_y}px 0",
            },
        )

    def draw_risk(self):
        st_risk = self._get_element_styling("risk")
        risk_percent = self.report_data.get("risk_percent")

        if risk_percent is not None:
            self.report_html.add_text(
                text=f"{float(risk_percent):.2f}%",
                position=st_risk.position,
                font_name=st_risk.font,
                font_size=st_risk.font_size,
                font_color=st_risk.color,
                additional_styles={"transform": "translateX(-100%)"},
            )

    def draw_liq_price(self):
        st_liq_price = self._get_element_styling("liq_price")
        liq_price = self.report_data.get("liq_price")

        if liq_price is not None:
            self.report_html.add_text(
                text=f"{liq_price}",
                position=st_liq_price.position,
                font_name=st_liq_price.font,
                font_size=st_liq_price.font_size,
                font_color=st_liq_price.color,
                additional_styles={
                    "transform": "translateX(-100%)",
                    "background": f"linear-gradient(to right, {st_liq_price.border_color} 0%, {st_liq_price.border_color} 50%, transparent 50%, transparent 100%) repeat-x left bottom",
                    "background-size": f"{st_liq_price.border_dash_length}px {st_liq_price.border_width}px",
                    "padding": f"{st_liq_price.padding_y}px 0",
                },
            )
