"""Quickly make a decision
Syntax: .decide"""
import requests

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("decide"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.reply_to_msg_id or event.message.id
    r = requests.get("https://yesno.wtf/api").json()
    await borg.send_message(
        event.chat_id, r["answer"], reply_to=message_id, file=r["image"]
    )
    await event.delete()
