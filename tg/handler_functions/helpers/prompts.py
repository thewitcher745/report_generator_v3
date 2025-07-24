"""
This file will contain the prompt functions used by the bot to ask for different information.
"""

from tg.handler_functions.helpers.utilities import send_message, send_media_group
from tg.handler_functions.helpers import strings
from tg.handler_functions.helpers import keyboards


async def prompt_get_exchange(update, context):
    await send_message(
        context, update, strings.GET_EXCHANGE, keyboard=keyboards.GET_EXCHANGE
    )


async def prompt_get_image(update, context):
    await send_media_group(
        context,
        update,
        "./background_images/" + context.user_data["exchange"] + "_images.png",
    )
    await send_message(
        context,
        update,
        strings.GET_IMAGE,
        keyboard=keyboards.GET_IMAGE(context.user_data["exchange"]),
    )


async def prompt_get_template(update, context):
    await send_message(
        context,
        update,
        strings.GET_TEMPLATE,
        keyboard=keyboards.GET_TEMPLATE(context.user_data["exchange"]),
    )
