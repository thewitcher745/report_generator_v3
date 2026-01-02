"""
This handler checks if any of the extra features are missing and redirects the inputs to it.
"""

import datetime
from tg.handler_functions.confirm import confirm
from tg.handler_functions.helpers.conversation_stages import (
    GET_MARGIN,
    GET_INPUT_DATE,
    GET_USERNAME,
    GET_PNL_USD,
    GET_PNL_PERCENT,
    GET_PERIOD_START,
    GET_PERIOD_END,
)
from tg.handler_functions.helpers.extra_features import (
    is_extra_feature_missing,
)
from tg.handler_functions.helpers.prompts import (
    prompt_get_input_date,
    prompt_get_input_date_example,
    prompt_get_margin,
    prompt_get_username,
    prompt_get_pnl_usd,
    prompt_get_pnl_percent,
    prompt_get_period_start,
    prompt_get_period_end,
)


async def check_missing(update, context):
    if is_extra_feature_missing(context, "margin"):
        await prompt_get_margin(update, context)
        return GET_MARGIN
    elif is_extra_feature_missing(context, "date"):
        context.user_data["date"] = datetime.datetime.now()
        return await check_missing(update, context)
    elif is_extra_feature_missing(context, "input_date"):
        await prompt_get_input_date(update, context)
        await prompt_get_input_date_example(update, context)
        return GET_INPUT_DATE
    elif is_extra_feature_missing(context, "pnl_usd"):
        await prompt_get_pnl_usd(update, context)
        return GET_PNL_USD
    elif is_extra_feature_missing(context, "pnl_percent"):
        await prompt_get_pnl_percent(update, context)
        return GET_PNL_PERCENT
    elif is_extra_feature_missing(context, "period_start"):
        await prompt_get_period_start(update, context)
        await prompt_get_input_date_example(update, context)
        return GET_PERIOD_START
    elif is_extra_feature_missing(context, "period_end"):
        await prompt_get_period_end(update, context)
        await prompt_get_input_date_example(update, context)
        return GET_PERIOD_END
    elif is_extra_feature_missing(context, "username"):
        await prompt_get_username(update, context)
        return GET_USERNAME

    # await prompt_confirm(update, context)
    return await confirm(update, context)
