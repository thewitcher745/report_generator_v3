"""
This file contains the strings returned by the bot to the user, collected in a single file for brevity.
"""

# Welcome message
WELCOME = "🙏 Welcome. Forward a signal to continue."

# Cancel message
CANCEL = "❌ Operation canceled. Use /start to start over."

# Signal confirmation message
SIGNAL_CONFIRMATION_INTRO = "👇 This is the information entered. If it's incorrect, use /cancel to end the process."


def SIGNAL_CONFIRMATION(symbol, trade_type, leverage, entry_price, targets):
    return f"{SIGNAL_CONFIRMATION_INTRO}\n\n💰 Symbol: {symbol}\n💰 Type: {trade_type}\n⬆️ Leverage: {leverage}\n⏎ Entry: {entry_price}\n☑️ Targets: {targets}"
