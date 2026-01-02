from datetime import datetime

from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class BybitCumulativePnl(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_pnl_percent(additional_styles={"letter-spacing": "-2px"})
        self.draw_pnl_usd(additional_styles={"letter-spacing": "-2px"})
        self.draw_period_start()
        self.draw_period_end()
        self.draw_referral()
        self.draw_qr()

    def draw_pnl_percent(self, additional_styles: dict = {}) -> None:
        pnl_percent_styling = self._get_element_styling("pnl_percent")
        pnl_percent_string = "+" + str(self.pnl_percent) + "%"
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=pnl_percent_string,
            position=pnl_percent_styling.position,
            font_name=pnl_percent_styling.font,
            font_size=pnl_percent_styling.font_size,
            font_color=pnl_percent_styling.color,
        )

    def draw_pnl_usd(self, additional_styles: dict = {}) -> None:
        pnl_usd_styling = self._get_element_styling("pnl_usd")
        pnl_usd_string = "+" + separate_price(str(self.pnl_usd))
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=pnl_usd_string,
            position=pnl_usd_styling.position,
            font_name=pnl_usd_styling.font,
            font_size=pnl_usd_styling.font_size,
            font_color=pnl_usd_styling.color,
        )

    def draw_period_start(self):
        period_start_styling = self._get_element_styling("period_start")
        start_str = datetime.strptime(self.period_start, "%Y-%m-%d %H:%M:%S").strftime(
            "%Y-%m-%d %H:%M"
        )
        self.report_html.add_text(
            text=f"{start_str} -",
            position=period_start_styling.position,
            font_name=period_start_styling.font,
            font_size=period_start_styling.font_size,
            font_color=period_start_styling.color,
            additional_styles={"letter-spacing": "0.2px"},
        )

    def draw_period_end(self):
        period_end_styling = self._get_element_styling("period_end")
        end_str = datetime.strptime(self.period_end, "%Y-%m-%d %H:%M:%S").strftime(
            "%Y-%m-%d %H:%M"
        )
        self.report_html.add_text(
            text=end_str,
            position=period_end_styling.position,
            font_name=period_end_styling.font,
            font_size=period_end_styling.font_size,
            font_color=period_end_styling.color,
            additional_styles={"letter-spacing": "0"},
        )
