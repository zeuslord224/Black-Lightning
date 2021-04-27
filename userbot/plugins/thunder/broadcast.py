 # By KeinShin !
 # Easy i know lol.
import asyncio
from telethon import *
from userbot.plugins.thunder.admin import omk
from userbot.plugins.thunder import ass_cmd_hndlr, ASSISTANT_HELP, oowner

from userbot.plugins.sql_helper.admin_sql import *
from userbot.plugins.sql_helper.idadder_sql import *
from userbot import ALIVE_NAME, bot

wow = str(ALIVE_NAME)
pub = str(users())
wh = len(pub.split())
h = pub.split()


# users.split
very_Ded2 = oowner()
very_Ded2 = very_Ded2.wah # Wew
@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}broadcast", from_users=very_Ded2.id)) # @tgbot.on(
    # events.NewMessage(
    #     pattern="^/broadcast ?(.*)", func=lambda e: e.sender_id == bot.uid
    # )

async def board(event):
    no = 0
    user=await bot.get_me()
    if user.id == event.sender_id:

      await tgbot.send_message(event.chat_id, 'Input the message that has to be boardcasted.')
    
      msg = await tgbot.get_response().text
      await asyncio.sleep(1.5)
      await tgbot.send_message(event.chat_id, f'Ok brodcasting  __{msg}__ to **{wh}** Users!')
      
    try:
       

       for user in range(1, wh):
        user=h[no]
        await tgbot.send_message(user, f'**A Message is Boardcasted by {wow}\n\n__{msg}__')
    except Exception as e:
        await tgbot.send_message(event.chat_id, f'**Error**: While Brodcasting __{msg}__ to **{wh}** Some Users and Groups!\n\n**Try again or contact\n**The following error with the users or groups are \n\n`{e}`')


# @tgbot.on(events.NewMessage(pattern="^/boardcast", from_users=very_Ded2.id))

ASSISTANT_HELP.update