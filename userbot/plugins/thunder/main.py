

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
def pic():
   ASSISTANT_PIC = os.environ.get("ASSISTANT_PIC", None)
   if ASSISTANT_PIC is None:
       PIC = "https://telegra.ph/file/b5afd12c58bfca1f1d47b.jpg"
    #    tgbot.download_media()
       img = Image.open(PIC)
       img.save("pic.png")
       Name = ALIVE_NAME
       ig_font = ImageFont.truetype('.resources/fonts/MakeupPersonalUseRegular-8Vpz.ttf',100)
       cc = ImageDraw.Draw('pic.png')
       cc.text(xy=(100, 200), text=f"Asssistant Of\n{Name}", fill=(0, 0, 0), font=ig_font)
       
   else:
       PIC = ASSISTANT_PIC


from userbot import bot as cool

@tgbot.on(events.NewMessage(pattern="^/start"))
async def send_welcome(event):
    global cool
    builder = event.builder
    img = Image.open(pic)
    if event.sender_id == cool.uid:
       owner = str(ALIVE_NAME)
       cool = "Hi! I'm Your Assistant Master\n\nAny One Can Contact You Via Me"
       result = tgbot.send_file(
            file=pic('pic.png'),
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
       await result
    else:
           user = await event.get_user()
           owner = str(ALIVE_NAME)
           cool = f"**Hello {user}!\n\n Thanks for Contacting {owner}\n\nI'm assistant of {owner} Kindly Leave Your Message**"
           result = tgbot.send_file(
                event.chat_id,
                pic(),
                caption=cool,
                buttons=[
                    [custom.Button.inline("Commands", data="commands")],
                    [
                        custom.Button.url(
                    "Help!", "@lightningsupport")
                    ]
                            ])
           await result


                            # @tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))

import re

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"commands")))                            
async def commands(event):
  got = await tgbot.get_me()


  if not event.send_id == cool.uid:
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
    if event.sender_id == cool.uid:
        return
    if event.raw_text.startswith("/"):
        return
    await event.get_sender()
    chet = await event.forward_to(cool.uid)
    add_to_userbase(chet.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
    mhg = await event.get_reply_message()
    if mhg is None:
        return
    mhg.id
    mhg_s = event.raw_text
    user_id, reply_message_id = his_userid(mhg.id)
    if event.sender_id != cool.uid:
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
