from aiogram import Router, types, F

router = Router()  # Use Router instead of `dp`


@router.message(F.text == "✍️ Qo'llanma")
async def bot_help_for_structure(message: types.Message):
    text = (
        "📌 *@YourBot_username* quyidagilarni yuklab beradi:\n\n"
        "✅ *Instagram* - Post, Stories, Reels\n"
        "✅ *YouTube* - Video, Shorts, Audio\n"
        "✅ *TikTok* - Suv belgisiz video\n"
        "✅ *Facebook* - Reels, Rasm\n"
        "✅ *Pinterest* - Rasm, Video\n"
        "✅ *Snapchat* - Rasm, Video\n\n"
        "🛠 *Bot guruhda ham ishlaydi!* Uni guruhga qo‘shib qo‘ysangiz bo‘ldi, "
        "admin qilish ham shart emas. Bot yuborilgan linklarni avtomatik yuklab beradi. 📥"
    )

    await message.answer(text, parse_mode="Markdown")
