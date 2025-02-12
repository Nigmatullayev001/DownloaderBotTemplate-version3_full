from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboard.inline.kanalga_azo_bolish import subscribe_ikm
from keyboard.inline.mp3_mp4 import mp4_or_mp3_ikm
from keyboard.inline.save_delete import save_del, saved
from utils.yt import extract_video_id, fetch_video_details
from utils.dp_api.db import Database
from handler.users.start import check_subscription

router = Router()  # Corrected: Using Router instead of dp
db = Database()


# ✅ YouTube URL Handler
@router.message(F.text.contains("https://youtube.com/") | F.text.contains("https://youtu.be/") | F.text.contains(
    "https://www.youtube.com/"))
async def youtube_downloader(message: types.Message, state: FSMContext):
    print('ichiga kirdi')
    user_id = message.from_user.id
    is_subscribed = await check_subscription(message.bot, user_id)

    if is_subscribed:
        print('obuna tekshirildi')
        await state.update_data(url=message.text)
        await message.answer("🎵 Formatlardan birini tanlang va davom eting:", reply_markup=mp4_or_mp3_ikm())
    else:
        await message.answer("Siz hali obuna bo'lmagansiz. Iltimos, obuna bo'ling va qayta tekshiring.",
                             reply_markup=subscribe_ikm())


# ✅ MP3 Callback Handler
@router.callback_query(F.data == "mp3")
async def handle_mp3_callback(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await callback_query.answer()

    data = await state.get_data()
    url = data.get("url")

    if not url:
        await callback_query.message.answer("Xabar noto‘g‘ri. Iltimos, qaytadan URL yuboring.")
        return

    video_id = extract_video_id(url)
    if not video_id:
        await callback_query.message.answer("Iltimos, to'g'ri YouTube video havolasini yuboring.")
        return

    await callback_query.message.answer("YouTube audioni yuklab olayapman, iltimos kuting...")

    download_url = fetch_video_details(video_id)
    if not download_url or not isinstance(download_url, dict):
        await callback_query.message.answer("Videoni yuklab olishda xatolik yuz berdi.")
        return

    audios = download_url.get("audios", {}).get("items", [{}])[0].get("url")
    title_id = download_url.get("title", "Unknown Title")
    thumbs = download_url.get("thumbnails", [])
    thumb_id = thumbs[0]["url"] if thumbs else None

    if not audios:
        await callback_query.message.answer("Videoning audio fayllari topilmadi.")
        return

    db.youtube_add_url(title=f'{title_id} #audio', url=audios)
    await callback_query.message.answer_audio(
        audio=audios, title=f'{title_id} | #audio', thumb=thumb_id,
        caption="Bu audio @instagram_youtbe_downloaders_bot orqali yuklab olindi!"
    )


# ✅ MP4 Callback Handler
@router.callback_query(F.data == "mp4")
async def handle_mp4_callback(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.delete()

    data = await state.get_data()
    url = data.get("url")

    if not url:
        await callback_query.message.answer("Iltimos, URL havolasini qayta yuboring.")
        return

    video_id = extract_video_id(url)
    if not video_id:
        await callback_query.message.answer("Iltimos, to'g'ri YouTube video havolasini yuboring.")
        return

    await callback_query.message.answer("YouTube videoni yuklab olayapman, iltimos kuting...")

    download_url = fetch_video_details(video_id)
    if not download_url or not isinstance(download_url, dict):
        await callback_query.answer("Videoni yuklab olishda xatolik yuz berdi.", show_alert=True)
        return

    videos = download_url.get("videos", {}).get("items", [])
    downloaded_url = videos[0]["url"] if videos else None
    url_mb = videos[0]["sizeText"] if videos else None
    title_id = download_url.get("title", "Unknown Title")

    if downloaded_url:
        db.youtube_add_url(title=f'{title_id} | #video', url=downloaded_url)
        await callback_query.message.answer_video(
            video=downloaded_url,
            caption=f"Bu video @instagram_youtbe_downloaders_bot orqali yuklab olindi!\n"
                    f"Video hajmi: {url_mb}",
            reply_markup=save_del()
        )
    else:
        await callback_query.answer("Kechirasiz, videoni yuklab olishda xatolik yuz berdi.", show_alert=True)


# ✅ Save Callback Handler
@router.callback_query(F.data == "save")
async def handle_save_callback(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=saved())
    await callback_query.answer("Saqlandi ✅", show_alert=True)


# ✅ Delete Callback Handler
@router.callback_query(F.data == "delete")
async def handle_delete_callback(callback_query: CallbackQuery):
    await callback_query.message.delete(reply_markup=None)  # ✅ Ensure keyboard removal
    await callback_query.answer("O'chirildi", show_alert=True)
