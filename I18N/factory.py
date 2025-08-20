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
                               f'{DIR_PATH}/ru/LC_MESSAGES/car.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/user.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/home.ftl']),
            ),
            FluentTranslator(
                locale='en',
                translator=FluentBundle.from_files(
                    locale='en',
                    filenames=[f'{DIR_PATH}/en/LC_MESSAGES/general.ftl',
                               f'{DIR_PATH}/ru/LC_MESSAGES/start.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/car.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/user.ftl',
                               f'{DIR_PATH}/en/LC_MESSAGES/home.ftl']),
            ),
        ],
        root_locale='en',
    )
