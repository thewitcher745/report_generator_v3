"""
This file contains generic handler functions used by the bot.
"""

from tg.handler_functions.helpers import strings
from tg.handler_functions.helpers.utilities import send_message

from tg.handler_functions.helpers.conversation_stages import END


async def welcome(update, context):
    await send_message(context, update, strings.WELCOME)


async def cancel(update, context):
    await send_message(context, update, strings.CANCEL)
    return END
