"""
Contains the conversation stages used by the bot.
"""

from telegram.ext import ConversationHandler

(
    PROCESS_SIGNAL_DATA,
    GET_EXCHANGE,
    GET_IMAGE,
    GET_TEMPLATE,
    GET_MARGIN,
    GET_INPUT_DATE,
    GET_USERNAME,
    CONFIRM,
    CUSTOMIZE_QR,
    CUSTOMIZE_REFERRAL,
    CUSTOMIZE_USERNAME,
) = range(11)

END = ConversationHandler.END
