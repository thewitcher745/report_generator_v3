"""
The image composer uses CSS and HTML to put compile the list of images into a collage as an HTML file.
"""

import os

from image.image_list_composer.utilities import get_image_list_label_by_id


def compose_html_collage(
    image_list: list[str], output_path: str = None, max_images_per_row: int = 2
) -> str:
    """
    Generates an HTML file displaying a collage of unique images for the given exchange.
    Images are arranged using CSS grid. The image sources are assumed to be in the
    'background_images' directory and named as '{image_id}.png'.

    Args:
        image_list (list[str]): The list of image IDs to use for the collage.
        output_path (str, optional): Where to save the HTML file. Defaults to 'collage_{exchange}.html' in the current directory.

    Returns:
        str: The path to the generated HTML file.
    """
    images_html = []
    number_of_rows = int(len(image_list) / max_images_per_row) + 1
    for i in range(number_of_rows):
        row_images_html = []

        for j in range(max_images_per_row):
            # Find the image id at the current position
            try:
                img_id = image_list[i * max_images_per_row + j]
            # In the last row, continue until the loop finishes
            except IndexError:
                continue

            # Compute the absolute path and convert to file URL with forward slashes
            abs_img_path = os.path.abspath(
                os.path.join(
                    os.path.dirname(
                        output_path or "image/image_list_composer/collage.html"
                    ),
                    "../../background_images",
                    f"{img_id}.png",
                )
            )
            img_src = f"file:///{abs_img_path.replace(os.sep, '/')}"

            row_images_html.append(
                f"""
                <div class="collage-img-container">
                    <img src="{img_src}" class="collage-img" alt="{img_id}">
                    <span>{get_image_list_label_by_id(img_id)}</span>
                </div>
                """
            )

        images_html.append(
            f"<div class='collage-row'>{'\n'.join(row_images_html)}</div>"
        )

    collage_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Image Collage</title>
            <style>
                .collage-row {{
                    display: flex;
                }}
                .collage {{
                    display: inline-block;
                }}
                .collage-img-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    position: relative;
                }}
                .collage-img {{
                    height: 140px;
                    object-fit: cover;
                    background: #f3f3f3;
                }}
                .collage-img-container span {{
                    position: absolute;
                    top: calc(50% - 18px);
                    left: calc(50% - 9px);
                    z-index: 100;
                    width: 100%;
                    height: 100%;
                    color: orange;
                    font-size: 36px;
                }}
                body {{
                    padding: 0;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }}
            </style>
        </head>
        <body>
            <div class="collage">
                {"".join(images_html)}
            </div>
        </body>
        </html>
"""

    if output_path is None:
        output_path = "image/image_list_composer/collage.html"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(collage_html)

    return os.path.abspath(output_path)
