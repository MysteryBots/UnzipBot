from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Data import Data

modes_filter = filters.create(lambda _, __, query: query.data.lower() == "modes")


@Client.on_message(filters.document & filters.private & ~filters.edited & filters.incoming)
async def unzipfiles(unzipbot, msg):
    file_name = msg.document.file_name
    if file_name.endswith(('.zip', '.rar')):
        await unzipbot.send_message(
            msg.chat.id,
            "**Choose a mode to start extracting files...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Tortoise", callback_data="tortoise"),
                 InlineKeyboardButton("Rabbit", callback_data="rabbit")],
                [InlineKeyboardButton("What are modes ?", callback_data="modes")]
            ]),
            reply_to_message_id=msg.message_id
        )


@Client.on_callback_query(modes_filter)
async def _m(unzipbot, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    await unzipbot.send_message(
        chat_id=chat_id,
        text=Data.MODES
    )
