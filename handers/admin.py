from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import dp, bot
from aiogram.dispatcher.filters import Text
from keyboard import keyboard
from data_base import sqlite_db
from keyboard import admin_panel

ID = None


class FSMAdmin(StatesGroup):
    id = State()
    photo = State()
    username = State()
    lastname = State()


async def make_changes_command(message: types.Message):
    # global ID
    # ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо???', reply_markup=admin_panel.button_case_admin)
    await message.delete()


async def cm_start(message: types.Message):
    # if message.from_user.id == ID:
        await FSMAdmin.id.set()
        await message.reply('Введи свой id')



async def load_id(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        async with state.proxy()as data:
            data['id'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введи фото')


async def load_photo(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        async with state.proxy() as data:
             data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь свое имя')


async def load_username(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        async with state.proxy() as data:
            data['username'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введи свою фамилию')


async def load_lastname(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        async with state.proxy() as data:
            data['lastname'] = message.text
        await sqlite_db.sql_add_command(state)
        await state.finish()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Done')


def dp_register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*" )
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cm_start, commands='Загрузить', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_username, state=FSMAdmin.username)
    dp.register_message_handler(load_lastname, state=FSMAdmin.lastname)
