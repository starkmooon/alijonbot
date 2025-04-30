import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncpg

from data.config import ADMINS
from loader import dp, userdb, bot, kinodb


#botdagi foydalanuvchilar soni
@dp.message_handler(commands="count")
async def count_users(message:types.Message):
    user_count=await userdb.count_users()
    msg=f"botdagi jami foydalanuvchilar soni\n"
    msg+=f"{user_count} ta\n"
    await bot.send_message(ADMINS[0],msg)

@dp.message_handler(commands="soni")
async def barcha_users(message:types.Message):
    kino_barcha=await kinodb.count_all_kinos()
    msg=f"botdagi jami kinolar soni\n"
    msg+=f"{kino_barcha} ta\n"
    await bot.send_message(ADMINS[0],msg)


@dp.message_handler(commands="reklama")
async def reklama_function(message:types.Message):
    users=await userdb.select_all_users()
    for user in users:
        await bot.send_message(user['telegram_id'],"bu reklama")


