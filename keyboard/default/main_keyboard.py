from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    button1 = KeyboardButton(text="✍️ Qo'llanma")
    button2 = KeyboardButton(text="📁 Saqlanganlar")
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [button1],
        [button2]
    ])
    return rkm
