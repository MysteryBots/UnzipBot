import humanize
import time
import os
from pyrogram.errors import FloodWait


async def progress(current, total, message, process):
    new_current = humanize.naturalsize(current)
    new_total = humanize.naturalsize(total)
    percentage = round((current * 100) / total, 2)
    try:
        await message.edit(f"**{process}** \n\n**Progress :** {new_current}/{new_total} | {percentage}℅")
    except FloodWait as e:
        time.sleep(e.x)


async def absolute_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
