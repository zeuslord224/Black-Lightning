from userbot import bot

ASSISTANT_HELP = {}
import os, asyncio 
ASSISTANT_CMD_HNDLR = os.environ.get("ASSISTANT_CMD_HNDLR", None)
if ASSISTANT_CMD_HNDLR is None:
    ASSISTANT_CMD_HNDLR = "/"
else:
   ass_cmd_hndlr = ASSISTANT_CMD_HNDLR


async def cmd():
    commn = "ls userbot/plugins/thunder"
    process = await asyncio.create_subprocess_shell(
        commn, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    o=o.split()

    return len(o)


class oowner:
      
  async def very_Ded(self):
       self.wah=await bot.get_me()
       return self.wah
  
