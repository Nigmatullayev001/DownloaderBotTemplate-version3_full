from aiogram import Router, types, F
from handler.users.start import check_subscription
from keyboard.inline.kanalga_azo_bolish import subscribe_ikm

router = Router()  # Use Router instead of `dp`


@router.callback_query(F.data == "tekshirsh")
async def check_subscription_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_subscribed = await check_subscription(callback_query.bot, user_id)

    if is_subscribed:
        await callback_query.message.answer("✅ Obuna tasdiqlandi! Endi botdan foydalanishingiz mumkin.")
    else:
        await callback_query.message.answer(
            "❌ Siz hali obuna bo'lmagansiz. Iltimos, obuna bo'ling va qayta tekshirishni bosing.",
            reply_markup=subscribe_ikm()
        )

    await callback_query.answer()  # Callbackni yopish uchun
