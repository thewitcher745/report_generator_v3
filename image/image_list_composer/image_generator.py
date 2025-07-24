"""
This module converts the generated HTML file containing the collage to an image.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import hashlib
import os

from image.image_list_composer.utilities import get_unique_images_by_exchange
from image.image_list_composer.html_composer import compose_html_collage


def html_to_image(html_path, output_path="image_outputs/image_lists/image_list.png"):
    """
    Uses Selenium and headless Chrome to render an HTML file and take a screenshot.

    Args:
        html_path (str): Path to the HTML file.
        output_path (str): Path to save the screenshot image.

    Returns:
        str: Path to the generated image.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--allow-file-access-from-files")
    chrome_options.add_argument("--enable-local-file-accesses")

    driver = webdriver.Chrome(options=chrome_options)

    # Convert the HTML path to an absolute path and convert backslashes to forward slashes
    abs_html_path = os.path.abspath(html_path)
    file_url = f"file:///{abs_html_path.replace(os.sep, '/')}"

    driver.get(file_url)

    # Locate the collage div
    collage_div = driver.find_element("css selector", ".collage")
    # Screenshot only the collage div
    collage_div.screenshot(output_path)

    driver.quit()

    return os.path.abspath(output_path)


def create_image_list_collage(exchange: str):
    """
    Creates an image list for the given exchange. If the same image list has already been done, it returns the cached image.

    Args:
        exchange (str): The exchange to create the image list for.
    """

    # Cache the current list of images using SHA256
    list_of_images = get_unique_images_by_exchange(exchange)

    # Sort the list of images to ensure that the same list of images always has the same hash
    cache_key = hashlib.sha256(",".join(sorted(list_of_images)).encode()).hexdigest()
    next_cache_filename = f"{exchange}_{cache_key}.png"

    # Check if the PNG file in the image_lists directory that begins with the name of the exchange has the same name/hash
    for filename in os.listdir("image_outputs/image_lists"):
        if filename.startswith(exchange) and filename.endswith(".png"):
            # If such a file exists, then it has already been cached and we can return the cached image.
            if filename == next_cache_filename:
                return os.path.abspath(
                    os.path.join("image_outputs/image_lists", filename)
                )
            else:
                # If such a file exists, but it has a different hash, then we delete it and continue.
                os.remove(os.path.join("image_outputs/image_lists", filename))

    output_path = os.path.join("image_outputs/image_lists", next_cache_filename)

    html_path = compose_html_collage(
        list_of_images,
        max_images_per_row=2,
        output_path=output_path.replace(".png", ".html"),
    )

    image_path = html_to_image(html_path, output_path=output_path)

    return os.path.abspath(image_path)
