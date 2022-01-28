from userbot import topfunc
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd
from var import Var

idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "4.0"
telever = "5.0"

amiusingsudo = "Active ✅" if issudousing else "Inactive ❌"
logchat = "Connected ✅" if islogokay else "Dis-Connected ❌"
riplife = "Connected ✅" if isherokuokay else "Not Connected ❌"
wearenoob = "Active ✅" if gdriveisshit else "Inactive ❌"
gendu = "Added ✅" if rmbg else "Not Added ❌"
starknoobs = "Added ✅" if wttrapi else "Not Added ❌"
meiko = "Added ✅" if hmmok else "Not Added ❌"
dbstats = "Fine ✅" if isdbfine else "Not Fine ❌"
if Config.PRIVATE_GROUP_BOT_API_ID is None:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
if Var.LIGHTNING_PRO.lower() == "NO":
    light_pr = "NO"
else:
    lightning_pr = "YES"

lightning_status = (
    f"Sorry Sir In Some Plugin There Is A Telegram Bug\n"
    f"Pls Try To Understand\n"
    f"Instead Do .help <cmd name>\n\n"
    f"VERSION = {currentversion} \n"
    f"DATABASE = {dbstats} \n"
    f"SUDO = {amiusingsudo} \n"
    f"LOG-CHAT = {logchat} \n"
    f"HEROKU = {riplife} \n"
    f"G-DRIVE = {wearenoob}"
)
