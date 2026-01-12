from tg.handler_functions.helpers.conversation_stages import (
    GET_N_REPORTS,
    GET_CHANNEL,
    GET_EXCHANGE,
    END,
)
from tg.handler_functions.helpers.multiple_config import CHANNELS, MAX_N_REPORTS
from tg.handler_functions.helpers.prompts import prompt_get_exchange
from tg.handler_functions.helpers.utilities import send_message
from tg.handler_functions.helpers import strings, keyboards


async def start_multiple(update, context):
    signal_required_keys = [
        "symbol",
        "signal_type",
        "leverage",
        "entry",
        "targets",
        "stop",
    ]
    if not all(k in context.user_data for k in signal_required_keys):
        await send_message(context, update, strings.MULTIPLE_NEED_SIGNAL)
        return END

    context.user_data["multiple_mode"] = True
    context.user_data["multiple_queue"] = []
    context.user_data["multiple_current_index"] = 0
    context.user_data.pop("multiple_n_reports", None)

    for key in [
        "channel",
        "exchange",
        "image_id",
        "template",
        "precision",
        "qr",
        "referral",
        "username",
        "avatar",
        "date",
        "input_date",
        "period_start",
        "period_end",
        "pnl_usd",
        "pnl_percent",
        "input_symbol",
        "input_signal_type",
        "leverage_type",
        "input_leverage",
        "risk_percent",
        "input_entry_price",
        "input_target_price",
        "liq_price",
        "position_size",
        "margin",
        "current_feature",
    ]:
        context.user_data.pop(key, None)

    await send_message(context, update, strings.MULTIPLE_GET_N_REPORTS)
    return GET_N_REPORTS


async def get_n_reports(update, context):
    text = (update.message.text or "").strip()
    try:
        n_reports = int(text)
    except Exception:
        await send_message(context, update, strings.MULTIPLE_INVALID_N_REPORTS)
        return GET_N_REPORTS

    if n_reports <= 0 or n_reports > MAX_N_REPORTS:
        await send_message(context, update, strings.MULTIPLE_INVALID_N_REPORTS)
        return GET_N_REPORTS

    context.user_data["multiple_n_reports"] = n_reports
    context.user_data["multiple_current_index"] = 0

    await send_message(
        context,
        update,
        strings.MULTIPLE_GET_CHANNEL(1, n_reports),
        keyboard=keyboards.GET_CHANNELS(),
    )
    return GET_CHANNEL


async def get_channel(update, context):
    await update.callback_query.answer()
    channel = update.callback_query.data

    if channel not in CHANNELS:
        await send_message(context, update, strings.MULTIPLE_INVALID_CHANNEL)
        return GET_CHANNEL

    context.user_data["channel"] = channel

    await prompt_get_exchange(update, context)
    return GET_EXCHANGE
