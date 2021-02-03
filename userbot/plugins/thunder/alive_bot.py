from telethon.tl.custom import button
from var import Var
from telethon import events, custom, Button
from userbot import bot
g = Var.TG_BOT_USER_NAME_BF_HER


import os

ASSISTANT_PIC = os.environ.get("ASSISTANT_PIC", None)
if ASSISTANT_PIC is None:
       PIC = "https://telegra.ph/file/b5afd12c58bfca1f1d47b.jpg"
else:
       PIC = ASSISTANT_PIC



cation = f"Commands Available\n\n{g}"





@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    buil = event.builder  
    do = [custom.Button.inline("Commands", data="commands")]
    await event.delete()

    await tgbot.send_file(event.chat_id,
            file=PIC,
            caption=cation,
            link_preview=False,
            buttons=do)

import re

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"commands")))                            
async def commands(event):
   username = Var.TG_BOT_USER_NAME_BF_HER
   commanss = f"Commands For {username} listed Here!\n\n/alive\n/hack\n\id\n/trans\n/yta `music link` ( will download in audio format ) \n\ytv `music link` (will downloa in video format)"
   await bot.send_message(event.chat_id, commanss)            