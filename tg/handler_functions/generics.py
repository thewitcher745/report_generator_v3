"""
This file contains generic handler functions used by the bot.
"""

from tg.handler_functions.helpers import strings
from tg.handler_functions.helpers.utilities import send_message


async def welcome(update, context):
    await send_message(context, update, strings.WELCOME)


async def cancel(update, context):
    await send_message(context, update, strings.CANCEL)
