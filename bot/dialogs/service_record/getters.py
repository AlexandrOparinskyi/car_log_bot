from typing import Dict

from fluentogram import TranslatorHub

from utils import get_buttons_for_select_service_type


async def getter_select_type(i18n: TranslatorHub,
                             **kwargs) -> Dict[str, str]:
    buttons = get_buttons_for_select_service_type()

    return {"select_service_type_text": i18n.select.service.type.text(),
            "back_button": i18n.back.button(),
            "home_button": i18n.home.button(),
            "buttons": buttons}
