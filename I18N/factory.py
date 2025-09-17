from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub

DIR_PATH = 'I18N/locales'


def create_translator_hub() -> TranslatorHub:
    return TranslatorHub(
        {'ru': ('ru', 'en'), 'en': 'en'},
        [
            FluentTranslator(
                locale='ru',
                translator=FluentBundle.from_files(
                    locale='ru',
                    filenames=[f'{DIR_PATH}/ru/LC_MESSAGES/general.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/start.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/garage.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/refuel.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/user.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/home.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/service.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/purchase.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/instruction.ftl']),
            ),
            FluentTranslator(
                locale='en',
                translator=FluentBundle.from_files(
                    locale='en',
                    filenames=[f'{DIR_PATH}/en/LC_MESSAGES/general.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/start.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/garage.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/refuel.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/user.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/home.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/service.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/purchase.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/instruction.ftl']),
            ),
        ],
        root_locale='en',
    )
