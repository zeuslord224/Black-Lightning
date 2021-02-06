import glob
import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from userbot.plugins.thunder import bhok




from telethon import functions

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
        bot.loop.run_until_complete(main_basE_ot(Var.TG_BOT_USER_NAME_BF_HER))
        logg.info("Completed")
    else:
        bot.start()





   
try:
 
    
    path3 = "userbot/plugins/*.py"
    files = glob.glob(path3)
    for name in files:
       with open(name) as f:
           path1 = Path(f.name)
           shortname = path1.stem
           load_module(shortname.replace(".py", ""))
           
except Exception:
 logg.info(f"Disconnected From {DEFAULTUSER}\n Connected To Assistant")
 pass
finally:
    path2 = "userbot/plugins/thunder/*.py"
    files = glob.glob(path2)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            finnalise(shortname.replace(".py", ""))
       
 






try:
    bot.run_until_disconnected()
except Exception:
 logg.info(f"Disconnected From {DEFAULTUSER}\nTrying Connection To Assistant")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
    logg.info(f"Disconnected From {DEFAULTUSER}")
else:

  logg.info("Setup Sucessfull! ")
  import os
  logg.info("Sucessfully Connected To Telegram!")
  logg.info("Black Lightning Installed\n\n.alive and @lightningsupport For Any Kind Of Help")



