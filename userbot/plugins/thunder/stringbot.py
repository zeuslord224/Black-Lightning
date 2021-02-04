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
from telethon import events, Button, custom
from telethon import TelegramClient as assitant_client
from telethon.sessions import StringSession as assistant_string
from telethon.errors.rpcerrorlist import  PhoneCodeInvalidError

bgusername = Var.TG_BOT_USER_NAME_BF_HER
token = str(Var.TG_BOT_TOKEN_BF_HER)
userb_bot = assitant_client('bot', api, f'{hash}').start(bot_token=token)
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"

TEXT = """Hi, {}.
This is Your Assitant Now As a String Session Generator Bot. I will generate String Session of your Telegram Account.
Now send your `API_ID` same as `APP_ID` to Start Generating Session."""
LOGGING = """Assitant
**ID**: {APP_ID}
**HASH**: {API_HASH}
[Current User ID](tg://user?id={C}): {C}
[Logged In User ID](tg://user?id={L}): {L}"""

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


from userbot.plugins.thunder import userb_bot as cleine

from userbot import bot


@cleine.on(events.NewMessage(pattern="^/string"))
async def string(event):    
    if not await userb_bot.is_user_authorized():
        await userb_bot.send_message(
            event.chat_id,
            message=f"Press Start For Making String ",
            buttons=[
                [
                    custom.Button.inline(
                        "Start ",
                        data="start",
                    )
                ],
                [Button.url("Api Hash Bot", "@UseTGXBot")],
            ],
        )
    elif event.query.user_id == bot.uid:
        await userb_bot.send_message(
            event.chat_id,
            message=f"Hi Master\n\nI'm Your Assistant Any One Can Contact Me To Get The String Session via {bgusername}",
            buttons=[
                [
                    custom.Button.inline(
                        "Start ",
                        data="start",
                    )
                ],
                [Button.url("Api Hash Bot", "@UseTGXBot")],
            ],
        )
    else:     
           await userb_bot.send_message(
            event.chat_id,
            message=f"Press Start For Making String ",
            buttons=[
                [
                    custom.Button.inline(
                        "Start ",
                        data="start",
                    )
                ],
                [Button.url("Api Hash Bot", "@UseTGXBot")],
            ],
        )
@cleine.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def ass_string(event):   
    global assitant_client
    sender = await event.get_input_sender()
    api = await cleine.get_entity(sender, 'Enter You API ID')
    hash = await cleine.get_entity(sender, 'Enter You API HASH')
    contact = await cleine.get_entity(sender, '+91 xxxxxxxxx if Indian Else You Country Format')
    await cleine.send_code_request(contact)
    
    code = cleine.get_entity('Enter The Code: Something Like 1 9 6 8 ')
    code_tf = None
    code = "".join(code.split(" "))


    userb_bot = assitant_client('bot', api, f'{hash}').start(bot_token=token) 

    client = userb_bot

    me = await client.get_me()


    async with event.client.conversation(event.chat_id) as conv:
        await conv.send_message(PHONE_NUMBER)
        response = conv.wait_event(events.NewMessage(
            chats=event.chat_id
        ))
        response = await response
        loggingd.info(response)
        phone = response.message.message.strip()
        current_client = userb_bot
        await current_client.connect()

        try:
            await current_client.sign_in(phone, code=code, password=code_tf)
        except PhoneCodeInvalidError:
            await conv.send_message(NOT_VAILD)
            return
        except Exception as e:
            loggingd.info(str(e))
            await conv.send_message(
                TWO_STEPS_VERI,
            )
            response = conv.wait_event(events.NewMessage(
                chats=event.chat_id
            ))
            response = await response
            loggingd.info(response)
            code_tf = response.message.message.strip()
            await current_client.sign_in(password=code_tf),
            assitant_client = await current_client.get_me()
            loggingd.info(assitant_client.stringify())
        session_string = current_client.session.save()
        await conv.send_message(f"`{session_string}`")
        assitant_client = await current_client.get_me()

    try:    
        await cleine.send_message(sender, f"Thanksk For Creating String Session Via {bgusername}\n\nCheck You Saved Message")
        striing=current_client.session.save()
        await userb_bot.send_message("me", f'{striing}')
    except Exception:
        await conv.send_message("Number Not Vaild /string To Restart")








def Api_Hash_Id(APP_IDS, API_HASHS):
    id = len(APP_IDS)
    indexs = random.randint(0, len(id) - 1)
    return APP_IDS[indexs], API_HASHS[indexs]
