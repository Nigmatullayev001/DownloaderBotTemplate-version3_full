from aiogram import Router, types, F
from utils.dp_api.db import Database
from utils.tiktok import download_tiktok_video  # TikTok video yuklab olish
from utils.notify_admins import on_error_notify

router = Router()  # Use Router instead of `dp`
db = Database()


@router.message(F.text.contains("tiktok.com"))
async def handle_tiktok_url(message: types.Message):
    video_url = message.text.strip()

    await message.reply("📥 Video yuklanmoqda... Iltimos, kuting.")

    # Video yuklab olish
    try:
        video_download_url = download_tiktok_video(video_url)

        if video_download_url:
            db.tiktok_add_url('title_tiktok', video_download_url)
            await message.reply_video(video_download_url)
        else:
            await message.reply("❌ Videoni yuklab bo‘lmadi. Iltimos, boshqa link yuboring.")

    except Exception as e:
        await message.reply("❌ Videoni yuklab olishda xatolik yuz berdi.")
        await on_error_notify(message.bot, f"⚠️ TikTok yuklashda xatolik: {str(e)}")
