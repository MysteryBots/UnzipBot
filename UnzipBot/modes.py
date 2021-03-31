from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Data import Data


# Modes Message
@Client.on_message(filters.private & filters.command(["modes"]))
async def modes(unzipbot, msg):
    await msg.reply(
        text=Data.MODES,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(Data.home_button),
    )