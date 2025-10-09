"""
This file contains the handler that gets the margin to calculate the $ profit.
"""

from tg.handler_functions.check_missing import check_missing


async def get_margin(update, context):
    context.user_data["margin"] = float(update.message.text)

    return await check_missing(update, context)
