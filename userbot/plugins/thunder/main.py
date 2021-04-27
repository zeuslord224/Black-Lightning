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
import heroku3
from userbot.plugins.heroku_h import *

# from pyrogram import *


from math import ceil

from telethon import TelegramClient, events, custom, Button, events
from telethon.utils import pack_bot_file_id
from telethon.events.common import EventBuilder
from userbot.plugins.thunder import ASSISTANT_HELP, cmd
from var import Var
from userbot.plugins.sql_helper.users_sql import *
from userbot.plugins.thunder.admin import omk
from userbot.plugins.sql_helper.idadder_sql import *
import coffeehouse

from coffeehouse.lydia import LydiaAI
from userbot.function.heroku_helper import HerokuHelper
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
from userbot.plugins.thunder.admin import ADMINS
from PIL import Image, ImageDraw, ImageFont
from userbot import ALIVE_NAME, bot

how = []
total_cmds = []

LYDIA_AP = {}
SESSION_ID = {}


import os
temp = Var.TEMP_DOWNLOAD_DIRECTORY 
CHAT_BOT = os.environ.get("CHAT_BOT", None)
GROUP_ASSITANT = os.environ.get("GROUP_ASSITANT", None)

ASISTANT_CMD_ROWS = os.environ.get("GROUP_ASSITANT", None)
if ASISTANT_CMD_ROWS is None:
   ASISTANT_CMD_ROWS = 7
else:
   number_of_rows_in_commands = ASISTANT_CMD_ROWS



plugs = []



ASISTANT_CMD_COLUMNS = os.environ.get("GROUP_ASSITANT", None)
if ASISTANT_CMD_COLUMNS is None:
   ASISTANT_CMD_COLUMNS = 5
else:
   number_of_columns_in_commands = ASISTANT_CMD_COLUMNS


   
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
                     [custom.Button.inline("Chat Bot😸", data="chat_bot")],
                     
                     [
                         custom.Button.inline(
                     "Commands", data="commands")
                     ]
                             ])
      elif   event.sender_id == omk:
            text =  'Hi Admin\nYou Can use the features avaiable in Black Lightning\n\nTo See current features for admins do /admincommand'

            await tgbot.send_file(
                 event.chat_id,
                 pis,
                 text=text,
                 buttons=[
                     [custom.Button.inline("❤️Users❤️", data="users")],
                     [
                         custom.Button.url(
                     "Help!", "t.me/lightningsupport")
                     ],                     
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

@tgbot.on(events.NewMessage(pattern="^/commands")) 
async def command(event):
    for i in ASSISTANT_HELP:
        if i.startswith('_'):
            return
        plugs.append(i)
    des = sorted(plugs)
    
    buttons = assitant_help(0, ASSISTANT_HELP, 'help')
    if des in ASSISTANT_HELP:

     await event.edit("**Total Commands for assistant {}**".format(len(des)), buttons=buttons)


@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"_total_cmds_(.*)")
   )
)
async def lightning_pugins_query_hndlr(event):
    command = ASSISTANT_HELP['Command']
    cmd = event.data_match.group(1).decode("UTF-8")
    type = ASSISTANT_HELP[f"{cmd}'s Type"]
    try:
    
     if cmd in ASSISTANT_HELP:
        assistant_help_strin = f"**✡ Type : {type} ✡**"
        assistant_help_strin  += f"**🔺 COMMAND 🔺 :** `{cmd}` \n\n{command}"
        
        assistant_buttons = assistant_help_strin 
        assistant_buttons += "\n\n**In Case Any Problem @lightning_support_grup**".format(cmd)
        await event.edit(assistant_buttons)
    
    except KeyError:
        await event.answer("The command isn't displayable", cache_time=0, alert=True)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"help_prev\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(lightning):
    
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = assitant_help(
            lightning_page - 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)




@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"help_next\((.+?)\)")
    )
)   
async def ass_pugins_query_hndlr(lightning):
        await lightning.delete()
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        
        buttons = assitant_help(
            lightning_page + 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
        )
        # https://t.me/TelethonsChat/115200
        await lightning.edit(buttons)

# help taken from telebot :)
def assitant_help(b_lac_krish, lightning_plugs, lightning_lol):

 total_cmds = []
 for p in lightning_plugs:
     if not p.startswith("_"):
         total_cmds.append(p)
 total_cmds = sorted(total_cmds)
 plugins = [
     custom.Button.inline(
         "{}".format( x), data="_total_cmds_{}".format(x)
     )
     for x in total_cmds
 ]
 pairs = list(zip(plugins[::number_of_columns_in_commands], plugins[1::number_of_columns_in_commands]))
 if len(plugins) % number_of_columns_in_commands == 1:
     pairs.append((plugins[-1],))
 max_fix = ceil(len(pairs) / number_of_rows_in_commands)
 total_cmds_pages = b_lac_krish % max_fix
 
 if len(pairs) > number_of_rows_in_commands:
   if cmd()>number_of_rows_in_commands: 
   

     pairs = pairs[
         total_cmds_pages * number_of_rows_in_commands : number_of_rows_in_commands * (total_cmds_pages + 1)
     ] + [
         (
             custom.Button.inline(
                 "Previous", data="{}_prev({})".format(lightning_lol, total_cmds_pages)
             ),
            
            custom.Button.inline(
                 "Next", data="{}_next({})".format(lightning_lol, total_cmds_pages)
             ),
             
         )
     ]
   else:
     pairs = pairs[
         total_cmds_pages * ASISTANT_CMD_ROWS : ASISTANT_CMD_ROWS * (total_cmds_pages + 1)
     
     ]

 return pairs





@tgbot.on(events.NewMessage(pattern="^!ask ?(.*)"))
async def ask(event):
    ok = await bot.get_me()
    if event.sender_id == ok.id:
     user=ALIVE_NAME
     await tgbot.send_message(f"Hi Dear,\n\nNow you can ask your question i'll send it to {user}")

@tgbot.on(events.NewMessage(pattern="^/admincommand", from_users=omk))
async def _(event):
    await tgbot.send_message(
        event.chat_id,
        ''''Admin Commands are listed below
        /alive
        /hack
        /string
        /admins
        
        Commands in Admins --> /promote, /demote 
        '''
    )




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat_bot")))                            
async def commands(event):
   from userbot import bot

   co = await bot.get_me()

   if CHAT_BOT == "ENABLE":
    tgbot.send_message(event.chat_id,  
    "Chat Bot Already Enabled",
    buttons=[custom.Button.inline("Deactivate", data="lol_nvm")])
   else:
    kok = f"**What Chat Bot Does?**\n\n**Answer - Chatbot Will Activate Artificial intelligence Of Your Bot\nIn Short Bot Will Chat With The User Like a Human**"
    await tgbot.send_message(event.chat_id,  
    kok,
    buttons=[custom.Button.inline('🙎Activate🙎', data='activate')])

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"activate")))    
async def chatboot(event):
    from userbot import bot
    app= Heroku.app(Var.HEROKU_APP_NAME)
    var=app.config()
    var[CHAT_BOT] = 'ENABLE'
    me = await bot.get_me()
    await tgbot.send_message(event.chat_id, "Chat Bot Activated")
    app = Heroku.app(Var.HEROKU_APP_NAME)

    kek = await event.sender_id
    id = his_userid(kek.id)
    session = Lydia.create_session()
    session_id = session.id
    LYDIA_AP.update({str(event.chat_id) + " " + str(id.from_id): session})
    SESSION_ID.update(
            {str(event.chat_id) + " " + str(id.from_id): session_id}
        )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_nvm")))    
async def chatboot(event):
    from userbot import bot
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    heroku_var[CHAT_BOT] = 'DISABLE'
    me = await bot.get_me()
    
    await tgbot.send_message(event.chat_id, "Chat Bot Deactivated")

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
    if ai.raw_text.startswith("!ask"): 
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
      if CHAT_BOT == 'ENABLE':
          return
      ssendr = event.sender_id
      from userbot import bot
      ko=await bot.get_me()
      
      if ssendr == ko.id :
       await tgbot.send_message(event.chat_id, "**Hi! Master If You Want That I Talk!**\n\n**Kindly Enable Chatbot**\n\n**You Can Chat With Me :)**")
      
      else:
       await tgbot.send_message(event.chat_id, "**Hi! How Can I Help?**\n\n**Kindly Leave The Message**\n\n**You Can ask my master by doin !ask :)**")



@tgbot.on(events.NewMessage(pattern="^Help"))
async def send_welcome(event):
    if CHAT_BOT == 'ENABLE':
     return
    user =str(ALIVE_NAME) # U s k a B a s  c h a l e  t o  s a r a d a r i y a  p i i  j a y e, a a e k h u d a  t u  b o l d e   t e r e   b a d l o  k o 
    
    sendr = event.sender_id
    from userbot import bot
    
    owner=await bot.get_me()
      
    if sendr == owner.id :
       await tgbot.send_message(event.chat_id, "**Hi! Master If You Want That I Talk!**\n\n**Kindly Enable Chatbot Then, You Can Chat With Me :)**")
    else:
       await tgbot.send_message(event.chat_id, f"**Kindly Leave The Message**\n\n**I Will Pass It To {user}**")


