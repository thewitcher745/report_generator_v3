"""
This file contains the strings returned by the bot to the user, collected in a single file for brevity.
"""

# Welcome message
import datetime


WELCOME = "🙏 Welcome. Forward a signal to continue."

# Cancel message
CANCEL = "❌ Operation canceled. Use /start to start over."

# Signal confirmation message
SIGNAL_CONFIRMATION_INTRO = "👇 This is the information extracted. If it's incorrect, use /cancel to end the process."


# Invalid signal message
INVALID_SIGNAL = "❌ Invalid signal. Please correct and forward the signal again."


def SIGNAL_CONFIRMATION(symbol, signal_type, leverage, entry, targets, stop):
    return f"{SIGNAL_CONFIRMATION_INTRO}\n\n💰 Symbol: {symbol}\n💰 Type: {signal_type}\n⬆️ Leverage: {leverage}\n⏎ Entry: {entry}\n☑️ Targets: {targets}\n☐ Stop: {stop}"


GET_EXCHANGE = "❓ Please select an exchange:"

GET_IMAGE = "❓ Please select an image for the selected exchange:"

GET_TEMPLATE = "❓ Please select a template for the selected exchange:"

GET_MARGIN = "❓ Please enter the margin, since this image requires it:"

GET_USERNAME = "❓ Please enter the username, since this image requires it:"

CONFIRM_INTRO = "💭 This is the provided signal and selected settings. If you need to customize the QR, referral or username, use the buttons below. Otherwise, press Confirm to generate the images."


def CONFIRM(
    exchange: str,
    image_id: str,
    template: str,
    referral: str = "",
    qr: str = "",
    margin: float = 0,
    username: str = "",
    date: datetime.datetime | None = None,
) -> str:
    message = f"{CONFIRM_INTRO}\n\n📊 Exchange: {exchange}\n🖼 Image: {image_id}\n📊 Template: {template}\n"
    # For signals that get/require the margin, the margin is also included.
    if margin:
        message += f"🖥 Margin: {margin}\n"
    if username:
        if len(username) > 0:
            message += f"👤 Username: {username}\n"
    if date:
        message += f"📅 Date: {date}\n"
    if qr:
        if len(qr) > 0:
            message += f"🖥 QR Code: {qr}\n"
    if referral:
        if len(referral) > 0:
            message += f"🤝 Referral Code: {referral}"
    return message
