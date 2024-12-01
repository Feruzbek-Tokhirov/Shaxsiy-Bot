from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

courses_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Foundation 🎯')
        ],
        [
            KeyboardButton('Professional 🤓')
        ],
        [
            KeyboardButton('Kids 👦')
        ],
        [
            KeyboardButton('Kerakli noutbuk 💻')
        ],
        [
            KeyboardButton('Back  ↩️')
        ]
    ],
    resize_keyboard=True
)

foundation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Java'),
            KeyboardButton('Python')
        ],
        [
            KeyboardButton('Back ⬅️')
        ]
    ],
    resize_keyboard=True
)


professional_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Java Backend'),
            KeyboardButton('Python Backend')
        ],
        [
            KeyboardButton('Android+Flutter')
        ],
        [
            KeyboardButton('Data Scince')
        ],
        [
            KeyboardButton('Back  ↩️')
        ]
    ],
    resize_keyboard=True
)


