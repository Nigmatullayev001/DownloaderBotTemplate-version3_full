from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def save_del():
    button = InlineKeyboardButton(text="💾 Saqlash", callback_data="save")
    button2 = InlineKeyboardButton(text="❌ O'chirish", callback_data="delete")
    ikm = InlineKeyboardMarkup(inline_keyboard=[
        [button, button2]
    ])
    return ikm


def saved():
    button = InlineKeyboardButton(text="✅ Saqlandi", callback_data="unsave")
    button2 = InlineKeyboardButton(text="❌ O'chirish", callback_data="delete")
    ikm = InlineKeyboardMarkup(inline_keyboard=[
        [button, button2]
    ])
    return ikm
