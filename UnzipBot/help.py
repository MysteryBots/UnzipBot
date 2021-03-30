from Data import Data
from Config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def start(unzipbot, msg):
	print("/help")
	await unzipbot.send_message(
		msg.chat.id,
		Data.HELP,
		reply_markup=InlineKeyboardMarkup(Data.buttons),
	)