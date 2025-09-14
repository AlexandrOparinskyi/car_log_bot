import locale
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from bot.dialogs import register_dialogs
from bot.handlers import register_routers
from bot.middlewares import TranslatorRunnerMiddleware


async def main(token: str,
               hub: TranslatorHub,
               logger: logging) -> None:
    try:
        locale.setlocale(locale.LC_TIME, 'ru_RU')
        logger.info("Russian locale installed")
    except locale.Error:
        logger.error("Failed to install Russian locale. Default locale is used")

    bot: Bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())

    await bot.set_my_commands(
        commands=[
            BotCommand(
                command='home',
                description="♻️ В главное меню"
            )
        ]
    )

    dp.update.middleware(TranslatorRunnerMiddleware())
    register_routers(dp)
    register_dialogs(dp)
    setup_dialogs(dp)

    await dp.start_polling(bot, _translator_hub=hub)
