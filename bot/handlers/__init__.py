from aiogram import Router

from . import user


def get_routers() -> list[Router]:
    return [
        user.user_router,
    ]
