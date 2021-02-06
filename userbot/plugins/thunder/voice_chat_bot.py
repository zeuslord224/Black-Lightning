from  userbot.plugins.thunder import bhok
import pyaudio
import wave
import sys
from userbot.utils import admin_cmd, sudo_cmd
from var import Var

import asyncio
from playsound import playsound

import pyglet

from telethon.sessions import StringSession
import os


from userbot import bot

import wget
from youtubesearchpython import SearchVideos
from telethon import *



CHAT_ID =  os.environ.get("CHAT_ID", -1001291663564)
OWNER_IDS =  os.environ.get("OWNER_IDS", 1311769691)

ASSISTANT_MUSIC = os.environ.get("ASSISTANT_MUSIC", None)
if ASSISTANT_MUSIC is not None:
    session_name = str(ASSISTANT_MUSIC)
    player = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    player = None

# def generate_sample(file):
    
#     CHUNK = 1024
#     FORMAT = pyaudio.paInt16
#     CHANNELS  = 2
#     RATE = 44100
#     RECORD_SECONDS=5
#     p = pyaudio.PyAudio()
#     stream = p.open(format=FORMAT,
#     channels=CHANNELS,
#     rate=RATE,
#     input=True,
#     frames_per_buffer=CHUNK)
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#       data = stream.read(CHUNK)
#       frames.append(data)

#     stream.stop_stream()


@player.on(events.NewMessage(pattern="ytmusic ?(.*)", 
                               from_users=CHAT_ID))

async def _(event):
    if event.fwd_from:
        return

    lol =  event.sender_id  
    url = event.pattern_match.group(1)
    search = SearchVideos(f"{url}", offset=1, mode="dict", max_results=1)
    sed = search.result()
    keke = sed["search_result"]
    mo = keke[0]["link"]
    thumails = keke[0]["title"]
    tittlle = keke[0]["id"]
    thumailss = keke[0]["channel"]
    sel = f"https://img.youtube.com/vi/{tittlle}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    if not os.path.isdir("./music/"):
        os.makedirs("./music/")
    path = Var.TEMP_DOWNLOAD_DIRECTORY
    gggg = wget.download(sel, out=path)
    music = (
        f'youtube-dl --force-ipv4 -q -o "./music/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 128k '
        + mo
    )
    os.system(music)
    await asyncio.sleep(4)
    cong = f"./music/{thumails}.mp3"
    if os.path.exists(cong):
        await event.edit("`Song Downloaded Sucessfully. Playing")
    else:
        await event.edit("`Error Try Again.`")
    capy = f"**Song Name ➠** `{thumails}` \n**Requested For ➠** `{url}` \n**Channel ➠** `{thumailss}` \n**Requested By ➠** `[User]({lol})`"
    await player.send_file(
        event.chat_id,
        cong,
        force_document=False,
        allow_cache=False,
        caption=capy,
        thumailsb=gggg,
        performer=thumailss,
        buttons=[custom.Button.inline("End", data="region_lol")],
        supports_streaming=True,
    )
    await player(playsound(f'{thumails}.mp3'))
    
    
    
    
# WO Knows For Later Purpose
# async def main(cong):
#     music  = await bhok(pyglet.resource.media(cong, streaming=False) )
#     await bhok(music.play())

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

 
    


