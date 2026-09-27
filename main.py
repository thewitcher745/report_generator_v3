from dotenv import dotenv_values

from telegram import Update
from telegram.ext import Application
from tg.handler_objects import (
    welcome_handler,
    automatic_signal_handler,
)

if __name__ == "__main__":
    token = dotenv_values(".env.secret").get("BOT_TOKEN")
    proxy_server = dotenv_values(".env.local").get("PROXY_SERVER")

    if not token:
        raise ValueError("BOT_TOKEN is missing from .env.secret")

    application_builder = Application.builder().token(token)
    if proxy_server:
        application_builder.proxy(proxy_server).get_updates_proxy(proxy_server)

    application = application_builder.build()

    application.add_handlers([welcome_handler, automatic_signal_handler])

    print("RG bot started.")

    application.run_polling(allowed_updates=Update.ALL_TYPES)
