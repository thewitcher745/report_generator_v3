from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

    try:
        driver.get(f"https://www.okx.com/trade-spot/{symbol}-usdt")

        logo_url = driver.find_element("css selector", ".ticker-logo").get_attribute(
            "src"
        )
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
