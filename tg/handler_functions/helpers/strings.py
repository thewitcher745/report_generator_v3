"""
This file contains the strings returned by the bot to the user, collected in a single file for brevity.
"""

# Welcome message
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
