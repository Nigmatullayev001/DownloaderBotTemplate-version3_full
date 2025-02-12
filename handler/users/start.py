from aiogram import Bot, Router, types
from aiogram.filters import CommandStart

from data.config import CHANNEL_USERNAME
from keyboard.default.main_keyboard import main_keyboard
from keyboard.inline.kanalga_azo_bolish import subscribe_ikm

router = Router()  # Router yaratildi


async def check_subscription(bot: Bot, user_id: int) -> bool:
    """Foydalanuvchining kanalga a'zo bo'lganligini tekshiradi"""
    member = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
    return member.status in ["member", "administrator", "creator"]


@router.message(CommandStart())  # Aiogram 3.x uchun to'g'ri yozilishi
async def bot_start(message: types.Message, bot: Bot):
    """Botni ishga tushirganda ishlaydi"""
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=main_keyboard())

    user_id = message.from_user.id
    is_subscribed = await check_subscription(bot, user_id)

    if is_subscribed:
        await message.reply("Botdan foydalanishingiz mumkin!")
    else:
        await message.reply(
            "Botdan foydalanish uchun avval kanalimizga obuna bo'ling:",
            reply_markup=subscribe_ikm()
        )
