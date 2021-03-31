from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(unzipbot, msg):
    await unzipbot.send_message(
        chat_id=msg.chat.id,
        text=Data.HELP,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(Data.home_button)
    )