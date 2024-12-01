from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Umumiy Ma'lumot  📰")
        ],
        [
            KeyboardButton("Afzalliklar  📌")
        ],
        [
            KeyboardButton("Ijtimoiy tarmoqlarimiz 🌍")
        ],
        [
            KeyboardButton("Back  ↩️")
        ]
    ],
    resize_keyboard=True
)