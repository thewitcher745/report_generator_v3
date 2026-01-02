"""
This file contains the handler that gets the period start.
"""

from tg.handler_functions.check_missing import check_missing


async def get_period_start(update, context):
    if update.callback_query:
        await update.callback_query.answer()

    context.user_data["period_start"] = update.message.text

    return await check_missing(update, context)
