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
    get_pnl_usd,
    get_pnl_percent,
    get_period_start,
    get_period_end,
    get_username,
    welcome,
    cancel,
    extract_signal_data,
    get_exchange,
    get_image,
    get_template,
)
from tg.telegram_classes import ForwardedMessageHandler
from tg.handler_functions.helpers.conversation_stages import (
    GET_INPUT_DATE,
    GET_EXCHANGE,
    GET_IMAGE,
    GET_MARGIN,
    GET_TEMPLATE,
    GET_PNL_USD,
    GET_PNL_PERCENT,
    GET_PERIOD_START,
    GET_PERIOD_END,
    GET_USERNAME,
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
        GET_PNL_USD: [MessageHandler(filters=filters.TEXT, callback=get_pnl_usd)],
        GET_PNL_PERCENT: [
            MessageHandler(filters=filters.TEXT, callback=get_pnl_percent)
        ],
        GET_PERIOD_START: [
            MessageHandler(filters=filters.TEXT, callback=get_period_start)
        ],
        GET_PERIOD_END: [MessageHandler(filters=filters.TEXT, callback=get_period_end)],
        GET_USERNAME: [MessageHandler(filters=filters.TEXT, callback=get_username)],
        # CONFIRM: [CallbackQueryHandler(confirm)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
