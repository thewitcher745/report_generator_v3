from telegram import InputMediaPhoto
import csv


# Send a message to the user requeting the update, depending on the type of update (callback or message)
async def send_message(context, update, message_text, keyboard=None):
    if update.callback_query:
        chat_id = update.callback_query.message.chat_id
    else:
        chat_id = update.message.chat_id

    await context.bot.send_message(
        chat_id=chat_id, text=message_text, reply_markup=keyboard
    )


# Send a media group to the user
async def send_media_group(context, update, file_address, caption=None):
    media_group = [InputMediaPhoto(open(file_address, "rb"))]
    if update.callback_query:
        chat_id = update.callback_query.message.chat_id
    else:
        chat_id = update.message.chat_id

    await context.bot.send_media_group(
        chat_id=chat_id, media=media_group, caption=caption
    )


def strip_pair(pair: str) -> str:
    return pair.replace("USDT", "").replace(" Perpetual", "")


def get_pair_precision(symbol: str, exchange: str) -> int | None:
    """
    Get the precision of a symbol for a specific exchange. Returns None if the symbol is not found for that exchange or in the list in general.
    """
    symbol = strip_pair(symbol)
    with open("./static/precisions.csv", "r") as f:
        column_numbers = {
            "binance": 1,
            "bitget": 2,
            "bybit": 3,
            "lbank": 4,
            "mexc": 5,
            "okx": 6,
            "bingx": 7,
        }
        reader = csv.reader(f)
        for row in reader:
            if row[0] == symbol:
                field_string = row[column_numbers[exchange]]
                if field_string:
                    return int(field_string)
                return None

        return None
