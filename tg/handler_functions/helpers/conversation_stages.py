"""
Contains the conversation stages used by the bot.
"""

from telegram.ext import ConversationHandler

PROCESS_SIGNAL_DATA, GET_EXCHANGE, GET_IMAGE, GET_TEMPLATE, CONFIRM, CUSTOMIZE_QR_CODE, CUSTOMIZE_REFERRAL_CODE, CUSTOMIZE_USERNAME = range(8)

END = ConversationHandler.END
