from typing import Dict

from fluentogram import TranslatorHub


def get_service_work_edit_text(i18n: TranslatorHub,
                               data: Dict[str, str]) -> str:
    text =i18n.service.edit.error.param.text()
    service_work_param = data.get("service_work_param")

    if service_work_param == "name":
        text = i18n.service.work.edit.name.text()
    if service_work_param == "price":
        text = i18n.service.work.edit.price.text()
    if service_work_param == "description":
        text = i18n.service.work.edit.description.text()

    return text
