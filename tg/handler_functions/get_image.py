"""
This file contains the handler that gets the image for the selected exchange from the user.
"""

from tg.handler_functions.helpers.conversation_stages import END


async def get_image(update, context):
    await update.callback_query.answer()

    context.user_data["image_id"] = update.callback_query.data

    return END
