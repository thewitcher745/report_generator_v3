"""
This file contains custom classes inheriting python-telegram-bot classes with additional functionality.
"""

from telegram.ext import MessageHandler, filters


# Custom message handlers for text and forwarded messages.
class TextMessageHandler(MessageHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(filters.TEXT & ~filters.COMMAND, *args, **kwargs)


class ForwardedMessageHandler(MessageHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(filters.FORWARDED & ~filters.COMMAND, *args, **kwargs)
