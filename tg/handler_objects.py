"""
This file contains handlers for the telegram bot, conversation handlers, welcome handlers, etc.
"""

from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from tg.handler_functions import (
    get_extra_feature,
    welcome,
    cancel,
    extract_signal_data,
    get_exchange,
    get_image,
    get_template,
    start_multiple,
    get_n_reports,
    get_channel,
)
from tg.telegram_classes import ForwardedMessageHandler
from tg.handler_functions.helpers.conversation_stages import (
    GET_EXCHANGE,
    GET_IMAGE,
    GET_TEMPLATE,
    GET_EXTRA_FEATURE,
    GET_N_REPORTS,
    GET_CHANNEL,
)

welcome_handler = CommandHandler("start", welcome)

multiple_handler = CommandHandler("multiple", start_multiple)

automatic_signal_handler = ConversationHandler(
    entry_points=[ForwardedMessageHandler(extract_signal_data)],
    states={
        GET_N_REPORTS: [
            MessageHandler(
                filters=filters.TEXT & ~filters.COMMAND, callback=get_n_reports
            )
        ],
        GET_CHANNEL: [CallbackQueryHandler(get_channel)],
        GET_EXCHANGE: [CallbackQueryHandler(get_exchange)],
        GET_IMAGE: [CallbackQueryHandler(get_image)],
        GET_TEMPLATE: [CallbackQueryHandler(get_template)],
        GET_EXTRA_FEATURE: [
            MessageHandler(filters=filters.TEXT, callback=get_extra_feature)
        ],
        # CONFIRM: [CallbackQueryHandler(confirm)],
    },
    fallbacks=[
        CommandHandler("cancel", cancel),
        CommandHandler("multiple", start_multiple),
    ],
)
