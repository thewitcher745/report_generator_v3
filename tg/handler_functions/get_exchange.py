"""
This file contains the handler that gets the exchange from the user.
"""

from tg.handler_functions.helpers.conversation_stages import END


async def get_exchange(update, context):
    await update.callback_query.answer()

    context.user_data["exchange"] = update.callback_query.data

    return END
