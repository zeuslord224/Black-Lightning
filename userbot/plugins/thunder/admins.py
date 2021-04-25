# by kienshin dude

from userbot.plugins.sql_helper import admin_sql
from userbot.plugins.sql_helper.botusers_sql import *
from userbot.plugins.sql_helper.admin_sql import *
from userbot import bot
from userbot.plugins.thunder import ASSISTANT_HELP, ass_cmd_hndlr

from telethon import *
a = []
import os
import io


def ADMINS(): 
    sed=[]

    for i in str(users()):
        sed.append(i)

    return sed

omk = tuple(ADMINS())
omk=''.join(omk)
@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}promote", from_users=omk ))
async def admins(event):
    msg = await event.get_reply_message()
    
    if event.fwd_from:
        return
    async with tgbot.conversation(event.chat_id) as conv:

     if admin_sql.is_admin(msg.id):
       

         await conv.send_message('You are already an admin!')
     else:
      
         await conv.send_message('Input Userid')
         id = await conv.get_response()
         await conv.send_message(f'Sucessfully Promoted user {id}')
         admin_sql.make_admin(id)
         add_me_in_db(id)
    # elif



#    Copyright (C) Midhun KM 2020

def starkusers(event):
    if event.query.user_id == bot.uid:
  
        total_users = users()
        users_list = "Tottal Admins\n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name='adminslist.txt'
            return tedt_file



@tgbot.on(events.NewMessage(pattern=f"^{ass_cmd_hndlr}demote", from_users=omk))
async def kooladmins(event):
    msg = await event.get_reply_message()
    
    if event.fwd_from:
        return
    async with tgbot.conversation(event.chat_id) as conv:

     if admin_sql.demote(msg.id):
       

         await conv.send_message('You are already an admin!')
     else:
      
         await conv.send_message('Enter Userid who you want to demote')
         id = await conv.get_response()
         await conv.send_message(f'Sucessfully Promoted user {id}')
         admin_sql.demote(id)
    # elif



ASSISTANT_HELP.update({
    "admins": "Admin Command",
    "Type":  "Owner",
    "Command": f"{ass_cmd_hndlr}promote | {ass_cmd_hndlr}demote\
    \n**Usage**: Promotes the input user id as your bot admin\
    \nDisclaimer: He / She can use such commands like {ass_cmd_hndlr}alive, {ass_cmd_hndlr}hack, etc.\
    \n\n"
})