from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types import CallbackQuery, Message

from db_commands import add_user, get_item, select_user
from kayboards.menu_keyboards import menu_cd, categories_keyboard, subcategories_keyboard, items_keyboard, item_keyboard
from load_all import dp, bot

from kayboards import start_menu


@dp.message_handler(CommandStart())
async def register_user(message: types.Message):
    user = await select_user(message.from_user.id)
    if not user:
        await add_user(user_id=message.from_user.id,
                       full_name=message.from_user.full_name,
                       username=message.from_user.username)

    await message.answer(
        f'Привіт {message.from_user.first_name}, '
        f'інженерами компанії STEEL були сконструйовані дульні пристрої з унікальними'
        ' і екстремальними характеристиками, вони повністю відповідають найвищим вимогам по гасінню'
        ' звуку, пострілу. Повністю прибирають спалах, підтримують автоматичний режим стрільби.',
        reply_markup=start_menu)


@dp.message_handler(text='Відеоінструкції 🎦')
async def show_menu(message: types.Message):
    await list_categories(message)


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    markup = await categories_keyboard()

    if isinstance(message, Message):
        await message.answer("Інструкції та відеоматеріали: ", reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)

    # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
    await callback.message.edit_reply_markup(markup)


async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)

    # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
    await callback.message.edit_text(text="Інструкції та відеоматеріали: ", reply_markup=markup)


async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    # markup = item_keyboard(category, subcategory)

    # Берем запись о нашем товаре из базы данных
    item = await get_item(item_id)
    # text = f"{item.name}"
    await callback.message.answer_video(video=item.video, caption=item.description)
    # await callback.message.edit_text(text='[eqyz', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """

    # Получаем текущий уровень меню, который запросил пользователь
    current_level = callback_data.get("level")

    # Получаем категорию, которую выбрал пользователь (Передается всегда)
    category = callback_data.get("category")

    # Получаем подкатегорию, которую выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    subcategory = callback_data.get("subcategory")

    # Получаем айди товара, который выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    item_id = int(callback_data.get("item_id"))

    # Прописываем "уровни" в которых будут отправляться новые кнопки пользователю
    levels = {
        "0": list_categories,  # Отдаем категории
        "1": list_subcategories,  # Отдаем подкатегории
        "2": list_items,  # Отдаем товары
        "3": show_item,

    }

    # Забираем нужную функцию для выбранного уровня
    current_level_function = levels[current_level]

    # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
    await current_level_function(
        call,
        category=category,
        subcategory=subcategory,
        item_id=item_id
    )
    await bot.answer_callback_query(callback_query_id=call.id)


@dp.message_handler(text='Каталог продукції')
async def catalog(message: types.Message):
    await message.answer(f"З каталогом продукції компанії STEEL можна ознайомитися перейшовши за посиланням: \n"
                         f"https://silent-steel.in.ua/collections/all")


#
# @dp.message_handler(text='Відеоінструкції 🎦')
# async def video_instruction(message: types.Message):
#     await message.answer('Відеоінструкці:', reply_markup=choice_video_instruction)
#
#
# @dp.message_handler(text='Назад 🔙')
# async def return_to(message: types.Message):
#     await message.delete()
#     await message.answer(f"Для роботи з ботом, скористайтеся меню:", reply_markup=start_menu)
#
#
@dp.message_handler(content_types=types.ContentType.VIDEO)
async def echo(message: types.Message):
    await message.answer(message.video.file_id)
