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
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


# It's the user you want to add (``user_id=user_to_add``).



async def main_basE_ot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

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



async def startup_log_all_done():
    try:
        logg.info("Sucessfully Installed Everything")
    except BaseException:
        logg.warning("You Left The Group!\n\nSystem Failure")

async def cant():
    if bot.uid not in bot.uid:
        logg.warning("Can't Access Me\n\nDisconnecting! ")
    return







if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None

    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)

        logg.info("Initialisation finished, no errors")
        logg.info("Starting Black Lightning")
    try:
   
        bot.loop.run_until_complete(main_basE_ot(Var.TG_BOT_USER_NAME_BF_HER))
        bot.loop.run_until_complete(lel())
        logg.info("Completed")
    except Exception:
      pass
            
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
    bot.run_until_disconnected()
    logg.info("Setup Sucessfull! ")
    import os
    logg.info("Sucessfully Connected To Telegram And Your Assistant!")




