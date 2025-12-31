"""
This file contains the handler that returns the current date.
"""

from tg.handler_functions.check_missing import check_missing


async def get_pnl_usd(update, context):
    if update.callback_query:
        await update.callback_query.answer()

    context.user_data["pnl_usd"] = float(update.message.text)

    return await check_missing(update, context)
