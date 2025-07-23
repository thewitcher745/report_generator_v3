"""
This file contains handlers for the telegram bot, conversation handlers, welcome handlers, etc.
"""

from telegram.ext import CommandHandler
from tg.handler_functions import generics

welcome_handler = CommandHandler("start", generics.welcome)
