"""
Contains the conversation stages used by the bot.
"""

from telegram.ext import ConversationHandler

PROCESS_SIGNAL_DATA, GET_EXCHANGE, GET_IMAGE, GET_TEMPLATE = range(4)

END = ConversationHandler.END
