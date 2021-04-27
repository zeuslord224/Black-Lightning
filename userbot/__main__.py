#    Copyright (C) KeinShin 2021
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
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import asyncio

import glob
import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient
from userbot.plugins.thunder import bhok
from telethon import *

from telethon.tl.functions.messages import ImportChatInviteRequest


from telethon import functions
from telethon.errors import *
from userbot import CMD_HNDLR, bot, ALIVE_NAME

from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import finnalise, load_module, main_loader


BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT
logg = logging.getLogger("Black Lightning")
assistant_logg = logging.getLogger("Black Lightning")
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else " "



async def cool_noice():
    
    user = await bot.get_me()
    if not user.bot_inline_placeholder:
     await  bot.send_message("me", f"{DEFAULTUSER} Kindly Enable Inline For Accessing All The Features Including `.help` and Many More")
    else:
        logg.info("Everything Loaded!\nLightning Userbot is online!")
    
        await bot.send_message("me", "**Black Lightning Message**\nHi Master I'm On\nDo .alive\nOr `.help` **\n© @lightningsupport")
"Nani TwT!?"

# async def main_basE_ot(bot_token):
#     await bot.start(bot_token)
#     bot.me = await bot.get_me()
#     bot.uid = telethon.utils.get_peer_id(bot.me)

async def assustnat_player(player):
    player.me = await player.get_me()
    player.uid = telethon.utils.get_peer_id(player.m)

async def sed_k():
    await asyncio.sleep(0)
    return

async def lel():
    try:
        log_id = str(Var.PLUGIN_CHANNEL)

        await bot(ImportChatInviteRequest(log_id))

    except UserAlreadyParticipantError:

        return


async def force_join():
    try:
        chet = "lightning_support_channel"
        await bot(ImportChatInviteRequest(chet))
        logg.info("You have been added to support channel so that you will never miss any update!")
    except UserAlreadyParticipantError:
        pass


async def cant():
    user = await bot.get_me()
    if not bot.uid == user.id:
        logg.warning("Can't Access Me\n\nDisconnecting! ")
    return




# async def some_shits(chat):

  
#   try:
#       with bot.takeout() as takeout:
#           await bot.get_messages('me')  # normal call
#           await takeout.get_messages('me')  # wrapped through takeout (less limits)
  
#           for message in takeout.iter_messages(chat, wait_time=0):
#               ...  # Do something with the message

#   except errors.TakeoutInitDelayError as e:
#     print('Must wait', e.seconds, 'before takeout')


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None

    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)


    try:
   
        bot.loop.run_until_complete(force_join()) # Sorry  ppl )
        bot.loop.run_until_complete(lel())
        logg.info("Completed")
    except Exception:
      logg.info("Error! restart if problem continues contact @lightning_support_group")
            
    else:
        bot.start()





    lol = str(ALIVE_NAME)
    logg.info(f"Disconnected From {lol} Can't Load Plugins\nLoading Assistant")

    path3 = "userbot/plugins/*.py"
    files = glob.glob(path3)
    for name in files:
       with open(name) as f:
           path1 = Path(f.name)
           shortname = path1.stem
           if  not  bot.is_connected():
              break
           load_module(shortname.replace(".py", ""))
    


path2 = "userbot/plugins/thunder/*.py"
files = glob.glob(path2)
for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            finnalise(shortname.replace(".py", ""))
         
 






if len(argv) not in (1, 3, 4):
    bot.disconnect()
    logg.info(f"Disconnected From {DEFAULTUSER}")
elif  not  bot.is_connected():
    logg.info(f"Failed Connection To User!")


else:
    bot.loop.run_until_complete(cool_noice())
    bot.run_until_disconnected()
    logg.info("Setup Sucessfull! ")
    # import os
    logg.info("Sucessfully Connected To Telegram And Your Assistant!")




