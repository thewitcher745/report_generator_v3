"""
This file contains handlers for the telegram bot, conversation handlers, welcome handlers, etc.
"""

from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler

from tg.handler_functions import welcome, cancel, extract_signal_data, get_exchange
from tg.telegram_classes import ForwardedMessageHandler
from tg.handler_functions.helpers.conversation_stages import GET_EXCHANGE

welcome_handler = CommandHandler("start", welcome)

automatic_signal_handler = ConversationHandler(
    entry_points=[ForwardedMessageHandler(extract_signal_data)],
    states={
        GET_EXCHANGE: [CallbackQueryHandler(get_exchange)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
