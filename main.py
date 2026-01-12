from dotenv import dotenv_values

from telegram import Update
from telegram.ext import Application
from tg.handler_objects import (
    welcome_handler,
    automatic_signal_handler,
    multiple_handler,
)

if __name__ == "__main__":
    token = dotenv_values(".env.secret").get("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN is missing from .env.secret")
    application = Application.builder().token(token).build()

    application.add_handlers([welcome_handler, automatic_signal_handler])
    application.add_handler(multiple_handler)

    print("RG bot started.")

    application.run_polling(allowed_updates=Update.ALL_TYPES)
