from image.report_generator.utils.generic import style_str


class StyleStrings:
    @staticmethod
    def background_img():
        return style_str(styles={"top": 0, "left": 0})

    @staticmethod
    def text(additional_styles: dict = {}, **kwargs):
        return style_str(
            styles={
                "position": "absolute",
                "padding": 0,
                "margin": 0,
                "text-wrap": "nowrap",
                "top": kwargs["position"].y,
                "left": kwargs["position"].x,
                "font-family": f'"{kwargs["font_name"]}"',
                "font-size": kwargs["font_size"],
                "color": kwargs["font_color"],
                "text-align": kwargs["justify_content"],
                **additional_styles,
            }
        )

    @staticmethod
    def inline_text(additional_styles: dict = {}, **kwargs):
        return style_str(
            styles={
                "padding": 0,
                "margin": 0,
                "text-wrap": "nowrap",
                "font-family": f'"{kwargs["font_name"]}"',
                "font-size": kwargs["font_size"],
                "color": kwargs["font_color"],
                "text-align": kwargs["justify_content"],
                **additional_styles,
            }
        )

    @staticmethod
    def inline_img(additional_styles: dict = {}, **kwargs):
        return style_str(
            styles={
                "padding": 0,
                "margin": 0,
                "width": kwargs["size"],
                **additional_styles,
            }
        )

    @staticmethod
    def inline_elements(additional_styles: dict = {}, **kwargs):
        return style_str(
            styles={
                "position": "absolute",
                "align-items": "center",
                "padding": 0,
                "margin": 0,
                "text-wrap": "nowrap",
                "display": "flex",
                "flex-direction": "row",
                "top": kwargs["position"].y,
                "left": kwargs["position"].x,
                "text-align": kwargs["justify_content"],
                **additional_styles,
            }
        )

    @staticmethod
    def separator(additional_styles: dict = {}, **kwargs):
        return style_str(
            styles={
                "padding": 0,
                "margin": 0,
                "flex-direction": "row",
                "height": f"{kwargs['length']}px",
                "width": f"{kwargs['width']}px",
                "background-color": kwargs["color"],
                **additional_styles,
            }
        )

    @staticmethod
    def img(additional_styles: dict = {}, **kwargs):
        return style_str(
            styles={
                "padding": 0,
                "margin": 0,
                "position": "absolute",
                "top": kwargs["position"].y,
                "left": kwargs["position"].x,
                "width": f"{kwargs['width']}px",
                "height": f"{kwargs['height']}px",
                "object-fit": "contain",
                **additional_styles,
            }
        )
