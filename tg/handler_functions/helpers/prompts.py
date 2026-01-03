"""
This file will contain the prompt functions used by the bot to ask for different information.
"""

from image.image_list_composer import create_image_list_collage
from tg.handler_functions.helpers.utilities import send_message, send_media_group
from tg.handler_functions.helpers import strings
from tg.handler_functions.helpers import keyboards
from tg.handler_functions.helpers.extra_feature_config import (
    get_feature_prompt,
    get_feature_keyboard,
    get_feature_example,
)


async def prompt_get_exchange(update, context):
    await send_message(
        context, update, strings.GET_EXCHANGE, keyboard=keyboards.GET_EXCHANGE
    )


async def prompt_get_feature(update, context, feature: str):
    prompt_text = get_feature_prompt(feature)
    keyboard = get_feature_keyboard(update, context, feature)
    await send_message(context, update, prompt_text, keyboard=keyboard)
    example = get_feature_example(feature)
    if example:
        await send_message(context, update, example, keyboard=keyboard)


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


async def prompt_precision_not_found(update, context):
    await send_message(
        context,
        update,
        strings.PRECISION_NOT_FOUND,
    )


async def prompt_confirm(update, context):
    prompt_text = strings.CONFIRM(context.user_data)

    await send_message(
        context,
        update,
        prompt_text,
        keyboard=keyboards.CONFIRM,
    )
