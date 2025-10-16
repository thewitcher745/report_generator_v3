import string
from tkinter.constants import X
from image.report_generator.utils.generic import separate_price
from ..BaseReport import BaseReport


class Kcex1(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        def price_string_function(x):
            return "$" + separate_price(x).replace(".", ",")

        self.draw_date(
            string_function=lambda x: x.strftime("%Y-%m-%d %H:%M:%S"),
        )
        self.draw_symbol(
            string_function=lambda x: x.replace(" Perpetual", "").replace(
                "USDT", " USDT Sürekli"
            ),
            additional_styles={"letter-spacing": "1px"},
        )
        self.draw_signal_type_leverage()
        self.draw_roi(
            string_function=lambda x: "+%" + str(self.roi_percent).replace(".", ",")
        )
        self.draw_entry(string_function=price_string_function)
        self.draw_target(string_function=price_string_function)
        self.draw_referral()
        self.draw_qr()

    def draw_signal_type_leverage(self):
        signal_type_color = (
            self._get_element_styling("signal_type").short_color
            if self.signal_type == "short"
            else self._get_element_styling("signal_type").long_color
        )
        signal_type_element = self.report_html.create_inline_text(
            text=f"{self.signal_type.capitalize()}",
            font_name=self._get_element_styling("signal_type").font,
            font_size=self._get_element_styling("signal_type").font_size,
            font_color=signal_type_color,
        )
        leverage_element = self.report_html.create_inline_text(
            text="/" + str(self.leverage) + "X",
            font_name=self._get_element_styling("leverage").font,
            font_size=self._get_element_styling("leverage").font_size,
            font_color=self._get_element_styling("leverage").color,
        )

        self.report_html.add_inline_elements(
            elements=[signal_type_element, leverage_element],
            position=self._get_element_styling("signal_type").position,
            justify_content="left",
        )
