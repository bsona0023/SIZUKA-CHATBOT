

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://telegra.ph/file/1d8ac0a1a98ec5ced9124.jpg",
    "https://telegra.ph/file/36213460b3aa6069d763f.jpg",
    "https://telegra.ph/file/416d87dc64c6508736dca.jpg",
    "https://telegra.ph/file/d6701b75d7228128926d1.jpg",
    "https://telegra.ph/file/1d8ac0a1a98ec5ced9124.jpg",
    "https://telegra.ph/file/36213460b3aa6069d763f.jpg",
    "https://telegra.ph/file/416d87dc64c6508736dca.jpg",
    "https://telegra.ph/file/d6701b75d7228128926d1.jpg",
    "https://telegra.ph/file/1d8ac0a1a98ec5ced9124.jpg",
    "https://telegra.ph/file/36213460b3aa6069d763f.jpg",
    "https://telegra.ph/file/416d87dc64c6508736dca.jpg",
    "https://telegra.ph/file/d6701b75d7228128926d1.jpg",
    "https://telegra.ph/file/1d8ac0a1a98ec5ced9124.jpg",
    "https://telegra.ph/file/d6701b75d7228128926d1.jpg",
]


#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@nexichat.on_cmd("ping")
async def ping(_, message: Message):
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{nexichat.name} ᴄʜᴀᴛʙᴏᴛ ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [𝙈𝙍 𝘿𝙀𝙑𝙄𝙇](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
