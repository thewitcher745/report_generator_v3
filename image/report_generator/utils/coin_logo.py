import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json


def get_coin_logo(symbol: str) -> str | None:
    symbol = symbol.upper().removesuffix(" PERPETUAL").removesuffix("USDT")
    cache_path = Path(__file__).with_name("coin_logos.json")

    if not symbol:
        return None

    with cache_path.open(encoding="utf-8") as fs:
        logo_links: dict[str, str] = json.load(fs)
    if logo_links.get(symbol):
        return logo_links[symbol]

    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=2000,2000")
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception:
        return None

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
    except Exception:
        return None
    finally:
        driver.quit()

    # Cache the logo once received in the json file
    if logo_url:
        logo_links[symbol] = logo_url

        with cache_path.open("w", encoding="utf-8") as fs:
            json.dump(logo_links, fs)

    return logo_url
