import os

import django
from aiogram import executor

# from database import create_db
from config import admin_id
from load_all import bot


async def on_startup(dp):
    # await create_db()
    await bot.send_message(admin_id, 'Доброго часу доби!')


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "django_project.telegrambot.telegrambot.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


if __name__ == "__main__":
    setup_django()
    from aiogram import executor
    from hendlers import dp

    executor.start_polling(dp, on_startup=on_startup)
