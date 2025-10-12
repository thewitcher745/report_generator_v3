"""
This file contains the handler that returns the current date.
"""

from tg.handler_functions.check_missing import check_missing


async def get_input_date(update, context):
    context.user_data["input_date"] = update.message.text

    return await check_missing(update, context)
