from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Data import Data


# On Files
@Client.on_message(filters.document & filters.private & ~filters.edited & filters.incoming)
async def unzip_files(unzipbot, msg):
    file_name = msg.document.file_name
    if file_name.endswith(('.zip', '.rar')):
        await unzipbot.send_message(
            msg.chat.id,
            Data.CHOOSE_MODE,
            reply_markup=InlineKeyboardMarkup(Data.modes_buttons),
            reply_to_message_id=msg.message_id
        )