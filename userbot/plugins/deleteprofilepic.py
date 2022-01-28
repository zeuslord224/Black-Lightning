from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import InputPhoto

from uniborg.util import lightning_cmd


@borg.on(lightning_cmd(pattern="delpfp ?(.*)"))
async def remove_profilepic(delpfp):
    """ For .delpfp command, delete your current profile picture in Telegram. """
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = [InputPhoto(
                id=sep.id,
                access_hash=sep.access_hash,
                file_reference=sep.file_reference,
            ) for sep in pfplist.photos]
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(f"`Successfully deleted {len(input_photos)} profile picture(s).`")
