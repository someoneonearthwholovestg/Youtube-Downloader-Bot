from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single video links (No playlist).. /n/n Just send a YouTube link Or search using @vid inline mode."
    await message.reply_text(helptxt)
