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
        if fb[1] == message.from_user.id:
            if fb[3].startswith("http"):
                await message.bot.send_video(fb[1], fb[3], reply_markup=main_keyboard())  # Facebookdan video yuborish
            else:
                await message.answer("Facebook video URL noto'g'ri.", reply_markup=main_keyboard())
        else:
            await message.answer('Siz hali video saqlamagansiz!')

# 📌 Instagram
@router.message(F.text == "Instagram")
async def handle_instagram(message: Message):
    is_all = db.instagram_all_urls()
    media_groups = []
    for inst in is_all:
        if inst[1] == message.from_user.id:
            if inst[3].startswith("http"):
                if inst[2] == "carousel":
                    media_groups.append(
                        types.InputMediaPhoto(media=inst[3], caption=f"📸 {inst[0]}")
                    )
                    if media_groups:
                        await message.bot.send_media_group(inst[1], media_groups)

                elif 'png' in inst[3]:
                    await message.bot.send_photo(inst[1], photo=inst[3])
                else:
                    await message.bot.send_video(inst[1], video=inst[3])

                # await message.bot.send_video(inst[1], inst[3], reply_markup=main_keyboard())  # Instagramdan video yuborish
            else:
                await message.answer("Instagram video URL noto'g'ri.", reply_markup=main_keyboard())
        else:
            await message.answer('Siz hali Video Saqlamagansiz')

# 📌 TikTok
@router.message(F.text == "TikTok")
async def handle_tiktok(message: Message):
    tt_all = db.tiktok_all_urls()
    for tt in tt_all:
        if tt[1] == message.from_user.id:
            if tt[3].startswith("http"):
                await message.bot.send_video(tt[1], tt[3], reply_markup=main_keyboard())  # TikTokdan video yuborish
            else:
                await message.answer("TikTok video URL noto'g'ri.", reply_markup=main_keyboard())
        else:
            await message.answer('Hali siz Video saqlamagansiz')


# 📌 Pinterest
@router.message(F.text == "Pinterest")
async def handle_pinterest(message: Message):
    pin_all = db.pinterest_all_urls()
    for pin in pin_all:
        if pin[1] == message.from_user.id:
            if pin[3].endswith(".mp4"):
                await message.bot.send_video(pin[1], pin[3], reply_markup=main_keyboard())
            elif pin[3].endswith(".jpg"):
                await message.bot.send_photo(pin[1], pin[3], reply_markup=main_keyboard())
        else:
            await message.answer("Siz hali Video yuklab olmagansiz!")


# 📌 Pinterest
@router.message(F.text == "Snapchat")
async def handle_pinterest(message: Message):
    snap_all = db.snapchat_all_urls()
    for snap in snap_all:
        if snap[1] == message.from_user.id:
            if snap[3].endswith(".mp4"):
                await message.bot.send_video(snap[1], snap[3], reply_markup=main_keyboard())
            elif snap[3].endswith(".jpg"):
                await message.bot.send_photo(snap[1], snap[3], reply_markup=main_keyboard())
        else:
            await message.answer("Siz hali MEDIA saqlamagansiz! Media yuklab olish uchun link yuboring!")


# 🎬 YouTube - Video Tanlash
@router.callback_query(F.data == "vid")
async def handle_video(callback_query: CallbackQuery):
    yt_all = db.youtube_all_urls()
    await callback_query.message.delete()

    found = False
    for yt in yt_all:
        if yt[1] == callback_query.from_user.id:
            if yt[2].endswith("#video") and yt[3].startswith("http"):
                if yt[1] == callback_query.from_user.id:
                    await callback_query.message.bot.send_video(yt[1], yt[3], reply_markup=main_keyboard())
                    found = True
        else:
            await callback_query.message.answer('Hali siz Video saqlamagansiz!')

    if not found:
        await callback_query.message.answer("Video topilmadi.", reply_markup=main_keyboard())


# 🎵 YouTube - Audio Tanlash
@router.callback_query(F.data == "aud")
async def handle_audio(callback_query: CallbackQuery):
    yt_all = db.youtube_all_urls()
    await callback_query.message.delete()

    found = False
    for yt in yt_all:
        if yt[1] == callback_query.from_user.id:
            audio_url = yt[3]
            # Check if the URL is valid and if the format ends with .mp3 or other acceptable audio types
            if "#audio" in yt[2] and audio_url.startswith("http"):
                # audio_url.endswith(".mp3") or audio_url.endswith(".m4a")):
                try:
                    # Send the audio file
                    await callback_query.message.bot.send_audio(
                        chat_id=yt[1],  # The chat ID where to send the audio
                        audio=audio_url,  # Direct URL to the audio file
                        caption=f"Bu audio @instagram_youtbe_downloaders_bot orqali yuklab olindi!",  # Optional caption
                        title=f'{yt[2]}',
                        reply_markup=main_keyboard()  # Optional reply markup
                    )
                    found = True
                except Exception as e:
                    print(f"Error sending audio: {e}")
                    await callback_query.message.answer("Ishlatishda xato yuz berdi. Iltimos, qayta urinib ko'ring.",
                                                        reply_markup=main_keyboard())
                    # break  # Stop the loop if an error occurs
        else:
            await callback_query.message.answer("Hali siz Video saqlamagansiz!")

    if not found:
        await callback_query.message.answer("Audio topilmadi.", reply_markup=main_keyboard())
