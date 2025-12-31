from datetime import datetime
from ..BaseReport import BaseReport


class BybitTodaysPnl(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_pnl_usd(additional_styles={"letter-spacing": "-2px"})
        self.draw_input_date()
        self.draw_referral()
        self.draw_qr()

    def draw_pnl_usd(
        self,
        additional_styles: dict = {},
    ) -> None:
        """
        Draws the PNL (USD) of the report.
        """
        pnl_usd_styling = self._get_element_styling("pnl_usd")
        pnl_usd_string = "+" + str(self.pnl_usd)
        self.report_html.add_text(
            additional_styles=additional_styles,
            text=pnl_usd_string,
            position=pnl_usd_styling.position,
            font_name=pnl_usd_styling.font,
            font_size=pnl_usd_styling.font_size,
            font_color=pnl_usd_styling.color,
        )

    def draw_input_date(self):
        input_date_styling = self._get_element_styling("input_date")
        self.report_html.add_text(
            text=datetime.strptime(self.input_date, "%Y-%m-%d %H:%M:%S").strftime(
                "%Y-%m-%d %H:%M"
            ),
            position=input_date_styling.position,
            font_name=input_date_styling.font,
            font_size=input_date_styling.font_size,
            font_color=input_date_styling.color,
        )
