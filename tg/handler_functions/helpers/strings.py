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

GET_INPUT_DATE = "❓ Please enter a date and time, since this image requires it. Format: YYYY-MM-DD HH:MM:SS"

GET_INPUT_DATE_EXAMPLE = "2025-10-08 13:47:22"

GET_USERNAME = "❓ Please enter the username, since this image requires it:"

PRECISION_NOT_FOUND = "⚠️ Warning: Precision not found for the selected coin. Using the precision given by the signal text."

CONFIRM_INTRO = "💭 This is the provided signal and selected settings. If you need to customize the QR, referral or username, use the buttons below. Otherwise, press Confirm to generate the images."


def CONFIRM(user_data: dict) -> str:
    message = f"{CONFIRM_INTRO}\n\n📊 Exchange: {user_data.get('exchange', '')}\n🖼 Image: {user_data.get('image_id', '')}\n📊 Template: {user_data.get('template', '')}\n"
    # For signals that get/require the margin, the margin is also included.
    if user_data.get("margin"):
        message += f"🖥 Margin: {user_data.get('margin')}\n"
    if user_data.get("username"):
        if len(user_data.get("username", "")) > 0:
            message += f"👤 Username: {user_data.get('username')}\n"
    if user_data.get("date"):
        message += f"📅 Current time: {user_data.get('date')}\n"
    if user_data.get("input_date"):
        message += f"📅 Input time: {user_data.get('input_date')}\n"
    if user_data.get("qr"):
        if len(user_data.get("qr", "")) > 0:
            message += f"🖥 QR Code: {user_data.get('qr')}\n"
    if user_data.get("referral"):
        if len(user_data.get("referral", "")) > 0:
            message += f"🤝 Referral Code: {user_data.get('referral')}"
    return message
