import logging
from aiogram import Bot
from data.config import ADMINS


async def on_startup_notify(bot: Bot):
    """Bot ishga tushganda administratorlarga xabar yuboradi"""
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)


async def on_error_notify(bot: Bot, er):
    """Xatolik yuz berganda administratorlarga xabar yuboradi"""
    for admin in ADMINS:
        try:
            await bot.send_message(admin, f"Xatolik yuz berdi:\n{er}")
        except Exception as err:
            logging.exception(err)
