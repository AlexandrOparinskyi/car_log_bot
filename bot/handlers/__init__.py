from aiogram import Router

from .user import user_router


def register_routers(router: Router) -> None:
    router.include_router(user_router)
