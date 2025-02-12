from aiogram import Router, types, F
from utils.dp_api.db import Database
from handler.users.start import check_subscription
from keyboard.inline.kanalga_azo_bolish import subscribe_ikm
from utils.insta import downloader
from utils.notify_admins import on_error_notify

db = Database()

router = Router()  # Use Router instead of `dp`


@router.message(F.text.startswith(("https://instagram.com/", "https://www.instagram.com/")))
async def instagram_down(message: types.Message):
    user_id = message.from_user.id
    is_subscribed = await check_subscription(message.bot, user_id)

    if not is_subscribed:
        await message.answer(
            "❌ Siz hali obuna bo'lmagansiz. Iltimos, obuna bo'ling va qayta tekshirishni bosing.",
            reply_markup=subscribe_ikm()
        )
        return

    await message.reply("📥 Media yuklanmoqda! 2 soniya kuting...")

    try:
        data = downloader(link=message.text)

        if data == "error":
            await message.answer("❌ Bu linkda hech qanday ma'lumot yo'q")
            return

        if data["type"] == "image":
            await message.answer_photo(photo=data["media"])
            db.instagram_add_url(title="image", url=f"{data['media']} | #image")

        elif data["type"] == "video":
            await message.answer_video(video=data["media"])
            db.instagram_add_url(title="video", url=f"{data['media']} | #video")

        elif data["type"] == "carousel":
            media_groups = []
            for item in data["media"]:
                if isinstance(item, dict):
                    media_url = item.get("media")
                    media_title = item.get("title")
                    media_groups.append(
                        types.InputMediaPhoto(media=media_url, caption=f"📸 {media_title}")
                    )
                    db.instagram_add_url(title="carousel", url=f"{media_url} | #carousel")
                else:
                    await message.answer("❌ Media formati mos kelmadi!")

            if media_groups:
                await message.answer_media_group(media_groups)

        else:
            await message.answer("❌ Qaytarilgan linkda mos keladigan ma'lumot topilmadi.")

    except Exception as e:
        await on_error_notify(message.bot, f"{e}: APIda obuna tugagan!!")
        await message.answer("❌ Uzr, xatolik yuz berdi! Adminlar muammoni ko'rib chiqishadi.")
