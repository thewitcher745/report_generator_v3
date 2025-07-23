"""
Contains the conversation stages used by the bot.
"""

from telegram.ext import ConversationHandler

PROCESS_SIGNAL_DATA, GET_EXCHANGE, GET_IMAGE = range(3)

END = ConversationHandler.END
