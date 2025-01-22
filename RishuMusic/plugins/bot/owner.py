from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - ʀᴀᴅʜᴇ 
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ᴘʀɪɴᴄᴇ 
│├─────────────────╯
├┼─────────────────⦿
├┤~ @ll_BOTCHAMBER_ll
├┤~ @DP_WORLD7
├┤~ @RADHE_XD
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @ll_RADHE7_ll
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Ｒ ᴀ ᴅ ʜ ᴇ ", url=f"https://t.me/ll_RADHE7_ll")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/ll_RADHE7_ll"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://github.com/RishuBot/RishuManagement"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/ll_BOTCHAMBER_ll"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/sanataniimusicbot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/v2F.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
