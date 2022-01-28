import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "githubs":

        await event.edit(input_str)

        animation_chars = [
            "https://github.com/KeinShin/Black-Lightning",
            "https://github.com/KeinShin/Black-Lightning",
        ]

        animation_interval = 0.1

        animation_ttl = range(101)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 2])
