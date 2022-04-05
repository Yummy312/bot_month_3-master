import sqlite3 as sq
from config import bot


def sql_create():
    global db, cursor
    db = sq.connect("client.sqlite3")
    cursor = db.cursor()
    if db:
        print("Database connected successfully")
    db.execute("CREATE TABLE IF NOT EXISTS users "
               "(id text , img text, username primary key , lastname text)")
    db.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cursor.execute('insert into users values(?,?,?,?)', tuple(data.values()))
        db.commit()


async def sql_casual_select():
    return cursor.execute('SELECT * FROM users').fetchall()


async def sql_command_delete(data):
    cursor.execute("DELETE FROM users WHERE id == ?", (data,))
    db.commit()


