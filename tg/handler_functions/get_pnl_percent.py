"""
This file contains the handler that gets the PnL percent.
"""

from tg.handler_functions.check_missing import check_missing


async def get_pnl_percent(update, context):
    if update.callback_query:
        await update.callback_query.answer()

    context.user_data["pnl_percent"] = float(update.message.text)

    return await check_missing(update, context)
