"""
This file will contain the prompt functions used by the bot to ask for different information.
"""

from tg.handler_functions.helpers.utilities import send_message
from tg.handler_functions.helpers import strings
from tg.handler_functions.helpers import keyboards


async def prompt_get_exchange(update, context):
    await send_message(
        context, update, strings.GET_EXCHANGE, keyboard=keyboards.GET_EXCHANGE
    )

async def prompt_get_image(update, context):
    await send_message(
        context, update, strings.GET_IMAGE, keyboard=keyboards.GET_IMAGE
    )