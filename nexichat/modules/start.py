

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message


from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


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
    "https://telegra.ph/file/416d87dc64c6508736dca.jpg",
    "https://telegra.ph/file/d6701b75d7228128926d1.jpg",
    "https://telegra.ph/file/1d8ac0a1a98ec5ced9124.jpg",
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


#---------------EMOJIOS---------------#

EMOJIOS = [
    "🥰",
    "😘",
    "🥵",
    "🔥",
    "⚡",
    "😍",
    "😚",
    "☺️",
    "🥶",
    "🤭",
]


#---------------EMOJIOS---------------#

@nexichat.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("🥰")
        await asyncio.sleep(0.2)
        await accha.edit("😘")
        await asyncio.sleep(0.2)
        await accha.edit("🥵")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_text(
            text=f"""𝙷𝙴𝙻𝙻𝙾  𝙱𝙰𝙱𝚈 

𝙸𝙰𝙼 𝚂𝙸𝚉𝚄𝙺𝙰 𝙼𝙸𝙽𝙰𝙼𝙾𝚃𝙾 𝙰𝙽 𝙰𝙸 𝙱𝙰𝚂𝙴𝙳 𝙲𝙷𝙰𝚃𝙱𝙾𝚃 𝙸 𝙲𝙰𝙽 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙴𝙴𝙿 𝙰𝙲𝚃𝙸𝚅𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿"""
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("help")
async def help(client: nexichat, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("crepo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@nexichat.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
