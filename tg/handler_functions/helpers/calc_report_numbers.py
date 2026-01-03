from tg.handler_functions.helpers.tz_data import get_tz_delta
from tg.handler_functions.helpers.extra_features import get_extra_features


def calc_report_numbers(user_data):
    """
    This function calculates the numbers necessary for the report.
    """
    signal_type = (
        user_data.get("signal_type").lower() if user_data.get("signal_type") else None
    )
    entry = user_data.get("entry", None)
    targets = user_data.get("targets", [])
    leverage = user_data.get("leverage", None)

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

        report_data_item = {}
        key_list = [
            "image_id",
            "symbol",
            "username",
            "avatar",
            "qr",
            "referral",
            "date",
            "input_date",
            "period_start",
            "period_end",
            "pnl_usd",
            "pnl_percent",
            "signal_type",
            "entry",
            "target",
            "leverage",
            "roi_dollars",
            "roi_percent",
            "tz_delta",
            "precision",
        ]

        # Also include any extra features required by this image so they are available during processing
        image_id_for_keys = user_data.get("image_id")
        if image_id_for_keys:
            extras = [
                f for f in get_extra_features(image_id_for_keys) if f not in key_list
            ]
            key_list.extend(extras)

        for key in key_list:
            if key == "roi_dollars":
                if "margin" in user_data.keys():
                    report_data_item[key] = round(gain - loss, 2)
            elif key == "tz_delta":
                report_data_item[key] = get_tz_delta(user_data.get("exchange"))
            elif key == "roi_percent":
                report_data_item[key] = round((gain - loss) / margin * 100, 2)
            elif key == "target":
                report_data_item[key] = target

            else:
                if key in user_data:
                    report_data_item[key] = user_data.get(key)

        report_data.append(report_data_item)

    return report_data
