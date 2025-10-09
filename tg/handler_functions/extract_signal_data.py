"""
This file contains the handler that extract the signal data from the forwarded message.
"""

from tg.handler_functions.helpers.conversation_stages import (
    GET_EXCHANGE as GET_EXCHANGE_STAGE,
    END,
)
from tg.handler_functions.helpers.utilities import send_message
from tg.handler_functions.helpers.regex import (
    symbol as regex_symbol,
    signal_type as regex_signal_type,
    leverage as regex_leverage,
    entry as regex_entry,
    targets as regex_targets,
    stop as regex_stop,
)
from tg.handler_functions.helpers.strings import INVALID_SIGNAL, SIGNAL_CONFIRMATION
from tg.handler_functions.helpers.prompts import prompt_get_exchange


async def extract_signal_data(update, context):
    """
    Processes the signal to extract its data.
    """

    signal_text: str = update.message.text.lower()

    # Process the signal to extract its data
    symbol = regex_symbol(signal_text).replace(" Perpetual", "").upper()
    signal_type = regex_signal_type(signal_text)
    leverage = int(regex_leverage(signal_text))
    entry = float(regex_entry(signal_text))
    targets = [float(target) for target in regex_targets(signal_text)]
    stop = float(regex_stop(signal_text))

    # If any of the sections are not found correctly, return the invalid signal message
    if not all([symbol, signal_type, leverage, entry, targets, stop]):
        await send_message(
            context,
            update,
            INVALID_SIGNAL,
        )
        return END

    # Assign the extracted data to the user_data dictionary
    context.user_data["symbol"] = symbol
    context.user_data["signal_type"] = signal_type
    context.user_data["leverage"] = leverage
    context.user_data["entry"] = entry
    context.user_data["targets"] = targets
    context.user_data["stop"] = stop

    # If the signal is valid, send the confirmation message and the prompt for getting the exchange
    await send_message(
        context,
        update,
        SIGNAL_CONFIRMATION(symbol, signal_type, leverage, entry, targets, stop),
    )
    
    await prompt_get_exchange(update, context)

    return GET_EXCHANGE_STAGE
