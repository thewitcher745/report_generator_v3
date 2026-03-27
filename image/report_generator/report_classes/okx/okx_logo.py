import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json


def get_okx_logo(symbol: str) -> str | None:
    symbol = symbol.replace(" Perpetual", "").replace("USDT", "").lower()

    with open("image/report_generator/report_classes/okx/okx_logos.json", "r") as fs:
        okx_logo_links: dict[str, str] = json.load(fs)
        if symbol in okx_logo_links:
            if okx_logo_links[symbol]:
                return okx_logo_links[symbol]

    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=2000,2000")
    driver = webdriver.Chrome(options=chrome_options)

    # Number of waits for the page to load before admitting the logo isn't there
    tries = 0

    logo_url = None
    is_logo_element_img = False
    try:
        driver.get(f"https://www.okx.com/trade-spot/{symbol}-usdt")

        while logo_url is None and tries < 5 and not is_logo_element_img:
            logo_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ticker-logo"))
            )
            is_logo_element_img = logo_element.tag_name == "img"

            logo_url = logo_element.get_attribute("src")
            tries += 1
            time.sleep(1)
    except:
        return None

    # Cache the logo once received in the json file
    if logo_url:
        okx_logo_links[symbol] = logo_url

        with open(
            "image/report_generator/report_classes/okx/okx_logos.json", "w"
        ) as fs:
            json.dump(okx_logo_links, fs)

    driver.quit()
    return logo_url
