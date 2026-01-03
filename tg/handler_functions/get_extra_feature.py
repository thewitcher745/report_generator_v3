"""
Generic handler for all custom extra features.
Relies on extra_feature_config for prompts/keyboards/sanitizers.
"""

from tg.handler_functions.check_missing import check_missing
from tg.handler_functions.helpers.extra_feature_config import sanitize_feature_value


async def get_extra_feature(update, context):
    if update.callback_query:
        await update.callback_query.answer()

    feature = context.user_data.get("current_feature")
    if not feature:
        # Nothing to do; continue flow
        return await check_missing(update, context)

    value_text = update.message.text
    try:
        sanitized = sanitize_feature_value(feature, value_text)
    except Exception:
        # If sanitize fails, keep raw text
        sanitized = value_text

    context.user_data[feature] = sanitized
    context.user_data.pop("current_feature", None)

    return await check_missing(update, context)
