#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7336591985:AAG6qGwrkDXEeR_0vViL3Wwqg8VyFzvU26g")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22281455"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dc3bf5521f4cd885f20e1fdd6aadd0ba")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002341804786"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7263364323"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://nico_music_bot:ahmed3434@cluster01.rnm5fc4.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = os.environ.get("DATABASE_NAME", "yamato_flux_bot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "inshorturl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "b83fdd727060c59a43b9b9b063dcee500190de3d")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 21600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/+OZTI8EghvmxmMTll")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002298045629"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Kᴏɴɴɪᴄʜɪᴡᴀ!! {mention}⚡,\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Adult_Flux'>𝐀ᴅᴜʟᴛ 𝐅ʟᴜx</a></b>")
try:
    ADMINS=[7263364323]
    for x in (os.environ.get("ADMINS", "1683225887 5961139833 7162615398 7263364323").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝐊ᴏɴɴɪᴄʜɪᴡᴀ {mention}❤️,\n\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ • ᴛʀʏ ᴀɢᴀɪɴ • ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Adult_Flux'>𝐀ᴅᴜʟᴛ 𝐅ʟᴜx</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Dᴏɴ'ᴛ sᴇɴᴅ ᴍᴇ ᴍᴇssᴀɢᴇs ᴅɪʀᴇᴄᴛʟʏ I ᴀᴍ ᴏɴʟʏ Wᴏʀᴋ Fᴏʀ @Adult_Flux ..."

ADMINS.append(OWNER_ID)
ADMINS.append(7263364323)

LOG_FILE_NAME = "sanjisamatokenbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
