"""
This file contains the handler that gets the exchange from the user.
"""

from tg.handler_functions.helpers.conversation_stages import GET_IMAGE
from tg.handler_functions.helpers.prompts import prompt_get_image


async def get_exchange(update, context):
    await update.callback_query.answer()

    context.user_data["exchange"] = update.callback_query.data

    await prompt_get_image(update, context)

    return GET_IMAGE
