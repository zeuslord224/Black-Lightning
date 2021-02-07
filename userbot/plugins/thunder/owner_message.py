from userbot.plugins.sql_helper.user_sql import *
from telethon.utils import pack_bot_file_id



@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def message(event):
    send_r = await event.get_reply_message()
    from userbot import bot
    if send_r is None:
        return
    send_r.id
    send_mssg = event.raw_text
    id = event.sender_id
    user_id, reply_message_id = his_userid(send_r.id)
    if id == bot.uid:
        if send_mssg.startswith("/"):
            return
        if event.text is not None and event.media:
            # if sending media
            bot_api_file_id = pack_bot_file_id(event.media)
            await tgbot.send_file(user_id, file=bot_api_file_id, caption=event.text, reply_to=reply_message_id)
        else:
            await tgbot.send_message(user_id, send_mssg, reply_to=reply_message_id)
