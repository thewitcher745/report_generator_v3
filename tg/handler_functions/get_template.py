"""
This file gets the template from the user through a callback query.
"""

from tg.handler_functions.helpers.conversation_stages import END
from tg.handler_functions.helpers.templates import get_template as get_template_details


async def get_template(update, context):
    await update.callback_query.answer()

    context.user_data["template"] = update.callback_query.data

    template_details = get_template_details(
        exchange=context.user_data["exchange"], template_name=update.callback_query.data
    )

    # Extend the context.user_data dict with the template_details dict
    context.user_data.update(template_details)

    return END
