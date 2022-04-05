from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

URL = "https://geekclone.herokuapp.com/"
URI = "postgres://uiussrcamotndg:f8073d1e812ca9572966b4d3407efeda3ca1685565497278834a92e75543b15f@ec2-52-30-67-143.eu-west-1.compute.amazonaws.com:5432/da89dev3296ser"