from aiogram import types
from keyboards.default.courcesKeyboard import courses_keyboard
from loader import dp
from keyboards.inline.contactinline import contact_inline

@dp.message_handler(text='Java')
async def java(message: types.Message):
    photo = open('static/img/foundation.jpg', 'rb')
    text = """
💻  Kursing davomiyligi 4 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

— Java dasturlash tilining boshlang'ich tushunchalari; 
— Java da ma’lumot turlari, o’zgaruvchilar bilan ishlash;
— Axborot texnologiyalari. Kompyuterning texnik va dasturiy ta’minoti;
— Algoritm tushunchasi va turlari;
— Tartiblash algoritmlar;
— Ma'lumotlar strukturasini;
— Funksiya, satr va massivlar bilan ishlashni
— Turli xil telegram-botlarni yaratish;
— Obyektga yo'naltirilgan dasturlashni(OOP) o'rganasiz. 


💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov: 1 000 000  so'm.
    """
    await message.answer_photo(photo=photo, caption=text, reply_markup=contact_inline)


@dp.message_handler(text='Python')
async def python(message: types.Message):
    photo = open('static/img/foundation.jpg', 'rb')
    text = """
💻  Kursing davomiyligi 4 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

— Python dasturlash tilining boshlang'ich tushunchalari; 
— Python da ma’lumot turlari, o’zgaruvchilar bilan ishlash;
— Axborot texnologiyalari. Kompyuterning texnik va dasturiy ta’minoti;
— Algoritm tushunchasi va turlari;
— Tartiblash algoritmlar;
— Ma'lumotlar strukturasini;
— Funksiya, satr va massivlar bilan ishlashni
— Turli xil telegram-botlarni yaratish;
— Obyektga yo'naltirilgan dasturlashni(OOP) o'rganasiz. 

💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov: 1 000 000  so'm.
    """
    await message.answer_photo(photo=photo, caption=text, reply_markup=contact_inline)


@dp.message_handler(text='Back ⬅️')
async def back(message: types.Message):
    await message.answer("Siz kurs sahifasiga o'tdingiz:", reply_markup=courses_keyboard)
