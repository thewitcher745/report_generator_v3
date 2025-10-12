"""
This handler checks if any of the extra features are missing and redirects the inputs to it.
"""

import datetime
from tg.handler_functions.helpers.conversation_stages import (
    GET_MARGIN,
    GET_INPUT_DATE,
    GET_USERNAME,
    CONFIRM,
)
from tg.handler_functions.helpers.extra_features import (
    is_extra_feature_missing,
)
from tg.handler_functions.helpers.prompts import (
    prompt_confirm,
    prompt_get_input_date,
    prompt_get_input_date_example,
    prompt_get_margin,
    prompt_get_username,
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
    elif is_extra_feature_missing(context, "username"):
        await prompt_get_username(update, context)
        return GET_USERNAME

    await prompt_confirm(update, context)
    return CONFIRM
