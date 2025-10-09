"""
This is the conversation handler staget  confirm the user inputs and ask if the user needs to customize them.
"""

from tg.handler_functions.helpers.conversation_stages import (
    END,
    CUSTOMIZE_QR,
    CUSTOMIZE_REFERRAL,
    CUSTOMIZE_USERNAME,
)
from image.report_generator.report_classes.BaseReport import BaseReport


async def confirm(update, context):
    if update.callback_query:
        await update.callback_query.answer()

    confirmation_dialog_answer = update.callback_query.data

    if confirmation_dialog_answer == "confirm":
        print("Data acquired successfully!")
    elif confirmation_dialog_answer == "customize_qr":
        print("Customize QR")
    elif confirmation_dialog_answer == "customize_referral":
        print("Customize Referral")
    elif confirmation_dialog_answer == "customize_username":
        print("Customize Username")

    report = BaseReport(context.user_data)
    report.print_info()

    return END
