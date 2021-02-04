from telethon import TelegramClient, events
from var import Var



api = Var.APP_ID
hash = Var.API_HASH



token = str(Var.TG_BOT_TOKEN_BF_HER)
userb_bot = TelegramClient('bot', api, f'{hash}').start(bot_token=token)
bot = TelegramClient('bot', api, f'{hash}').start(bot_token=token)


def is_owner(event):
    if event.query.user_id == cool.uid:
        pass



def is_users(event):
 if event.query.user_id not in cool.uid:
        pass

def is_not(user):
    a = user.id
    return a




def get_message(event):
    return event.reply(event.text)        


