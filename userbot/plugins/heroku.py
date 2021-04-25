# By  KeinShin

import heroku3

from var import Var
import asyncio
from userbot import bot as light, CMD_HELP, CMD_HNDLR

# lazy
heroku_conn = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_conn.apps()
app = heroku_conn.apps()[Var.HEROKU_APP_NAME]
NAME = []

from userbot.utils import *
@light.on(lightning_cmd(pattern="set var ?(.*)"))
async def heroku(event):
 if event.fwd_from:
   return
 try: 
    lo = event.pattern_match.group(1)
    old_var, new_var = lo.split(' ')
    app = heroku_conn.apps()[Var.HEROKU_APP_NAME]
    config = app.config()
    if lo == " ":
     await event.edit("**The Proper Way To Use This `set var 'key' 'value'`")
    else:
     config[str(old_var)] = str(new_var)
 except Exception as e:
    await event.edit(e)



@light.on(lightning_cmd(pattern="del var ?(.*)"))
async def heroku(event):
 if event.fwd_from:
   return 
 try: 
    lo = event.pattern_match.group(1)

    app = heroku_conn.apps()[Var.HEROKU_APP_NAME]
    config = app.config()
    if lo == " ":
      await event.edit("**The Proper Way To Use This `set var 'key' 'value'`")
    else:    
     config[str(lo)] = None
     await event.edit("`Var Deleted Sucessfully`")
 except Exception as e:
    await event.edit(e)

@light.on(lightning_cmd(pattern="get var ?(.*)"))
async def heroku(event):
 if event.fwd_from:
   return 

 try:
    await event.edit("Getting Var!")
    lo = event.pattern_match.group(1)

    app = heroku_conn.apps()[Var.HEROKU_APP_NAME]
    config = app.config()
    if lo in config:
     await event.edit(f"`Your Current Value For The Key `{lo}` is  {0}".format(config[lo]))
    else:
     await event.edit(f"`No Var Found For`{lo}`")
 except Exception as e:
    await event.edit(e)

@light.on(lightning_cmd(pattern="app(.*)"))
async def heroku(event):
 if event.fwd_from:
      return 
 lo = event.pattern_match.group(1)
 app = heroku_conn.apps()[Var.HEROKU_APP_NAME]
 if lo == ' ':
      await event.edit(f'Dear the command is {CMD_HNDLR}app restart | killdynos | kd | name | releases')
 if lo == 'restart':

  try:
     await event.edit("Restarting Your Userbot")
     await asyncio.sleep(2)
     await event.edit("**Dynos Restarted For The Bot**")
     app.restart()
  except Exception as e:
     await event.edit(e)
  if lo == 'name':
      await light.send_message(event.chat_id, 'Currrent App  name in which userbot is running! {}'.format(Var.HEROKU_APP_NAME))
  if lo == 'collabs':
      collaboratorlist = str(app.collaborators())
      sxy = collaboratorlist.split("\n")
      await light.send_message(event.chat_id, f"Total collaborators in {Var.HEROKU_APP_NAME} are\n\n{sxy}")



@light.on(lightning_cmd(pattern="releases(.*)"))
async def realse(event):
  if event.fwd_from:
      return 
  try:
     lo = int(event.pattern_match.group(1))
  except ValueError:
     await event.edit('Value Error, It must be a number!')
  try:
   sed = heroku_conn.apps()[Var.HEROKU_APP_NAME].releases(order_by='version', limit=lo, sort='desc')
   app.releases(order_by='version', limit=lo, sort='desc')
  
   await light.send_message(event.chat_id, f"The {lo} Recent releases of  {Var.HEROKU_APP_NAME} are\n\n`{sed}`\n\n@lightningsupport")
  except Exception as e:
      await light.send_message(event.chat_id, e)
import os
TZ =   os.environ.get("TZ", None)
if TZ is None:
   TZ = 'Asia/Kolkata'

   

@light.on(lightning_cmd(pattern="create(.*)"))
async def create(event):
   if event.fwd_from:
          return 
   nope = event.pattern_match.group(1)
   NAME.index({f"{nope}"})
 
   try:
      await light.send_message(event.chat_id, f"An app is created with the name {nope}\n\nbut No Addon Found {CMD_HNDLR}addon (app name) (plan_name)")
      heroku_conn.create_app(name=nope, stack_id_or_name='cedar', region_id_or_name=TZ)
   
   except Exception as e:
      await light.send_message(event.chat_id, e)

@light.on(lightning_cmd(pattern="addon(.*)"))
async def addon(event):
   if event.fwd_from:
      return 
   sed = event.pattern_match.group(1)
   sed30 = event.pattern_match.group(1).split()[2]
   # addonservice = heroku_conn.addon_services(sed30)
   app_name = ''.join(NAME)
   app = heroku_conn.apps()[app_name]
   app.install_addon(plan_id_or_name=sed30, config={})
   try:
    await light.send_message(event.chat_id, f'Addon sucessfully installed in {sed}\n\n**@lightningsupport')
   except Exception as e:
    await light.send_message(event.chat_id, f'Addon can not be installed due to\n\n {e}')
    
CMD_HELP.update({
   "heroku": f"Helpers your app {Var.HEROKU_APP_NAME}\
   \n**Usage**: Helps in setting and getting  var\
   \n\nCommands\
   \n\n{CMD_HNDLR}set var (var name) (key value)\
   \n**Usage**: Sets the given value as a var\
   \n\n{CMD_HNDLR}get var (var name)\
   \n**Usage**: Get input var from heroku.\
   \n\n{CMD_HNDLR}app restart | name  | collabs\
   \n**Usage**:{CMD_HNDLR}app restart, to restart the  userbot | {CMD_HNDLR}app name, to get the name of heroku app | {CMD_HNDLR}app colabs, gets the curent collaboratos in you heroku app {Var.HEROKU_APP_NAME}\
   \n\n{CMD_HNDLR}releases number\
   \n**Usage**: Get the last given releases\
   \n\n{CMD_HNDLR}create (app name)\
   \n**Usage**: Creates an heroku app with desired name.\
   "
})




# Thats it :)