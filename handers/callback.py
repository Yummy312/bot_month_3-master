from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, callback_query
from aiogram import types, Dispatcher
from config import bot


async def answer_yes_1(call: types.callback_query):
    buttons = InlineKeyboardMarkup()
    button_yes_2 = InlineKeyboardButton("Да", callback_data="button_yes_2")
    button_no_2 = InlineKeyboardButton("Нет", callback_data="button_no_2")
    buttons.add(button_yes_2, button_no_2)
    question_1_2 = 'Отлично, вы любите путешествовать?'
    await bot.send_message(call.message.chat.id, question_1_2, reply_markup= buttons)


async def answer_yes_2(call: types.callback_query):
    buttons = InlineKeyboardMarkup()
    button_yes_3 = InlineKeyboardButton("Да", callback_data="button_yes_3")
    button_no_3 = InlineKeyboardButton("Нет", callback_data="button_no_3")
    buttons.add(button_yes_3, button_no_3)
    answer = 'Хорошо, вы часто путешествуете?'
    await bot.send_message(call.message.chat.id, answer,reply_markup=buttons )


async def answer_yes_3(call: types.callback_query):
    buttons = InlineKeyboardMarkup()
    button_yes_4 = InlineKeyboardButton("Да", callback_data="button_yes_4")
    button_no_4 = InlineKeyboardButton("Нет", callback_data="button_no_4")
    buttons.add(button_yes_4, button_no_4)
    answer = 'Это замечательно! Ведь благодаря путешествиям человек познает много нового!'
    await bot.send_message(call.message.chat.id, answer)


async def answer_no(call: types.callback_query):
    answer = 'Хорошо, тогда в следующий раз)'
    await bot.send_message(call.message.chat.id, answer, )


async def answer_no_1(call: types.callback_query):
    answer = 'Понимаю, все люди разные.'
    await bot.send_message(call.message.chat.id, answer, )


async def answer_no_2(call: types.callback_query):
    answer = 'Отлично, все хорошо в меру.'
    await bot.send_message(call.message.chat.id, answer, )


async def jokes1(call: types.callback_query):
    button = InlineKeyboardMarkup()
    button_next_1 = InlineKeyboardButton("Далее", callback_data="jokes_1")
    button.add(button_next_1)
    photo = open("media\mem1-cat.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo, reply_markup=button)


async def jokes2(call: types.callback_query):
    button = InlineKeyboardMarkup()
    button_next_2 = InlineKeyboardButton("Далее", callback_data="jokes_2")
    button.add(button_next_2)
    photo = open("media\developer12.jpeg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo, reply_markup=button)


async def jokes3(call: types.callback_query):
    button = InlineKeyboardMarkup()
    button_next_3 = InlineKeyboardButton("Далее", callback_data="jokes_3")
    button.add(button_next_3)
    photo = open("media\images.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo, reply_markup=button)


async def jokes4(call: types.callback_query):
    button = InlineKeyboardMarkup()
    button_next_4 = InlineKeyboardButton("",callback_data="jokes_4",)
    button.add(button_next_4)
    photo = open("media\poem.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo, reply_markup=button)


async def quiz2(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующий",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question2 = 'Как вы вставляете комментарии в код Python?'
    answer2 = ['#Это комментарий', '/*Это комментарий*/', '//Это комментарий', 'Это комментарий#']
    await bot.send_poll(call.message.chat.id,
                        question= question2,
                        options=answer2,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        explanation='output function',
                        reply_markup=markup)
#
# DD = start-START quiz-QUIZ talk-TALK jokes-JOKES Share location-SHARE LOCATION Share info-SHARE INFO
async def quiz3(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующий",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question3 = 'Какое из них не является законным именем переменной?'
    answer3 = ['_Myvar', 'my-var', 'my_var', '_myvar']
    await bot.send_poll(call.message.chat.id,
                        question=question3,
                        options=answer3,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        explanation='output function',
                        reply_markup=markup)


async def quiz4(call: types.callback_query):
    question4 = 'Дан список list2 =[8, 12, 45, 67, 89, 45]' \
      ' Выберите правильный вариант решения ,чтобы результат был таким: ' \
      'list2 =[8, 12, 45, 67, 89, 45, 8, 12, 45, 67, 89, 45]'
    answer4 = ['for i in list2:list2.append(i)',
               'for list2 in list2:list1.append(list2)', 'for list2.append[list2]',
               'for i in range(len(list2)):list2.append(list2[i])']
    await bot.send_poll(call.message.chat.id,
                        question=question4,
                        options=answer4,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        explanation='output function')


def register_query_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(jokes4, lambda func: func.data == "jokes_3")
    dp.register_callback_query_handler(jokes3, lambda func: func.data == "jokes_2")
    dp.register_callback_query_handler(jokes2, lambda func: func.data == "jokes_1")
    dp.register_callback_query_handler(jokes1, lambda func: func.data == "jokes")
    dp.register_callback_query_handler(answer_no_2, lambda func: func.data == "button_no_3")
    dp.register_callback_query_handler(answer_no_1, lambda func: func.data == "button_no_2")
    dp.register_callback_query_handler(answer_no, lambda func: func.data == "button_no_1")
    dp.register_callback_query_handler(answer_yes_3, lambda func: func.data == "button_yes_3")
    dp.register_callback_query_handler(answer_yes_2, lambda func: func.data == "button_yes_2")
    dp.register_callback_query_handler(answer_yes_1, lambda func: func.data == "button_yes_1")
    dp.register_callback_query_handler(quiz2, lambda func: func.data == "button_call_1")
    dp.register_callback_query_handler(quiz3, lambda func: func.data == "button_call_2")
    dp.register_callback_query_handler(quiz4, lambda func: func.data == "button_call_3")
