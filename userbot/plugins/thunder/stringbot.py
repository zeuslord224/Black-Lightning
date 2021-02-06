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
from userbot import bot as hn
from userbot.plugins.thunder import bhok
from telethon import TelegramClient as assitant_client
from telethon.sessions import StringSession as assistant_string
from telethon.errors.rpcerrorlist import  PhoneCodeInvalidError


from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"

TEXT = """Hi, {}.
This is Your Assitant Now As a String Session Generator Bot. I will generate String Session of your Telegram Account.
Now send your `API_ID` same as `APP_ID` to Start Generating Session."""


NOT_VAILD = "Do /string This Not Vaild"
PHONE_NUMBER = (
    "Now send your Telegram account's Phone number in Indian Format. \n"
    "Including Country code. Example: **+91 XXXXX XXXXX**\n\n"
    "Press /cancel to Cancel Task."
)
NUMBER_ERROR = (
    f"{DEFAULTUSER} Seems This Number Is Already Registered"
)

TWO_STEPS_VERI = (" Semms That You Have Two Steps Verifcation Input Password")



loggingd = logging.getLogger("STRING BOT ")




from userbot import bot as lol
bgusername = Var.TG_BOT_USER_NAME_BF_HER
token = Var.TG_BOT_TOKEN_BF_HER

@bhok.on(events.NewMessage(pattern="^/start"))
async def string(event):    


    if not await hn.is_user_authorized():
    

        await bhok.send_message(
            event.chat_id,
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
    elif event.sender_id == lol.uid:
        await bhok.send_message(
            event.chat_id,
            message=f"**Hi Master\n\nI'm Your Assistant Any One Can Contact Me To Get The String Session via {bgusername}**",
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
           await bhok.send_message(
            event.chat_id,
            message=f"**Press Start For Making String**",
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
@bhok.on(events.callbackquery.CallbackQuery(data=re.compile(b"start00")))

async def ass_string(event):   
    global assitant_client

    await event.delete()

    async with bhok.conversation(event.chat_id) as conv:

     sender = await event.get_input_sender()
     await conv.send_message('Send Your APP_ID')
     api = await conv.get_response()

     await conv.send_message("Now Tell You API_HASH")
     hash = await conv.get_response()
     client = assitant_client(
    'client',
    api_id=api,
    api_hash=hash
)
     await conv.send_message("Now Send You Phone Number\nAs +91 xxxxxxxxx if Indian Else Your Country Format")
     contact = str(conv.get_response())
     phone=contact.text
     bhok = client
     await bhok.connect()
     await asyncio.sleep(0)
    try: 
     await bhok.send_code_request(phone=phone)
    except Exception:
      bhok.disconnect()
      return 
    await conv.send_message("Send The Code Something Like 1 6 8 9")
    

    code = await conv.get_response()
    code_tf = None
    code = "".join(code.split(" "))
    token = Var.TG_BOT_TOKEN_BF_HER
    client = bhok   
    user = await client.get_me()
    current_client = bhok
    await current_client.connect()
    try:
        await client.sign_in(contact, code)
    except PhoneCodeInvalidError:
        await conv.send_message(NOT_VAILD)
        return
    except Exception as e:
        loggingd.info(str(e))
        await conv.send_message("Looks Like You have Two Step Verification Enter Password")
        so = await conv.get_response()
        code_tf = so.message.message.strip()
        passw = await conv.get_response()
        await client.sign_in(contact, code, password=code_tf)
        assitant_client = await current_client.get_me()
        loggingd.info(assitant_client.stringify())
    session_string = current_client.session.save()
    await conv.send_message(event.chat_id, f"`{session_string}`")
    assitant_client = await current_client.get_me()
    try:    
        await conv.send_message(f"Thanks For Creating String Session Via {bgusername}\n\nCheck You Saved Message")
        striing=current_client.session.save()
        await bhok.send_message("me", f'{striing}')
    except Exception:
        await conv.send_message("Number Not Vaild /string To Restart")




# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(ass_string())



def Api_Hash_Id(APP_IDS, API_HASHS):
    id = len(APP_IDS)
    indexs = random.randint(0, len(id) - 1)
    return APP_IDS[indexs], API_HASHS[indexs]
