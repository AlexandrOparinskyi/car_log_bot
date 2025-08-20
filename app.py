import asyncio
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


async def main() -> None:
    config: Config = get_config()
    translator_hub: TranslatorHub = create_translator_hub()

    await asyncio.gather(bot(
        config.tg_bot.token,
        translator_hub
    ))


asyncio.run(main())
