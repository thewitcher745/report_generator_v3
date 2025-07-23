from telegram import InputMediaPhoto


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
