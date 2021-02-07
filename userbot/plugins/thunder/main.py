

#    Copyright (C) 2021 KeinShin

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>

import asyncio
from telethon import TelegramClient, events, custom, Button, events
from telethon.utils import pack_bot_file_id
from telethon.events.common import EventBuilder
from userbot.plugins.thunder import is_owner, get_message, is_users, is_not
from var import Var
from userbot.plugins.sql_helper.user_sql import *
import coffeehouse

from coffeehouse.lydia import LydiaAI


from PIL import Image, ImageDraw, ImageFont
from userbot import ALIVE_NAME



LYDIA_AP = {}
SESSION_ID = {}


import os
temp = Var.TEMP_DOWNLOAD_DIRECTORY 
CHAT_BOT = os.environ.get("CHAT_BOT", None)
ASSISTANT_PIC = os.environ.get("ASSISTANT_PIC", None)
if ASSISTANT_PIC is None:
    PIC = "https://telegra.ph/file/b5afd12c58bfca1f1d47b.jpg"
else:
    PIC = ASSISTANT_PIC

CHAT_BOT_API = os.environ.get("CHAT_BOT_API", None)
if CHAT_BOT_API is None:
    C_API = "e20daaf7e63f680cb1ba4d004a85981873f75ba260f2253e57ded815add3c2bab3388c085c8ad5469faf798bd1bfc2000edc6876566ae584d7db07623a9b7328"
else:
    C_API = CHAT_BOT_API



    lydia_ley = C_API
    client = coffeehouse.API(lydia_ley)
    Lydia = LydiaAI(client)


@tgbot.on(events.NewMessage(pattern="^/start"))
async def send_welcome(event):
      from userbot import bot
      pis = PIC
      co = await bot.get_me()
      if event.sender_id == co.id:
        owner = str(ALIVE_NAME)
        bot = "Hi! I'm Your Assistant Master\n\nAny One Can Contact You Via Me\n\nI'll Get users messages to you\n\n[ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ ᴜsᴇʀʙᴏᴛ](https://github.com/KeinShin/Black-Lightning)"
     #    pis = pic()
        await tgbot.send_file(
             event.chat_id,
             pis,
             text=bot,
             buttons=[
                 [custom.Button.inline("❤️Users❤️", data="users")],
                 [
                     custom.Button.url(
                 "Help!", "t.me/lightningsupport")
                 ],
                 [custom.Button.inline("Chat Bot", data="chat_bot")],
                 [
                     custom.Button.inline(
                 "Commands", data="commands")
                 ]
                         ])

      else:
             user = await event.get_sender()
             owner = str(ALIVE_NAME)
             kok = f"**Hello {user.username}!\n\n Thanks for Contacting {owner}\n\nI'm assistant of {owner} Kindly Leave Your Message**\n\nFeatured By [ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ ᴜsᴇʀʙᴏᴛ](https://github.com/KeinShin/Black-Lightning)"
             await tgbot.send_file(
                  event.chat_id,
                  pis,
                  caption=kok,
                  buttons=[
                      [custom.Button.inline("Commands", data="commands")],
                      [
                          custom.Button.url(
                      "Help!", "t.me/lightningsupport")
                      ]
                              ])
           


                            # @tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))

import re

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"commands")))                            
async def commands(event):
   from userbot import bot
   co = await bot.get_me()
   username = Var.TG_BOT_USER_NAME_BF_HER
   commanss = f"Commands For {username} listed Here!\n\n/alive\n/hack\n/id\n/trans\n/yta `music link` ( will download in audio format ) \n\ytv `music link` (will downloa in video format)"
   await tgbot.send_message(event.chat_id, commanss)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat_bot")))                            
async def commands(event):
   from userbot import bot
   os.environ['CHAT_BOT'] = 'ENABLE'
   co = await bot.get_me()
   if CHAT_BOT == "ENABLE":
    tgbot.send_message(event.chat_id,  
    "Chat Bot Already Enabled",
    buttons=[custom.Button.inline("Deactivate", data="lol_nvm")])
    return
   username = Var.TG_BOT_USER_NAME_BF_HER
   kok = f"**What Chat Bot Do?**\n\n**Answer - Chatbot Will Activate Artificial intelligence Of Your Bot\nIn Short Bot Will Chat With The User Like a Human**"
   await tgbot.send_message(event.chat_id,  
   kok,
   buttons=[custom.Button.inline('🙎Activate🙎', data='activate')])

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"activate")))    
async def chatboot(event):
    from userbot import bot
    me = await bot.get_me()
    await tgbot.send_message("Chat Bot Activated")

    kek = await event.get_reply_message()
    id = his_userid(kek.id)
    session = Lydia.create_session()
    session_id = session.id
    LYDIA_AP.update({str(event.chat_id) + " " + str(id.from_id): session})
    SESSION_ID.update(
            {str(event.chat_id) + " " + str(id.from_id): session_id}
        )


@tgbot.on(events.NewMessage(incoming=True))
async def user(ai):
    ai.text
    if CHAT_BOT == "DISABLE":
        return
    try:
        session = LYDIA_AP[str(ai.chat_id) + " " + str(ai.from_id)]
        session_id = SESSION_ID[str(ai.chat_id) + " " + str(ai.from_id)]
        messages = ai.text
        async with ai.client.action(ai.chat_id, "Typing"):
            text = session.think_thought((session_id, messages))
            wait_time = 0
            for i in range(len(text)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await ai.reply(text)
    except KeyError:
        return


@tgbot.on(events.NewMessage(pattern="^Hi"))
async def send_welcome(event):
      ssendr = event.sender_id
      from userbot import bot
      
      if ssendr == bot.uid:
       await tgbot.send_message(event.chat_id, "**Hi! Master If You Want That I Talk!**\n\n**Kindly Enable Chatbot**\n\n**You Can Chat With Me :)**")
      else:
       await tgbot.send_message(event.chat_id, "**Hi! How Can I Help?**\n\n**Kindly Leave The Message**\n\n**You Can Chat With Me :)**")



@tgbot.on(events.NewMessage(pattern="^Help"))
async def send_welcome(event):
    user =str(ALIVE_NAME)
    await tgbot.send_message(event.chat_id, f"**Kindly Leave The Message**\n\n**I Will Pass It To {user}**")

@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def get_message(event):
    from userbot import bot
    co = await bot.get_me()
    if present_in_userbase(event.sender_id):
        return
    if event.sender_id == co.id:
        return
    if event.raw_text.startswith("/"):
        return
    await event.get_sender()
    chet = await event.forward_to(co.id)
    add_to_userbase(chet.id, event.sender_id, event.id)

# Thanks To Stark Gang and Friday Userbot
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
    from userbot import bot
    mhg = await event.get_reply_message()
    co = await bot.get_me()
    if mhg is None:
        return
    mhg.id
    mhg_s = event.raw_text
    user_id, reply_message_id = his_userid(mhg.id)
    if event.sender_id == co.id:
        return
    elif event.raw_text.startswith("/"):
        return
    elif event.text is not None and event.media:
        bot_api_file_id = pack_bot_file_id(event.media) # Thanks To Friday Userbot
        await tgbot.send_file(
            user_id,
            file=bot_api_file_id,
            caption=event.text,
            reply_to=reply_message_id,
        )
    else:
        mhg_s = event.raw_text
        await tgbot.send_message(
            user_id,
            mhg_s,
            reply_to=reply_message_id,
        )    




