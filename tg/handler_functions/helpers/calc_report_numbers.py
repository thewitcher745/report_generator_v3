from tg.handler_functions.helpers.tz_data import get_tz_delta
from tg.handler_functions.helpers.extra_features import get_extra_features


def _compute_bingx_misc_position(user_data):
    margin = float(user_data.get("margin", 0) or 0)
    leverage = float(user_data.get("input_leverage", 0) or 0)
    entry_price = float(user_data.get("input_entry_price", 0) or 0)
    target_price = float(user_data.get("input_target_price", 0) or 0)
    signal_type = (user_data.get("input_signal_type") or "").lower()

    position_amount = leverage * margin
    qty = (leverage * margin / entry_price) if entry_price else 0

    if signal_type == "short":
        unrealized_pnl = position_amount - qty * target_price
    else:  # default to long
        unrealized_pnl = qty * target_price - position_amount

    pnl_percent = (unrealized_pnl / margin * 100) if margin else 0

    report_data_item = {
        "image_id": user_data.get("image_id"),
        # Symbol and common decorations
        "symbol": user_data.get("input_symbol", user_data.get("symbol")),
        "username": user_data.get("username"),
        "avatar": user_data.get("avatar"),
        "qr": user_data.get("qr"),
        "referral": user_data.get("referral"),
        # Position specifics
        "signal_type": signal_type,
        "leverage_type": user_data.get("leverage_type"),
        "leverage": leverage,
        "margin": margin,
        # Prices
        "entry": entry_price,
        "target": target_price,
        # Derived metrics
        "position_amount": position_amount,
        "pnl_usd": round(unrealized_pnl, 4),
        "pnl_percent": round(pnl_percent, 2),
        # Risk percent for rendering
        "risk_percent": user_data.get("risk_percent"),
    }

    return [report_data_item]


def _compute_standard(user_data):
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


def calc_report_numbers(user_data):
    """
    Calculates the numbers necessary for the report.
    Delegates to a specialized flow when needed.
    """
    image_id = user_data.get("image_id")
    if image_id == "bingx_misc_position_1":
        return _compute_bingx_misc_position(user_data)
    return _compute_standard(user_data)
