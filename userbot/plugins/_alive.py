from userbot import bot as light
from userbot.utils import lightning_cmd
import cv2




@light.on(lightning_cmd(pattern="alive"))
async def alive(event):
   if event.fwd_from:
       return
   txt=""" """
   await light.send_file(event.chat_id, txt) 

