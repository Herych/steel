from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Каталог продукції'),
            KeyboardButton(text='Відеоінструкції 🎦')
        ],
    ],
    resize_keyboard=True
)
