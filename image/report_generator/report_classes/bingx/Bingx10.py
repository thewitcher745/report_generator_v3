from ..BaseReport import BaseReport


class Bingx10(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_signal_type_leverage()
        self.draw_roi(additional_styles={"letter-spacing": "4px"})
        self.draw_entry(additional_styles={"letter-spacing": "1px"})
        self.draw_target(additional_styles={"letter-spacing": "1px"})
        self.draw_referral()
        self.draw_qr()
        self.draw_avatar()
        self.draw_username()

        self.draw_date(
            string_function=lambda date: f"{0 if date.month < 10 else ''}{date.month}/{0 if date.day < 10 else ''}{date.day} "
            + date.strftime("%H:%M")
        )

    def draw_signal_type_leverage(self):
        symbol_element = self.report_html.create_inline_text(
            text=f"{self.symbol.replace(' Perpetual', '').upper()}",
            font_name=self._get_element_styling("symbol").font,
            font_size=self._get_element_styling("symbol").font_size,
            font_color=self._get_element_styling("symbol").color,
        )
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
        separator_1 = self.report_html.create_separator(
            color=self._get_element_styling("symbol").separator_color,
            width=self._get_element_styling("symbol").separator_width,
            length=self._get_element_styling("symbol").separator_length,
            additional_styles={
                "margin": f"0px {self._get_element_styling('symbol').gap_1 / 2}px",
            },
        )
        separator_2 = self.report_html.create_separator(
            color=self._get_element_styling("symbol").separator_color,
            width=self._get_element_styling("symbol").separator_width,
            length=self._get_element_styling("symbol").separator_length,
            additional_styles={
                "margin": f"0px {self._get_element_styling('symbol').gap_2 / 2}px",
            },
        )
        leverage_element = self.report_html.create_inline_text(
            text=str(self.leverage) + "X",
            font_name=self._get_element_styling("leverage").font,
            font_size=self._get_element_styling("leverage").font_size,
            font_color=self._get_element_styling("leverage").color,
        )

        self.report_html.add_inline_elements(
            elements=[
                symbol_element,
                separator_1,
                signal_type_element,
                separator_2,
                leverage_element,
            ],
            position=self._get_element_styling("symbol").position,
            justify_content="left",
            additional_styles={
                "letter-spacing": "1px",
            },
        )
