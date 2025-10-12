"""
This file will contain the prompt functions used by the bot to ask for different information.
"""

from image.image_list_composer import create_image_list_collage
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
        create_image_list_collage(context.user_data["exchange"]),
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


async def prompt_get_margin(update, context):
    await send_message(
        context,
        update,
        strings.GET_MARGIN,
        keyboard=keyboards.GET_MARGIN(),
    )


async def prompt_get_input_date(update, context):
    await send_message(
        context,
        update,
        strings.GET_INPUT_DATE,
        keyboard=keyboards.GET_DATE(),
    )


async def prompt_get_input_date_example(update, context):
    await send_message(
        context,
        update,
        strings.GET_INPUT_DATE_EXAMPLE,
        keyboard=keyboards.GET_DATE(),
    )


async def prompt_get_username(update, context):
    await send_message(
        context,
        update,
        strings.GET_USERNAME,
        keyboard=keyboards.GET_USERNAME(),
    )


async def prompt_confirm(update, context):
    prompt_text = strings.CONFIRM(context.user_data)

    await send_message(
        context,
        update,
        prompt_text,
        keyboard=keyboards.CONFIRM,
    )
