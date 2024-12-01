from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3
from data.config import ADMINS
from keyboards.default.startKeyboard import start_keyboard
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id, name=name)

    except sqlite3.IntegrityError as err:
        # await bot.send_message(chat_id=ADMINS[0],  text=err)
        pass
    photo = open('static/img/start.jpg', 'rb')
    text = "🏢  Akademiyamiz haqida ko'proq ma'lumotlarni bilish uchun quyidagi bo'limlardan birini tanlang  ⬇️"
    await message.answer_photo(photo=photo, caption=text, reply_markup=start_keyboard)
    count = db.count_users()[0]
    # Adminga habar beramiz
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} tafoydalanuvchi bor!!!"
    await bot.send_message(chat_id=ADMINS[0], text=msg)
