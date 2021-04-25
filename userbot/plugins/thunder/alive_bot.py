from telethon.tl.custom import button
from var import Var
from telethon import events, custom, Button
from userbot.plugins.sql_helper.admin_sql import *
from userbot import bot
g = Var.TG_BOT_USER_NAME_BF_HER
from userbot.plugins.thunder.admins import omk


import os
from userbot.plugins.thunder import ASSISTANT_HELP, ass_cmd_hndlr

ASSISTANT_PIC = os.environ.get("ASSISTANT_PIC", None)
if ASSISTANT_PIC is None:
       PIC = "https://telegra.ph/file/b5afd12c58bfca1f1d47b.jpg"
else:
       PIC = ASSISTANT_PIC



cation = f"Commands Available\n\n{g}"





@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    buil = event.builder  
    do = [custom.Button.inline("Commands", data="commands")]
    await event.delete()

    await tgbot.send_file(event.chat_id,
            file=PIC,
            caption=cation,
            link_preview=False,
            buttons=do)

@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}alive", from_users=omk))
async def _(event):
 if admin_(event.sender_id) is False:
  return

 buil = event.builder  
 await event.delete()
 
 await tgbot.send_file(event.chat_id,
                 "Admin {}".format(admin_(event.sender_id)))
     


                       
ASSISTANT_HELP.update({
    "alive": "Users/Admin/Owner Command",
     "Type":  "Owner",
    "Command": f"{ass_cmd_hndlr}alive \
    \n**Usage**: An alive for assistant works in group/Personal Message\
    \nDisclaimer: You should add {g} in the particular group for {ass_cmd_hndlr}alive to work in group.\
    \n@"
})