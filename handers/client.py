from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher, executor
from config import dp, bot
from keyboard import keyboard
from data_base import sqlite_db
from parser_site import show_anime


async def hello(message: types.Message,):
    await bot.send_message(message.chat.id,f"Hello my master:{message.from_user.full_name}",
                           reply_markup=keyboard.keyboard_stat)


async def show(message: types.Message):
    data = show_anime.parser()
    for i in data:
        await bot.send_message(message.chat.id, i, reply_markup=keyboard.keyboard_stat)


def say (message:types.Message):
    if message.text.lower() == 'how are you':
        bot.send_message(message.chat.id, 'i am fine and you?')


async def delete_clients(message: types.Message):
    await sqlite_db.sql_command_delete(message)


async def jokes(message: types.Message):
    jokes = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Далее", callback_data="jokes")
    jokes.add(button)
    photo = open("media\images (1).jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo, reply_markup=jokes)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующий",
                                         callback_data="button_call_1",
                                         )
    markup.add(button_call_1)
    question1 = 'Каков правильный синтаксис для вывода "Привет Мир" в Python?'
    answer1 = ['echo("Привет Мир");', 'echo"Привет Мир"', 'p("Привет Мир")', 'print("Привет Мир")']
    await bot.send_poll(message.chat.id,
                        question=question1,
                        options=answer1,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        explanation='output function',
                        reply_markup=markup)


async def talk(message: types.Message):

    buttons = InlineKeyboardMarkup()
    button_yes_1 = InlineKeyboardButton("Да", callback_data="button_yes_1")
    button_no_1 = InlineKeyboardButton("Нет", callback_data="button_no_1")
    buttons.add(button_yes_1, button_no_1)
    await bot.send_message(message.chat.id, f"Привет меня зовут GeekNur, вам удобно говорить?", reply_markup=buttons)


async def send_emoji(message: types.Message):
    if message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")

    # await bot.send_message(message.chat.id, data)


def dp_register_client(dp: Dispatcher):
    dp.register_message_handler(show, commands=['anime'])
    dp.register_message_handler(jokes, commands=['jokes'])
    dp.register_message_handler(talk, commands=['talk'])
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_emoji, content_types=['text'])

