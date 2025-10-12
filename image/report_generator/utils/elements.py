"""
This module contains functions for creating backgrounds and drawing elements on an image using HTML and CSS.
"""

from image.report_generator.utils.style_strings import StyleStrings


class ReportHTML:
    def __init__(
        self,
        output_path: str = "image/report_generator/html/report.html",
    ) -> None:
        self.output_path: str = output_path

        # *fonts* is a placeholder that gets replaced by the actual fonts of the image later.
        self.head = """<html>
    <head>
        <style>
            @font-face {}
            body {
                background-color: transparent;
                margin: 0;
                padding: 0;
            }
        </style>
    </head>
    <body>
    """
        self.body: str = ""
        self.tail: str = "</body>\n</html>"

    def add_font(self, font_filename: str) -> None:
        """Returns the body of an HTML file with the given font as a background."""
        self.head = self.head.replace(
            "@font-face {}",
            f"""@font-face {{
                font-family: '{font_filename}';
                src: url('../../../fonts/{font_filename}') format('truetype');
                font-weight: normal;
                font-style: normal;
                font-display: swap;
            }}
            @font-face {{}}""",
        )

    def add_background(self, img_src: str) -> None:
        """Returns the body of an HTML file with the given background image.
        Args:
            img_src (str): The path to the image file.
        """
        self.body += f"<img id='bg' src='{img_src}' {StyleStrings.background_img()}>\n"
        self._set_image_size(img_src)

    def add_text(
        self,
        text: str,
        position: tuple[int, int],
        font_name: str,
        font_size: int,
        font_color: str,
        justify_content: str = "left",
    ) -> None:
        """Returns the body of an HTML file with the given text element."""

        style_string = StyleStrings.text(
            position=position,
            font_name=font_name,
            font_size=font_size,
            font_color=font_color,
            justify_content=justify_content,
        )
        self.body += f"<p {style_string}>{text}</p>\n"

    def save_html(self) -> None:
        """Saves the HTML file to the specified path."""

        with open(self.output_path, "w") as f:
            f.write(self.head + self.body + self.tail)
