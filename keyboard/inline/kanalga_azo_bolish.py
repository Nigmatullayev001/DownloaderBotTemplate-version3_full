from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import CHANNEL_USERNAME


def subscribe_ikm():
    button = InlineKeyboardButton(text="Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME.strip('@')}")
    button2 = InlineKeyboardButton(text="Tekshirsh☑️", callback_data="tekshirsh")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button],
            [button2]
        ])

    return ikm
