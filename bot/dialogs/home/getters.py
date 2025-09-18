from typing import Dict

from aiogram.types import User
from fluentogram import TranslatorHub

from bot.utils import (get_user_by_id,
                       get_current_date,
                       get_three_latest_records)



async def getter_home(i18n: TranslatorHub,
                      event_from_user: User,
                      **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    refuel_count = len(user.refuel_records)
    cost_count = round(user.get_total_cost, 2)
    current_date = get_current_date(user.created_at)
    list_record = get_three_latest_records(user.get_all_records)


    return {"home_text": i18n.home.text(username=user.first_name,
                                        car_count=len(user.count_car),
                                        refuel_count=refuel_count,
                                        cost_count=cost_count,
                                        current_date=current_date,
                                        records=len(user.get_all_records),
                                        list_record=list_record,),
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
            "home_button": i18n.home.button()}


async def getter_select_record(i18n: TranslatorHub,
                               **kwargs) -> Dict[str, str]:
    return {"add_record_text": i18n.add.record.text(),
            "refuel_button": i18n.refuel.button(),
            "service_button": i18n.service.button(),
            "purchase_button": i18n.purchase.button(),
            "other_record_button": i18n.other.record.button(),
            "home_button": i18n.home.button()}
