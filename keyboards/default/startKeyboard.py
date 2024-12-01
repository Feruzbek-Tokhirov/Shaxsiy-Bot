from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Kurslar  💻')
        ],
        [
            KeyboardButton('Biz Haqimizda 📔')
        ]
    ],
    resize_keyboard=True
)
