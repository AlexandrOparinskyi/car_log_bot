from typing import Dict

from aiogram.types import User
from fluentogram import TranslatorHub


async def getter_user_home(i18n: TranslatorHub,
                           event_from_user: User,
                           **kwargs) -> Dict[str, str]:
    username = event_from_user.first_name

    return {"user_home_text": i18n.user.home.text(username=username),
            "home_button": i18n.home.button(),
            "connect_premium_button": i18n.connect.premium.button(),
            "invite_friend_button": i18n.invite.friend.button(),
            "user_settings_button": i18n.user.settings.button(),
            "achievements_button": i18n.achievements.button()}


async def getter_invite_friend(i18n: TranslatorHub,
                               event_from_user: User,
                               **kwargs) -> Dict[str, str]:
    link = f"https://t.me/driver_notes_bot?start={event_from_user.id}"

    return {"invite_friend_text": i18n.invite.friend.text(link=link),
            "back_button": i18n.back.button(),
            "home_button": i18n.home.button(),
            "copy_link_button": i18n.copy.link.button()}


async def getter_copy_link(i18n: TranslatorHub,
                           event_from_user: User,
                           **kwargs) -> Dict[str, str]:
    link = (f"<code>https://t.me/driver_notes_bot?start="
            f"{event_from_user.id}</code>")

    return {"copy_link_text": link,
            "copy_text_link_button": i18n.copy.text.link.button()}
