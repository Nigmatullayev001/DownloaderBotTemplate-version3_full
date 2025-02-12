from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def mp4_or_mp3_ikm():
    button = InlineKeyboardButton(text="MP3 🎵", callback_data="mp3")
    button2 = InlineKeyboardButton(text="MP4 📹", callback_data="mp4")
    ikm = InlineKeyboardMarkup(inline_keyboard=[
        [button, button2]
    ])
    return ikm


def vid_or_aud_ikm():
    button = InlineKeyboardButton(text="Audio 🎵", callback_data="aud")
    button2 = InlineKeyboardButton(text="Video 📹", callback_data="vid")

    ikm = InlineKeyboardMarkup(inline_keyboard=[
        [button, button2]
    ])
    return ikm

# def mp4_or_mp3_ikm_for_insta():
#     ikm = InlineKeyboardMarkup()
#     button = InlineKeyboardButton(text="MP3 🎵", callback_data="mp3_insta")
#     button2 = InlineKeyboardButton(text="MP4 📹", callback_data="mp4_insta")
#     ikm.row(button, button2)
#     return ikm
