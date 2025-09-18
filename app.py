import asyncio
import json
import locale
import logging
from datetime import datetime, date
from typing import Any

from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from fluentogram import TranslatorHub
from redis.asyncio import Redis
from sqlalchemy.util import await_only

from I18N import create_translator_hub
from bot import bot
from config import Config, get_config
from database import Car
from utils import get_car_by_id

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


def custom_json_dumps(obj: Any) -> str:
    """Кастомная сериализация с поддержкой datetime"""

    def default_encoder(o):
        if isinstance(o, (datetime, date)):
            return {'__type__': 'datetime', 'value': o.strftime("%d.%m.%Y")}
        if isinstance(o, Car):
            return {'__type__': 'car', 'value': o.id}
        return str(o)

    return json.dumps(obj, default=default_encoder, ensure_ascii=False)


async def custom_json_loads(data: str) -> Any:
    """Кастомная десериализация с восстановлением datetime"""

    async def object_hook(obj):
        if '__type__' in obj and obj['__type__'] == 'datetime':
            return datetime.strptime(obj.get("value"), "%d.%m.%Y")
        if '__type__' in obj and obj['__type__'] == 'car':
            car = await get_car_by_id(int(obj["value"]))
            return car
        return obj

    result = json.loads(data, object_hook=object_hook)
    return result if isinstance(result, dict) else {}


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

    redis_client = Redis(
        host=config.redis.host,
        port=config.redis.port,
        db=config.redis.db,
        decode_responses=False
    )
    storage = RedisStorage(
        redis_client,
        key_builder=DefaultKeyBuilder(with_destiny=True, prefix='bot_fsm'),
        json_dumps=custom_json_dumps,
        json_loads=custom_json_loads
    )

    await asyncio.gather(bot(
        config.tg_bot.token,
        translator_hub,
        logger
    ))


asyncio.run(main())
