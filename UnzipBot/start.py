from Data import Data
from Config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(unzipbot, msg):
    print("/start")
    user = await unzipbot.get_me()
    mention = user["mention"]
    await unzipbot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )