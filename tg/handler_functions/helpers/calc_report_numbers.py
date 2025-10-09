import datetime

from tg.handler_functions.helpers.tz_data import get_tz_delta


def calc_report_numbers(user_data):
    """
    This function calculates the numbers necessary for the report.
    """
    image_id = user_data.get("image_id")
    symbol = user_data.get("symbol")
    username = user_data.get("username", "")
    qr = user_data.get("qr", "")
    referral = user_data.get("referral", "")
    date = user_data.get("date", datetime.datetime.now())

    signal_type = user_data.get("signal_type", "").lower()
    entry = user_data.get("entry")
    targets = user_data.get("targets")
    leverage = user_data.get("leverage")

    margin = user_data.get("margin", 1000)

    # The number of assets bought (or sold in  a short trade)
    qty = margin * leverage / entry
    report_data = []
    for target in targets:
        if signal_type == "long":
            # Money lost when buying the asset with "qty" units in dollars
            loss = qty * entry
            gain = qty * target
        else:
            # Money lost when selling the asset with "qty" units in dollars
            gain = qty * entry
            loss = qty * target

        report_data.append(
            {
                "image_id": image_id,
                "symbol": symbol,
                "username": username,
                "qr": qr,
                "referral": referral,
                "date": date,
                "signal_type": signal_type,
                "entry": entry,
                "target": target,
                "leverage": leverage,
                "roi_dollars": gain - loss,
                "roi_percent": (gain - loss) / margin * 100,
                "tz_delta": get_tz_delta(user_data["exchange"]),
            }
        )

    return report_data
