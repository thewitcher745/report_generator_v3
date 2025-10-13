"""
This file contains the handler that gets the margin to calculate the $ profit.
"""

from tg.handler_functions.check_missing import check_missing


async def get_username(update, context):
    if update.callback_query:
        await update.callback_query.answer()

    context.user_data["username"] = update.message.text

    return await check_missing(update, context)
