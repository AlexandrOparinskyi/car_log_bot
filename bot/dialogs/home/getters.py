from typing import Dict

from aiogram.types import User
from fluentogram import TranslatorHub

from utils import get_user_by_id


async def getter_home(i18n: TranslatorHub,
                      event_from_user: User,
                      **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)

    return {"home_text": i18n.home.text(username=user.first_name,
                                        car_count=len(user.cars)),
            "add_button": i18n.add.button(),
            "garage_button": i18n.garage.button(),
            "lk_button": i18n.lk.button(),
            "instructions_button": i18n.instructions.button(),
            "reviews_button": i18n.reviews.button(),
            "support_project_button": i18n.support.project.button(),
            "write_developer_button": i18n.write.developer.button()}
