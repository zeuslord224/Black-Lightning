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
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import asyncio
import logging

import random
import re


from var import Var
from telethon import client, events, Button, custom
import os
from userbot import bot as hn
from telethon import TelegramClient as assitant_client
from telethon.sessions import StringSession as assistant_string
from telethon.errors.rpcerrorlist import  *
from userbot.plugins.thunder import ASSISTANT_HELP, ass_cmd_hndlr

from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"




loggingd = logging.getLogger("STRING BOT ")




from userbot import bot as lol
bgusername = Var.TG_BOT_USER_NAME_BF_HER
token = Var.TG_BOT_TOKEN_BF_HER

STRING_BOT_PIC = os.environ.get("STRING_BOT_PIC", None)
if STRING_BOT_PIC is None:
    STRINGER_PIC = "https://telegra.ph/file/597b5ac659cda77b66198.jpg"
else:
    STRINGER_PIC = STRING_BOT_PIC

@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}string"))
async def string(event):    
    lol = await lol.get_me()

    if not await hn.is_user_authorized():
    

        await tgbot.send_message(
            event.chat_id,
            STRINGER_PIC,
            message=f"Press Start For Making String ",
            buttons=[
                [
                    custom.Button.inline(
                        "Start ",
                        data="start00"
                    )
                ],
                [Button.url("Api Hash Bot", "t.me/UseTGXBot")],
            ],
        )
    elif event.sender_id == lol.id:
        await tgbot.send_file(
            event.chat_id,
            STRINGER_PIC,
            text=f"**Hi Master\n\nI'm Your Assistant Any One Can Contact Me To Get The String Session via {bgusername}**",
            buttons=[
                [
                    custom.Button.inline(
                        "Start ",
                        data="start00"
                    )
                ],
                [Button.url("Api Hash Bot", "t.me/UseTGXBot")],
            ],
        )
    else:     
           await tgbot.send_file(
            event.chat_id,
            STRINGER_PIC,
            text=f"**Press Start For Making String**",
            buttons=[
                [
                    custom.Button.inline(
                        "Start ",
                        data="start00"
                    )
                ],
                [Button.url("Api Hash Bot", "t.me/UseTGXBot")],
            ],
        )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start00")))

async def ass_string(event):   
    global assitant_client

    await event.delete()

    async with tgbot.conversation(event.chat_id) as conv:
     

     sender = await event.get_input_sender()
     await conv.send_message('Send Your APP_ID')
    
     app_id = int(await conv.get_response().text)

     
    await conv.send_message("Now Tell You API_HASH")
    hash = await conv.get_response()
    hash_api=hash.text

    await conv.send_message("Now Send Your Phone Number\nAs +91 xxxxxxxxx if Indian Else Your Country Format\n\n**Note:** it is not stored!")
    phone = str((await conv.get_response()).text)

    tgboto = await assitant_client('strig', app_id, hash_api)
    await tgboto.connect()
    try:
     
     await tgboto.send_code_request(phone=phone, force_sms=False)
     
    except AuthRestartError:
     await conv.send_message("**Time Out!**")
     return
    except PhoneNumberBannedError:
     await conv.send_message("**Banned Telegram Number!**")
     return
    

    
    await conv.send_message("Send The Code Something Like 1 6 8 9")
     

    code = await conv.get_response()
    code_tf = None 
    code = "".join(code.split(" "))
    # token = Var.TG_BOT_TOKEN_BF_HER
    

    user = await client.get_me()
    client, current_client = tgboto
    try:
        await tgboto.sign_in(phone, code)
    except PhoneCodeInvalidError:
        await conv.send_message('Not Valid!, {retry}')
        return
    except PhonePasswordProtectedError:
        await conv.send_message("Looks Like You have Two Step Verification, Enter Password")
        so = await conv.get_response()
        code_tf = so.message.message.strip()
        passw = await conv.get_response()
        await tgboto.sign_in(phone, code, password=code_tf)
        # assitant_client = await current_client.get_me()
    session_string = tgboto.session.save()
    await conv.send_message(event.chat_id, f"`{session_string}`")
    assitant_client2 = await tgboto.get_me()
    try:    

        striing=tgboto.session.save()

        await conv.send_message(f"Thanks For Creating String Session Via {bgusername}\n\n{striing}")
    except Exception:
        await conv.send_message("Number Not Vaild /string To Restart")







ASSISTANT_HELP.update({
    "stringbot": "String Session Generator Global Command",
    "stringbot's Type": "String Session Generator",
    "Command": f"{ass_cmd_hndlr}string\
    \n**Usage**: Globaly Creates String for all users!\
    \n\n**Note**: No data is stored anywhere!"
})