"""use command .ducduckgo"""

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd("ducduckgo (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if sample_url := "https://duckduckgo.com/?q={}".format(
        input_str.replace(" ", "+")
    ):
        link = sample_url.rstrip()
        await event.edit(
            "Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(input_str, link)
        )
    else:
        await event.edit("something is wrong. please try again later.")
