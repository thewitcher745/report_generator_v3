from dotenv import dotenv_values

from telegram import Update
from telegram.ext import Application
from tg.handler_objects import welcome_handler, automatic_signal_handler

if __name__ == "__main__":
    application = (
        Application.builder().token(dotenv_values(".env.secret")["BOT_TOKEN"]).build()
    )

    application.add_handlers([welcome_handler, automatic_signal_handler])

    print("RG bot started.")

    application.run_polling(allowed_updates=Update.ALL_TYPES)
