"""
This module contains functions for creating backgrounds and drawing elements on an image using HTML and CSS.
"""

from PIL import Image
from image.report_generator.utils.generic import Position
from image.report_generator.utils.style_strings import StyleStrings


class ReportHTML:
    def __init__(
        self,
        output_path: str = "image/report_generator/html/report.html",
        drag_and_drop: bool = False,
    ) -> None:
        self.output_path: str = output_path

        self.width: int | None = None
        self.height: int | None = None

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
        <div id='report'>
    """
        self.body: str = ""
        if drag_and_drop:
            self.tail = "<script src='./dragging.js'></script>\n</div></body>\n</html>"
        else:
            self.tail = "</div></body>\n</html>"

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

    def _set_image_size(self, img_src: str) -> None:
        """Sets the width and height of the image."""
        img_filename = img_src.split("/")[-1]
        size = Image.open(f"./background_images/{img_filename}").size
        self.width = size[0]
        self.height = size[1]
        self.head = self.head.replace(
            "id='report'",
            f"id='report' style='width: {self.width}px; height: {self.height}px; padding: 0; margin: 0; position: relative;'",
        )

    def _convert_element_position(self, position: Position | None) -> Position:
        """Converts the position of an element to pixels from fractions (0-1)."""
        if not position:
            raise ValueError("Element position is None.")
        return Position(
            x=position.x * self.width,
            y=position.y * self.height,
        )

    def add_background(self, img_src: str) -> None:
        """Returns the body of an HTML file with the given background image.
        Args:
            img_src (str): The path to the image file.
        """
        self.body += f"<img id='bg' src='{img_src}' {StyleStrings.background_img()}>\n"
        self._set_image_size(img_src)

    def create_text(
        self,
        text: str,
        position: Position | None,
        font_name: str,
        font_size: int,
        font_color: str,
        additional_styles: dict = {},
        justify_content: str = "left",
    ) -> str:
        """Returns a <p> element with the given text element."""

        style_string = StyleStrings.text(
            additional_styles=additional_styles,
            position=self._convert_element_position(position),
            font_name=font_name,
            font_size=font_size,
            font_color=font_color,
            justify_content=justify_content,
        )
        return f"\t<p {style_string}>{text}</p>\n"

    def add_text(
        self,
        text: str,
        position: Position | None,
        font_name: str,
        font_size: int,
        font_color: str,
        additional_styles: dict = {},
        justify_content: str = "left",
    ) -> None:
        """Adds a <p> element with the given text element."""

        self.body += self.create_text(
            text=text,
            position=position,
            font_name=font_name,
            font_size=font_size,
            font_color=font_color,
            additional_styles=additional_styles,
            justify_content=justify_content,
        )

    def create_inline_text(
        self,
        text: str,
        font_name: str,
        font_size: int,
        font_color: str,
        additional_styles: dict = {},
        justify_content: str = "left",
    ) -> str:
        """Returns a <p> element with the given text element, for use inside the inline div element."""

        style_string = StyleStrings.inline_text(
            additional_styles=additional_styles,
            font_name=font_name,
            font_size=font_size,
            font_color=font_color,
            justify_content=justify_content,
        )
        return f"\t<p {style_string}>{text}</p>\n"

    def create_inline_element(
        self,
        elements: list[str],
        position: Position | None,
        additional_styles: dict = {},
        justify_content: str = "left",
    ) -> str:
        """Returns a <div> flex element with the given text containing multiple elements in a line."""

        style_string = StyleStrings.inline_elements(
            additional_styles=additional_styles,
            position=self._convert_element_position(position),
            justify_content=justify_content,
        )
        result = f"\t<div {style_string}>"
        for element in elements:
            result += "\t" + element + "\n"
        result += "\t</div>\n"
        return result

    def create_separator(
        self,
        color: str,
        width: int,
        length: int,
        additional_styles: dict = {},
    ) -> str:
        """Returns a <div> element with a separator."""

        style_string = StyleStrings.separator(
            additional_styles=additional_styles,
            color=color,
            width=width,
            length=length,
        )
        return f"\t<div {style_string}></div>\n"

    def add_inline_elements(
        self,
        elements: list[str],
        position: Position | None,
        additional_styles: dict = {},
        justify_content: str = "left",
    ) -> None:
        """Adds a <div> with elements put into a single line with a defined gap."""

        self.body += self.create_inline_element(
            elements=elements,
            position=position,
            additional_styles=additional_styles,
            justify_content=justify_content,
        )

    def add_img(
        self,
        img_src: str,
        position: Position | None,
        width: int,
        height: int,
        additional_styles: dict = {},
    ) -> None:
        """Adds an <img> element with the given image source."""
        img_styling = StyleStrings.img(
            position=self._convert_element_position(position),
            width=width,
            height=height,
            additional_styles=additional_styles,
        )
        self.body += f"\t<img src='{img_src}' {img_styling}/>\n"

    def save_html(self) -> str:
        """Saves the HTML file to the specified path."""

        with open(self.output_path, "w") as f:
            f.write(self.head + self.body + self.tail)

        return self.output_path
