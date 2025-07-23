"""
This file contains generic handler functions used by the bot.
"""

from tg import strings
from tg.utilities import send_message


async def welcome(update, context):
    await send_message(context, update, strings.WELCOME)
