from aiogram import types

from main import dp


# Echo bot
@dp.message(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
