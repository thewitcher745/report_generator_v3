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
    get_margin,
    get_input_date,
    welcome,
    cancel,
    extract_signal_data,
    get_exchange,
    get_image,
    get_template,
    confirm,
)
from tg.telegram_classes import ForwardedMessageHandler
from tg.handler_functions.helpers.conversation_stages import (
    GET_INPUT_DATE,
    GET_EXCHANGE,
    GET_IMAGE,
    GET_MARGIN,
    GET_TEMPLATE,
    CONFIRM,
)

welcome_handler = CommandHandler("start", welcome)

automatic_signal_handler = ConversationHandler(
    entry_points=[ForwardedMessageHandler(extract_signal_data)],
    states={
        GET_EXCHANGE: [CallbackQueryHandler(get_exchange)],
        GET_IMAGE: [CallbackQueryHandler(get_image)],
        GET_TEMPLATE: [CallbackQueryHandler(get_template)],
        GET_MARGIN: [MessageHandler(filters=filters.TEXT, callback=get_margin)],
        GET_INPUT_DATE: [MessageHandler(filters=filters.TEXT, callback=get_input_date)],
        CONFIRM: [CallbackQueryHandler(confirm)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
