from aiogram import executor
from handers import callback, client, more, admin,inline
from config import dp,URL, bot
from data_base import sqlite_db
from decouple import config


async def on_startup(_):
    await bot.set_webhook(URL)
    print('Бот вышел онлайн')
    sqlite_db.sql_create()


async def on_shutdown(dp):
    await bot.delete_webhook()

admin.dp_register_handlers_admin(dp)
client.dp_register_client(dp)
callback.register_query_handler_callback(dp)
inline.register_handlers_inline(dp)
more.register_handler_more(dp)


if __name__ == '__main__':
    # executor.start_polling(dp, skip_updates=False, on_startup = on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=int(config("PORT", default=5000)),
    )

# Некоторое изменение
#dss
#dsfsd





