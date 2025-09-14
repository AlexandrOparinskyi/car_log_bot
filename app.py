import asyncio
import locale
import logging

from fluentogram import TranslatorHub

from I18N import create_translator_hub
from bot import bot
from config import Config, get_config

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


def setup_russian_locale():
    """Пытаемся установить русскую локаль"""
    locales_to_try = [
        'ru_RU.UTF-8',
        'ru_RU.utf8',
        'ru_RU',
        'Russian_Russia.1251',
        'Russian',
        'C.UTF-8'  # fallback
    ]

    for loc in locales_to_try:
        try:
            locale.setlocale(locale.LC_TIME, loc)
            logger.info("Locales is installed successfully")
            return True
        except locale.Error:
            continue

    logger.error("Locales is not installed")
    return False


async def main() -> None:
    config: Config = get_config()
    translator_hub: TranslatorHub = create_translator_hub()
    setup_russian_locale()

    await asyncio.gather(bot(
        config.tg_bot.token,
        translator_hub,
        logger
    ))


asyncio.run(main())
