from telethon import *

import asyncio
from userbot.plugins.thunder import ASSISTANT_HELP, ass_cmd_hndlr

from var import Var
from userbot.utils import errors2, errors_s, logs
from userbot import bot
g = Var.TG_BOT_USER_NAME_BF_HER
@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}errors", func=lambda e: e.sender_id == bot.uid))
async def _(event):
 try:
    await event.edit(f'**Getting Assistant {g} Error Logs.**')
    await asyncio.sleep(2)
    await tgbot.send_file(event.chat_id, errors2(), caption='Assistant Logs')
    await event.delete()

 except Exception as e:
    await tgbot.send_message(e)
    await event.delete()


@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}geterrors", func=lambda e: e.sender_id == bot.uid))
async def geterrors(event):
    number=0
    await event.edit(f'**Getting the errors of  {g}.**')
    await asyncio.sleep(2)
    while True:
     number+=1
     con = logs()

     if 'Traceback' in con:
 
      await tgbot.send_file(event.chat_id, errors2(), caption=f'**Some Errors in line {number} , `{con}`\n\nReport it to @lightning_support_group**')
      await event.delete()
     else:
      await tgbot.send_message(event.chat_id, f'`{con}`\n\n**Everything is good, Enjoy!**')
    
      await event.delete()


ASSISTANT_HELP.update({
    "bot_logs": "Assistant Command.",
    "bot_logs's Type":  "Assistant Command, Owner",
    "Command": f"{ass_cmd_hndlr}errors | {ass_cmd_hndlr}geterrors\
    \n**Usage**:{ass_cmd_hndlr}errors will get userbot logs as a file | {ass_cmd_hndlr}geterrors Gets where the error is."
})