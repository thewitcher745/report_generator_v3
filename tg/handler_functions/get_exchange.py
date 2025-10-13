"""
This file contains the handler that gets the exchange from the user.
"""

from tg.handler_functions.helpers.conversation_stages import GET_IMAGE
from tg.handler_functions.helpers.prompts import (
    prompt_get_image,
    prompt_precision_not_found,
)
from tg.handler_functions.helpers.utilities import get_pair_precision


async def get_exchange(update, context):
    # Gets the exchange and also sets the precision for the report's prices

    if update.callback_query:
        await update.callback_query.answer()

    context.user_data["exchange"] = update.callback_query.data

    # See if the precision is available for the coin. If so, round the entry and targets to that precision.
    coin_precision = get_pair_precision(
        context.user_data["symbol"], context.user_data["exchange"]
    )
    context.user_data["precision"] = coin_precision
    if coin_precision is None:
        await prompt_precision_not_found(update, context)
        context.user_data["precision"] = None
    else:
        context.user_data["entry"] = round(context.user_data["entry"], coin_precision)
        context.user_data["targets"] = [
            round(target, coin_precision) for target in context.user_data["targets"]
        ]

    await prompt_get_image(update, context)

    return GET_IMAGE
