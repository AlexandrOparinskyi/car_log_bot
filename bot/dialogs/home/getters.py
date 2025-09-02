from typing import Dict

from aiogram.types import User
from fluentogram import TranslatorHub

from bot.utils import get_user_by_id


async def getter_home(i18n: TranslatorHub,
                      event_from_user: User,
                      **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    refuel_count = len(user.refuel_records)
    cost_count = user.get_total_cost

    return {"home_text": i18n.home.text(username=user.first_name,
                                        car_count=len(user.cars),
                                        refuel_count=refuel_count,
                                        cost_count=cost_count),
            "add_record_button": i18n.add.record.button(),
            "garage_button": i18n.garage.button(),
            "lk_button": i18n.lk.button(),
            "instructions_button": i18n.instructions.button(),
            "reviews_button": i18n.reviews.button(),
            "support_project_button": i18n.support.project.button(),
            "write_developer_button": i18n.write.developer.button()}


async def getter_write_developer(i18n: TranslatorHub,
                                 **kwargs) -> Dict[str, str]:
    return {"write_developer_text": i18n.write.developer.text(),
            "developer_button": i18n.developer.button(),
            "developer_url": i18n.developer.url(),
            "home_button": i18n.home.button(),}


async def getter_select_record(i18n: TranslatorHub,
                               **kwargs) -> Dict[str, str]:
    return {"add_record_text": i18n.add.record.text(),
            "refuel_button": i18n.refuel.button(),
            "service_button": i18n.service.button(),
            "purchase_button": i18n.purchase.button(),
            "other_record_button": i18n.other.record.button(),
            "home_button": i18n.home.button()}
