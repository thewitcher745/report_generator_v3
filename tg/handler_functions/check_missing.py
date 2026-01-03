"""
Generic missing-feature checker.
Finds the first required extra feature that is missing and prompts via the generic system.
"""

import datetime
from tg.handler_functions.confirm import confirm
from tg.handler_functions.helpers.conversation_stages import GET_EXTRA_FEATURE
from tg.handler_functions.helpers.extra_features import get_extra_features
from tg.handler_functions.helpers.prompts import prompt_get_feature


async def check_missing(update, context):
    image_id = context.user_data.get("image_id")
    if not image_id:
        return await confirm(update, context)

    required = get_extra_features(image_id)

    # Auto-set current date if required
    if "date" in required and not context.user_data.get("date"):
        context.user_data["date"] = datetime.datetime.now()

    # Prompt for the first missing feature using the generic system
    for feature in required:
        if context.user_data.get(feature) in (None, ""):
            context.user_data["current_feature"] = feature
            await prompt_get_feature(update, context, feature)
            return GET_EXTRA_FEATURE

    return await confirm(update, context)
