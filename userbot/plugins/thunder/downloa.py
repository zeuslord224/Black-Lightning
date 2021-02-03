import functools
import inspect
import logging
import re
from pathlib import Path

from telethon import events
import os
from telethon import functions
from var import Var as Car
from userbot import CMD_LIST, LOAD_PLUG
from userbot import bot
from userbot.plugins.upcomings.thunder import bot as fore
from userbot.Config import Var
from userbot.thunderconfig import Config

login_print = logging.getLogger("ASSISTANT BOOT")

def ok():
    cd = Car.ASSISTANT_PIC
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
     os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    photo = None

    photo = fore.download_media(  # pylint:disable=E0602
            cd, Var.TEMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
        )
    
    file = fore.upload_file(photo)  # pylint:disable=E0602
          
    fore(functions.photos.UploadProfilePhotoRequest(file))
   # pylint:disable=C0103,W0703
        
        
def main_loader(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"userbot/plugins/thunder/{shortname}.py")
        name = "userbot.plugins.thunder.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        load = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(load)

        login_print.info("Imported" + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        download_path = Path(f"userbot/plugins/assistant/{shortname}.py")
        name = "userbot.plugins.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, download_path)
        load_plugin = importlib.util.module_from_spec(spec)
        load_plugin.tgbot = bot.tgbot
        spec.loader.exec_module(load_plugin)
        sys.modules[
            "userbot.plugins.assistant" + "Initialising Lightning" + shortname
        ] = load_plugin
        login_print.info("Setting Up Assistant  " + shortname)


def finnalise(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"userbot/plugins/thunder/{shortname}.py")
        name = "userbot.plugins.mybot.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        login_print.info("Imported" + shortname)

    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"userbot/plugins/thunder/{shortname}.py")
        name = "userbot.plugins.mybot.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["userbot.plugins.thunder." + shortname] = mod
        print("Imported " + shortname)