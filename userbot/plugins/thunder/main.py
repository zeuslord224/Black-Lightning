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


from telethon import TelegramClient, events, custom, Button, events
from telethon.utils import pack_bot_file_id
from telethon.events.common import EventBuilder
from userbot.plugins.thunder import is_owner, get_message, is_users, is_not
from var import Var
from userbot.plugins.sql_helper.user_sql import *

from PIL import Image, ImageDraw, ImageFont
from userbot import ALIVE_NAME

import os
temp = Var.TEMP_DOWNLOAD_DIRECTORY 
from userbot.plugins.thunder.stringbot import tgbot
ASSISTANT_PIC = os.environ.get("ASSISTANT_PIC", None)
if ASSISTANT_PIC is None:
    PIC = "https://telegra.ph/file/b5afd12c58bfca1f1d47b.jpg"
else:
    PIC = ASSISTANT_PIC


from userbot import bot as cool

@tgbot.on(events.NewMessage(pattern="^/start"))
async def send_welcome(event):
    global cool
    pis = PIC
    co = await cool.get_me()
    if event.sender_id == co.id:

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


ACC_LYDIA = {}
SESSION_ID = {}

import os
temp = Var.TEMP_DOWNLOAD_DIRECTORY 

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
from userbot import bot as cool

@tgbot.on(events.NewMessage(pattern="^/start"))
async def send_welcome(event):
    global cool
    pis = PIC
    co = await cool.get_me()
    if event.sender_id == co.id:
       owner = str(ALIVE_NAME)
       cool = "Hi! I'm Your Assistant Master\n\nAny One Can Contact You Via Me\n\nI'll Get users messages to you\n\nFeatured by [Black Lightning Userbot]"
    #    pis = pic()
       await tgbot.send_file(
            event.chat_id,
            pis,
            text=cool,
            buttons=[
                [custom.Button.inline("❤️Users❤️", data="users")],
                [
                    custom.Button.url(
                "Help!", "@lightningsupport")
                ],
                [
                    custom.Button.inline(
                "Commands", data="commands")
                ]
                        ])

    else:
           user = await event.get_user()
           owner = str(ALIVE_NAME)
           cool = f"**Hello {user}!\n\n Thanks for Contacting {owner}\n\nI'm assistant of {owner} Kindly Leave Your Message**"
           await tgbot.send_file(
                event.chat_id,
                pis,
                caption=cool,
                buttons=[
                    [custom.Button.inline("Commands", data="commands")],
                    [custom.Button.inline("Chat Bot", data="chat_bot")]
                    [
                        custom.Button.url(
                    "Help!", "@lightningsupport")
                    ]
                            ])
           


                            # @tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))

import re

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"commands")))                            
async def commands(event):
   co = await cool.get_me()
   username = Var.TG_BOT_USER_NAME_BF_HER
   commanss = f"Commands For {username} listed Here!\n\n/alive\n/hack\n\id\n/trans\n/yta `music link` ( will download in audio format ) \n\ytv `music link` (will downloa in video format)"
   await tgbot.send_message(event.chat_id, commanss)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat_bot")))    
async def remcf(event):
    if event.fwd_from:
        return
    me = await cool.get_me()
    if event.sender_id == me:
     await event.send_message("Chat Bot Activated")
    else:
     async with tgbot.conversation(event.chat_id) as conv:

      
      id = await event.sender_id
      session = Lydia.create_session()
      session_id = session.id
      ACC_LYDIA.update({str(event.chat_id) + " " + str(id.from_id): session})
      SESSION_ID.update(
            {str(event.chat_id) + " " + str(id.from_id): session_id}
        )


@tgbot.on(events.NewMessage(pattern="^Hi"))
async def send_welcome(event):
    await tgbot.send_message("**Hi! How Can I Help?**\n\n**Kindly Leave The Message**")



@tgbot.on(events.NewMessage(pattern="^Help"))
async def send_welcome(event):
    await tgbot.send_message("**Kindly Leave The Message**")

@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def get_message(event):
    co = await cool.get_me()
    if present_in_userbase(event.sender_id):
        return
    if event.sender_id == co.id:
        return
    if event.raw_text.startswith("/"):
        return
    await event.get_sender()
    chet = await event.forward_to(co.id)
    add_to_userbase(chet.id, event.sender_id, event.id)
    id = await event.sender_id
    session = Lydia.create_session()
    session_id = session.id
    ACC_LYDIA.update({str(event.chat_id) + " " + str(id.from_id): session})
    SESSION_ID.update(
          {str(event.chat_id) + " " + str(id.from_id): session_id}
        )

@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
    mhg = await event.get_reply_message()
    co = await cool.get_me()
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

       owner = str(ALIVE_NAME)
       cool = "Hi! I'm Your Assistant Master\n\nAny One Can Contact You Via Me"
    #    pis = pic()
       await tgbot.send_file(
            event.chat_id,
            pis,
            text=cool,
            buttons=[
                [custom.Button.inline("❤️Users❤️", data="users")],
                [
                    custom.Button.url(
                "Help!", "@lightningsupport")
                ],
                [
                    custom.Button.inline(
                "Commands", data="commands")
                ]
                        ])

    else:
           user = await event.get_user()
           owner = str(ALIVE_NAME)
           cool = f"**Hello {user}!\n\n Thanks for Contacting {owner}\n\nI'm assistant of {owner} Kindly Leave Your Message**"
           await tgbot.send_file(
                event.chat_id,
                pis,
                caption=cool,
                buttons=[
                    [custom.Button.inline("Commands", data="commands")],
                    [
                        custom.Button.url(
                    "Help!", "@lightningsupport")
                    ]
                            ])
           


                            # @tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))

import re

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"commands")))                            
async def commands(event):
  got = await tgbot.get_me()


  if not event.send_id == co.id:
    await event.delete()
    commands = "Hello!\n\nKidnly Add Assitant In Some Group To Access This Feature"
    await tgbot.send_message(event.chat_id,
            message=commands,
            buttons=[
                [
                    Button.url(
                        "Add", f"t.me/{got.username}?startgroup=true"
                    )
                ],
            ],
        )
  else:
   username = Var.TG_BOT_USER_NAME_BF_HER
   commanss = f"Commands For {username} listed Here!\n\n/alive\n/hack\n\id\n/trans\n/yta `music link` ( will download in audio format ) \n\ytv `music link` (will downloa in video format)"
   await tgbot.send_message(event.chat_id, commanss)

@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def get_message(event):
    if present_in_userbase(event.sender_id):
        return
    if event.sender_id == co.id:
        return
    if event.raw_text.startswith("/"):
        return
    await event.get_sender()
    chet = await event.forward_to(co.id)
    add_to_userbase(chet.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
    mhg = await event.get_reply_message()
    if mhg is None:
        return
    mhg.id
    mhg_s = event.raw_text
    user_id, reply_message_id = his_userid(mhg.id)
    if event.sender_id != co.id:
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
