from states.state import KinoState
from loader import dp, bot, kinodb, userdb
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS

@dp.message_handler(commands="kino_add")
async def kino_add_function(message:types.Message):
    await message.answer("kino yuboring")
    await KinoState.kino.set()


@dp.message_handler(state=KinoState.kino,content_types=types.ContentTypes.VIDEO)
async def kino_add_content(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['file_id']=message.video.file_id
        data['caption']=message.caption or 'Kino'


    await message.answer("Kino uchun kod kiriting")
    await KinoState.kod.set()


@dp.message_handler(state=KinoState.kod,content_types=types.ContentTypes.TEXT)
async def kino_add_kod(message:types.Message,state:FSMContext):
    try:
        post_id=int(message.text)
        async with state.proxy() as data:
            data['post_id']=post_id
            await  kinodb.add_kino(post_id=data['post_id'],
                                   file_id=data['file_id'],
                                   caption=data['caption'])
        await message.answer("Kino muvaffaqiyatli qushildi.")
        await KinoState.states.finish()
    except ValueError:
        await message.answer("Kino uchun kod raqam sifatida kiriting:")

#kinoni topish kod boyicha
@dp.message_handler(lambda message:message.text.isdigit())
async def kino_top(message:types.Message):
    if message.text.isdigit():
        post_id=int(message.text)
        data=await kinodb.get_kino_by_post_id(post_id=post_id)
        if data:
            try:
                kinodb.increment_kino_views(post_id=post_id)
                await bot.send_video(chat_id=message.from_user.id,
                                        video=data['file_id'],
                                        caption=f"{data['caption']}\n\n@kinoowoorldbot")
            except:
                await message.answer("Kino topildi yuborishda hatolig qayta urinib koring")
        else:
            await message.answer("Kino topilmadi")

    else:
        await message.answer("Kino uchun kod raqam sifatida kiriting:")


@dp.message_handler(commands="kino_delete")
async def kino_add_function(message:types.Message):
    id=int(message.text)
    await message.answer("kino kodini yuboring")
    await kinodb.delete_movie(post_id=id)

@dp.message_handler(commands="user_delete")
async def user_add_function(message:types.Message):
    await message.answer("User id kiriting")
    await userdb.delete_user(telegram_id=id)

