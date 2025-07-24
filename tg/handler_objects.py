"""
This file contains handlers for the telegram bot, conversation handlers, welcome handlers, etc.
"""

from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler

from tg.handler_functions import (
    welcome,
    cancel,
    extract_signal_data,
    get_exchange,
    get_image,
    get_template,
    confirm
)
from tg.telegram_classes import ForwardedMessageHandler
from tg.handler_functions.helpers.conversation_stages import (
    GET_EXCHANGE,
    GET_IMAGE,
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
        CONFIRM: [CallbackQueryHandler(confirm)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
