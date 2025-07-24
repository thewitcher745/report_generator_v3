"""
This is the conversation handler staget  confirm the user inputs and ask if the user needs to customize them.
"""

from tg.handler_functions.helpers.conversation_stages import (
    END,
    CUSTOMIZE_QR_CODE,
    CUSTOMIZE_REFERRAL_CODE,
    CUSTOMIZE_USERNAME,
)


async def confirm(update, context):
    await update.callback_query.answer()

    confirmation_dialog_answer = update.callback_query.data

    if confirmation_dialog_answer == "confirm":
        print("Data acquired successfully!")
    elif confirmation_dialog_answer == "customize_qr_code":
        print("Customize QR Code")
    elif confirmation_dialog_answer == "customize_referral_code":
        print("Customize Referral Code")
    elif confirmation_dialog_answer == "customize_username":
        print("Customize Username")

    return END
