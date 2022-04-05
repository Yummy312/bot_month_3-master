from aiogram import types, Dispatcher
from config import bot


async def secret_word(message: types.Message):
    await message.reply("Да мой хозяин")


def register_handler_more(dp:Dispatcher):
    dp.register_message_handler(secret_word, lambda word: word.text.startswith('джарвис'))
