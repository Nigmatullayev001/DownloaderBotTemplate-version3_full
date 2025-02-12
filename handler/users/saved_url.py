from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from keyboard.default.main_keyboard import main_keyboard
from keyboard.default.saved import main_save_keyboard
from keyboard.inline.mp3_mp4 import mp4_or_mp3_ikm, vid_or_aud_ikm
from utils.dp_api.db import Database

db = Database()

router = Router()  # Use Router instead of `dp`


# 📁 Saqlanganlar
@router.message(F.text == "📁 Saqlanganlar")
async def handle_saved(message: Message):
    await message.answer("Toifani tanlang:", reply_markup=main_save_keyboard())


# 🎥 YouTube
@router.message(F.text == "YouTube")
async def handle_youtube(message: Message):
    yt_all = db.youtube_all_urls()
    await message.answer("Audio | Video", reply_markup=vid_or_aud_ikm())


# 📌 Facebook
@router.message(F.text == "Facebook")
async def handle_facebook(message: Message):
    fb_all = db.facebook_all_urls()
    for fb in fb_all:
        if fb.startswith("http"):
            await message.answer_video(fb, reply_markup=main_keyboard())  # Facebookdan video yuborish
        else:
            await message.answer("Facebook video URL noto'g'ri.", reply_markup=main_keyboard())


# 📌 Instagram
@router.message(F.text == "Instagram")
async def handle_instagram(message: Message):
    is_all = db.instagram_all_urls()
    for inst in is_all:
        if inst.startswith("http"):
            await message.answer_video(inst, reply_markup=main_keyboard())  # Instagramdan video yuborish
        else:
            await message.answer("Instagram video URL noto'g'ri.", reply_markup=main_keyboard())


# 📌 TikTok
@router.message(F.text == "TikTok")
async def handle_tiktok(message: Message):
    tt_all = db.tiktok_all_urls()
    for tt in tt_all:
        if tt.startswith("http"):
            await message.answer_video(tt, reply_markup=main_keyboard())  # TikTokdan video yuborish
        else:
            await message.answer("TikTok video URL noto'g'ri.", reply_markup=main_keyboard())


# 📌 Pinterest
@router.message(F.text == "Pinterest")
async def handle_pinterest(message: Message):
    pin_all = db.pinterest_all_urls()
    for pin in pin_all:
        if pin.startswith("http"):
            await message.answer_video(pin, reply_markup=main_keyboard())  # Pinterestdan video yuborish
        else:
            await message.answer("Pinterest video URL noto'g'ri.", reply_markup=main_keyboard())


# 🎬 YouTube - Video Tanlash
@router.callback_query(F.data == "vid")
async def handle_video(callback_query: CallbackQuery):
    yt_all = db.youtube_all_urls()
    await callback_query.message.delete()

    found = False
    for yt in yt_all:
        if yt[1].endswith("#video") and yt[2].startswith("http"):
            await callback_query.message.answer_video(yt[2], reply_markup=main_keyboard())
            found = True

    if not found:
        await callback_query.message.answer("Video topilmadi.", reply_markup=main_keyboard())


# 🎵 YouTube - Audio Tanlash
@router.callback_query(F.data == "aud")
async def handle_audio(callback_query: CallbackQuery):
    yt_all = db.youtube_all_urls()
    await callback_query.message.delete()

    found = False
    for yt in yt_all:
        if yt[1].endswith("#audio") and yt[2].startswith("http"):
            await callback_query.message.answer(yt[2], reply_markup=main_keyboard())
            found = True

    if not found:
        await callback_query.message.answer("Audio topilmadi.", reply_markup=main_keyboard())
