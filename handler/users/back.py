from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboard.default.main_keyboard import main_keyboard

router = Router()  # Use Router() instead of dp


@router.message(F.text == "Back🔙")
async def go_back(message: Message, state: FSMContext):
    await message.answer("Ortga 🔙", reply_markup=main_keyboard())
    await state.clear()  # Clear FSM state if any
