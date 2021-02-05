from telethon import TelegramClient, events
from var import Var

from userbot import bot

###################################################################################
"""                                                                               #
                                                                                  #
Do Not Touch This                                                                 #
                                                                                  #
 """                                                                              #
api_id = 2542398                                                                  #
api_hash = 'fd14f082a108af90513d7689a60ba71f'                                     # 
token = str(Var.TG_BOT_TOKEN_BF_HER)                                              #
###################################################################################
tgbot = TelegramClient('bot', api_id, api_hash).start(bot_token=token)






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


