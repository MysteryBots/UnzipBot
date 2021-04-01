import os
import shutil
import time
import zipfile
import rarfile
from datetime import datetime
from pyrogram import Client, filters
from UnzipBot.functions import absolute_paths, progress
from pyrogram.errors import FloodWait

tortoise_filter = filters.create(lambda _, __, query: query.data.lower() == "tortoise")


@Client.on_callback_query(tortoise_filter)
async def _tortoise(unzipbot, callback_query):
    start = datetime.now()
    msg = callback_query.message.reply_to_message
    await callback_query.message.delete()
    file_name = msg.document.file_name
    file_size = msg.document.file_size
    if file_size > 1524288000:
        await msg.reply("Files with size more than 500 MB aren't allowed.", quote=True)
        return
    try:
        main = await msg.reply("Downloading...", quote=True)
        file = await msg.download(progress=progress, progress_args=(main, "Downloading..."))
        await main.edit("Extracting Files...")
        if file_name.endswith(".zip"):
            with zipfile.ZipFile(file, 'r') as zip_ref:
                contents = zip_ref.namelist()
                zip_ref.extractall("downloads")
            dir_name = file.replace(".zip", "")
        if file_name.endswith(".rar"):
            with rarfile.RarFile(file, 'r') as rar_ref:
                contents = rar_ref.namelist()
                rar_ref.extractall("downloads")
            dir_name = file.replace(".rar", "")
        con_msg = await msg.reply("Checking Contents for you...", quote=True)
        constr = ""
        for a in contents:
            b = a.replace(f"{dir_name}/", "")
            constr += b + "\n"
        ans = "**Contents** \n\n" + constr
        if len(ans) > 4096:
            await con_msg.edit("Checking Contents for you... \n\nSending as file...")
            f = open("contents.txt", "w+")
            f.write(ans)
            f.close()
            await msg.reply_document("contents.txt")
            os.remove("contents.txt")
        else:
            await msg.reply(ans)
        await con_msg.delete()
        extracted_files = [i async for i in absolute_paths(dir_name)]
        number = 0
        for file in extracted_files:
            try:
                number += 1
                sending = await msg.reply(f"**Uploading... ({number}/{len(extracted_files)})**")
                await msg.reply_document(file, quote=False, progress=progress,
                                         progress_args=(sending, f"Uploading... ({number}/{len(extracted_files)})"), disable_notification=True)
                await sending.delete()
            except FloodWait as e:
                time.sleep(e.x)
        stop = datetime.now()
        await msg.reply(
            f"Extraction Done Successfully..! \n\nTook {round((stop - start).total_seconds() / 60, 2)} minutes \n\nFor more bots visit @MysteryBots")
    except rarfile.RarCannotExec:
        await msg.reply("**ERROR :** This File is possibly bugged. Cannot extract content. \n\n"
                        "This may happen when a file's extension is manually changed to `.zip`/`.rar` even when file isn't in that format. \n\n"
                        "Try with some other file please.", quote=True
                        )
    except Exception as e:
        await unzipbot.send_message(msg.chat.id, "**ERROR : **" + str(
            e) + "\n\nForward this message to @MysteryBots too solve this problem.")
    finally:
        if os.path.isdir("downloads"):
            shutil.rmtree("downloads")