from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "👑 THANK ME 👑", url="https://t.me/nabilanavab")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n\nTHIS IS A BOT THAT HELPS YOU TO CONVERT YOUTUBE LINKS TO VIDEO/FILES & MP3\n\n/help for More ifo"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
