from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

URL = "https://geeknur.herokuapp.com/"
URI = "postgres://jukaygyuhjtoyz:8805929fd84ff048a1ffcb6d6361fe9b5b3ae4829b62e37a8737917449f1cc9d@ec2-3-248-121-12.eu-west-1.compute.amazonaws.com:5432/dl0aam2ienc1t"