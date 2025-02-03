import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from RishuMusic import app
from RishuMusic.core.call import SACHIN, autoend
from RishuMusic.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave():
    if not config.AUTO_LEAVING_ASSISTANT:
        return

    while True:
        await asyncio.sleep(config.AUTO_LEAVE_ASSISTANT_TIME)
        from RishuMusic.core.userbot import assistants

        for num in assistants:
            client = await get_client(num)
            left = 0
            try:
                async for i in client.iter_dialogs():
                    if i.chat.type in ["supergroup", "group", "channel"]:
                        chat_id = i.chat.id
                        if chat_id in {config.LOGGER_ID, -1001919135283, -1001841879487}:
                            continue
                        if left >= 20:
                            break
                        if not await is_active_chat(chat_id):
                            print(f"Leaving chat: {chat_id}")  # Debugging ke liye
                            try:
                                await client.leave_chat(chat_id)
                                left += 1
                            except Exception as e:
                                print(f"Error leaving {chat_id}: {e}")
            except Exception as e:
                print(f"Error fetching dialogs: {e}")



asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await SACHIN.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
