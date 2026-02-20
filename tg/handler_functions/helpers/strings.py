from tg.handler_functions.helpers.multiple_config import LEVERAGE_SEQUENCE

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

PRECISION_NOT_FOUND = "⚠️ Warning: Precision not found for the selected coin. Using the precision given by the signal text."

MULTIPLE_NEED_SIGNAL = "❌ Please forward a signal first, then use /multiple."
MULTIPLE_GET_N_REPORTS = "❓ Enter total number of images to generate:"
MULTIPLE_INVALID_N_REPORTS = "❌ Invalid number. Please enter a valid integer."


def MULTIPLE_REPORT_PROGRESS(current: int, total: int) -> str:
    msg = f"📝 **Report {current}/{total}**"
    if LEVERAGE_SEQUENCE:
        # current is 1-indexed, so we use (current - 1) to get the correct leverage from the sequence
        leverage = LEVERAGE_SEQUENCE[(current - 1) % len(LEVERAGE_SEQUENCE)]
        msg += f" (Leverage: {leverage}x)"
    return msg


MULTIPLE_GET_CHANNEL_ONCE = "❓ Select the channel for this mass sending session:"


def MULTIPLE_GET_CHANNEL(current_index: int, n_reports: int) -> str:
    return f"❓ Select channel for report {current_index}/{n_reports}:"


MULTIPLE_INVALID_CHANNEL = "❌ Invalid channel selection. Please select again."

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
    if user_data.get("period_start"):
        message += f"📅 Period start: {user_data.get('period_start')}\n"
    if user_data.get("period_end"):
        message += f"📅 Period end: {user_data.get('period_end')}\n"
    if user_data.get("pnl_percent") is not None:
        message += f"📈 PnL %: {user_data.get('pnl_percent')}\n"
    if user_data.get("qr"):
        if len(user_data.get("qr", "")) > 0:
            message += f"🖥 QR Code: {user_data.get('qr')}\n"
    if user_data.get("referral"):
        if len(user_data.get("referral", "")) > 0:
            message += f"🤝 Referral Code: {user_data.get('referral')}"
    return message
