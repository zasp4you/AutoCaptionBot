from pyrogram import Client, filters
@Client.on_message(filters.command("start") & filters.private) async def start(client, message): await message.reply("Hey there, I'm AutoChannelCaption Bot for Zasp4you. Zakir Ayoub Developed me on 20 August 2021. \n\nSource code => https://github.com/zasp4you/AutoCaptionBot")
