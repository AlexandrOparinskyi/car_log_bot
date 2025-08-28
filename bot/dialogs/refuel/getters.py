from typing import Dict

from fluentogram import TranslatorHub


async def getter_total_price(i18n: TranslatorHub,
                             **kwargs) -> Dict[str, str]:
    return {"total_price_text": i18n.total.price.text()}