from userbot.helper.img_helprs import crtooonify
from userbot.utils import lightning_cmd

from userbot import bot
import os


@bot.on(lightning_cmd(pattern="toonify"))
async def toon(fy):
    oh=await bot.download_media(await fy.get_reply_message(), './pics')
    ok = crtooonify(oh)
    await bot.send_file(fy.chat_id, ok, force_document=False)
    os.remove('cartoonify.png')