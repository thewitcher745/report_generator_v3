"""
This file gets the template from the user through a callback query.
"""

from tg.handler_functions.helpers.conversation_stages import END


async def get_template(update, context):
    await update.callback_query.answer()

    context.user_data["template"] = update.callback_query.data

    return END
