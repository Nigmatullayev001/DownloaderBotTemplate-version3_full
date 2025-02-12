from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

router = Router()  # Create a router instead of using `dp`


@router.message(Command("help"))
async def bot_help(message: Message):
    text = (
        "📌 *Buyruqlar:*",
        "/start - Botni ishga tushirish",
        "/help - Yordam"
    )

    await message.answer("\n".join(text), parse_mode="Markdown")
