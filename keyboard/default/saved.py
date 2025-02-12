from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_save_keyboard():
    button1 = KeyboardButton(text="YouTube")
    button2 = KeyboardButton(text="Facebook")
    button3 = KeyboardButton(text="Instagram")
    button4 = KeyboardButton(text="TikTok")
    button5 = KeyboardButton(text="Pinterest")
    button6 = KeyboardButton(text="Snapchat")
    button7 = KeyboardButton(text='Back🔙')

    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              keyboard=[[button1, button2, button3],
                                        [button4, button5, button6],
                                        [button7]])
    return rkm
