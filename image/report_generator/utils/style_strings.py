from image.report_generator.utils.generic import style_str


class StyleStrings:
    @staticmethod
    def background_img():
        return style_str(styles={"position": "absolute", "top": 0, "left": 0})

    @staticmethod
    def text(**kwargs):
        return style_str(
            styles={
                "position": "absolute",
                "top": kwargs["position"][1],
                "left": kwargs["position"][0],
                "font-family": kwargs["font_name"],
                "font-size": kwargs["font_size"],
                "color": kwargs["font_color"],
                "text-align": kwargs["justify_content"],
            }
        )
