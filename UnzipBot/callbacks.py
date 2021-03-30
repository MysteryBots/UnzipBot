from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import Config
from Data import Data


help_filter = filters.create(lambda _, __, query: query.data.lower() == "help")
home_filter = filters.create(lambda _, __, query: query.data.lower() == "home")
deploy_filter = filters.create(lambda _, __, query: query.data.lower() == "deploy")
about_filter = filters.create(lambda _, __, query: query.data.lower() == "about")


# Callbacks
@Client.on_callback_query(home_filter)
async def _h(unzipbot, callback_query):
	chat_id = callback_query.from_user.id
	message_id = callback_query.message.message_id
	user = await unzipbot.get_me()
	mention = user["mention"]
	await unzipbot.edit_message_text(
		chat_id=chat_id,
		message_id=message_id,
		text=Data.START.format(callback_query.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons),
	)


@Client.on_callback_query(about_filter)
async def _a(unzipbot, callback_query):
	chat_id = callback_query.from_user.id
	message_id = callback_query.message.message_id
	await unzipbot.edit_message_text(
		chat_id=chat_id,
		message_id=message_id,
		text=Data.ABOUT,
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(Data.home_button),
	)


@Client.on_callback_query(help_filter)
async def _hh(unzipbot, callback_query):
	chat_id = callback_query.from_user.id
	message_id = callback_query.message.message_id
	await unzipbot.edit_message_text(
		chat_id=chat_id,
		message_id=message_id,
		text=Data.HELP,
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(Data.home_button),
	)


@Client.on_callback_query(deploy_filter)
async def _d(unzipbot, callback_query):
	chat_id = callback_query.from_user.id
	message_id = callback_query.message.message_id
	await unzipbot.edit_message_text(
		chat_id=chat_id,
		message_id=message_id,
		text=Data.DEPLOY,
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(Data.home_button),
	)