from image.report_generator.report_classes.okx.okx_logo import get_okx_logo
from ..BaseReport import BaseReport


class Okx2(BaseReport):
    def __init__(
        self, report_data: dict, extra_features: list[str] = [], drag_and_drop=False
    ) -> None:
        super().__init__(report_data, extra_features, drag_and_drop)

        self.draw_symbol()
        self.draw_signal_type_leverage()
        self.draw_roi(additional_styles={"letter-spacing": "-2px"})
        self.draw_entry(additional_styles={"transform": "translateX(-100%)"})
        self.draw_target(additional_styles={"transform": "translateX(-100%)"})
        self.draw_referral(string_function=lambda x: "okx.com/join/" + str(x))
        self.draw_qr()
        self.draw_logo(additional_styles={"border-radius": "100%"})

    def draw_signal_type_leverage(self):
        font = self._get_element_styling("signal_type_leverage").font
        font_size = self._get_element_styling("signal_type_leverage").font_size
        color = self._get_element_styling("signal_type_leverage").color

        signal_type_element = self.report_html.create_inline_text(
            text=f"{'Buy' if self.signal_type.lower() == 'long' else 'Sell'}",
            font_name=font,
            font_size=font_size,
            font_color=color,
            additional_styles={
                "letter-spacing": "-1px",
            },
        )

        separator = self.report_html.create_separator(
            color=self._get_element_styling("signal_type_leverage").separator_color,
            width=self._get_element_styling("signal_type_leverage").separator_width,
            length=self._get_element_styling("signal_type_leverage").separator_length,
            additional_styles={
                "margin": f"0px {self._get_element_styling('signal_type_leverage').gap / 2}px",
            },
        )

        leverage_element = self.report_html.create_inline_text(
            text=f"{self.leverage:.2f}" + "x",
            font_name=font,
            font_size=font_size,
            font_color=color,
        )

        closed_element = self.report_html.create_inline_text(
            text="Closed",
            font_name=font,
            font_size=font_size,
            font_color=color,
        )

        self.report_html.add_inline_elements(
            elements=[
                signal_type_element,
                separator,
                leverage_element,
                separator,
                closed_element,
            ],
            position=self._get_element_styling("signal_type_leverage").position,
            justify_content="left",
        )

    def draw_logo(self, additional_styles: dict = {}):
        logo_styling = self._get_element_styling("logo")

        additional_styles.update({"aspect-ratio": "1/1"})
        logo_link = get_okx_logo(self.symbol)
        if logo_link:
            self.report_html.add_img(
                additional_styles=additional_styles,
                img_src=logo_link,
                position=logo_styling.position,
                width=logo_styling.size,
                height=logo_styling.size,
            )
