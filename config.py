import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_USERNAME = getenv("OWNER_USERNAME","TG_PROFESS0R")
BOT_USERNAME = getenv("BOT_USERNAME" , "Spottfy_music_bot")
BOT_NAME = getenv("BOT_NAME" , "Spottfy_music_bot")
ASSUSERNAME = getenv("ASSUSERNAME" , "spottfymusic")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1002428511388))
OWNER_ID = int(getenv("OWNER_ID", 7861988028))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/sachin07638/Sanatanimusic",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://t.me/TG_PROFESS0R)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MUSIC_BOT_UPDATE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MUSIC_BOT_UPDATE")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "Flase")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://envs.sh/o5Y.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
STATS_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/o5Y.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
STREAM_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/57c384454b0072158a6c9-6d9834426000470fcf.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
