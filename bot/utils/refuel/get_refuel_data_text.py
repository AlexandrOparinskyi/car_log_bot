from typing import Dict

from fluentogram import TranslatorHub


def get_refuel_data(i18n: TranslatorHub,
                    data: Dict[str, str],):
    text = f"\n"

    if data.get("total_price"):
        text += data.get("total_price\n")
