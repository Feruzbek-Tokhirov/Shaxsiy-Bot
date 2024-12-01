from aiogram import types
from keyboards.default.startKeyboard import start_keyboard
from keyboards.inline.contactinline import contact_inline
from loader import dp
from keyboards.default.courcesKeyboard import courses_keyboard, foundation_keyboard, professional_keyboard


@dp.message_handler(text='Kurslar  💻')
async def bot_start(message: types.Message):
    text = "Bizning kurslarimiz 📋"
    await message.answer(text, reply_markup=courses_keyboard)


@dp.message_handler(text='Foundation 🎯')
async def foundation(message: types.Message):
    text = """
    📌 Dasturlash asoslarini o'rganish bir nechta muhim sabablarga ega:

📚 Dasturlash mantig'ini tushunish: dasturlash asoslari dasturlarning mantig'i va ishlash tamoyillarini tushunishga imkon beradi. Siz kompyuterlar ma'lumotni qanday qayta ishlashini va ma'lumotlar bilan qanday munosabatda bo'lishini bilib olasiz.

🔍 Algoritmik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish algoritmik fikrlash ko'nikmalarini va murakkab vazifalarni sodda va tushunarli bosqichlarga bo'lish qobiliyatini rivojlantirishga yordam beradi. Siz samarali muammolarni hal qilish algoritmlarini ishlab chiqishingiz mumkin.

👥  Jamoa bilan ishlash: dasturlash asoslarini bilish sizga boshqa ishlab chiquvchilar bilan samarali hamkorlik qilish imkonini beradi. Siz umumiy tilda tushunishingiz va muloqot qilishingiz, boshqa ishlab chiquvchilar tomonidan yaratilgan kodni osonroq ajratishingiz va tushunishingiz mumkin.

🚀 Analitik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish analitik fikrlash va muammolarni muntazam ravishda hal qilish qobiliyatini rivojlantiradi. Siz muammolarni tahlil qilishni, ularning sabablarini topishni va oqilona echimlarni ishlab chiqishni o'rganasiz.

🦾 Texnologiyaning texnik tomonini tushunish: texnologiyaga boy dunyoda dasturlash asoslarini tushunish sizga texnik echimlar va texnologik mahsulotlar bilan yaxshiroq tushunish va o'zaro aloqada bo'lishga yordam beradi.

🎓 Dasturlash asoslarini o'rganish sizga nafaqat o'ziga xos dasturlash ko'nikmalarini beradi, balki tanqidiy fikrlash, ijodkorlik va muammoli fikrlashni rivojlantirishga yordam beradi. Ushbu ko'nikmalar nafaqat dasturlash sohasida, balki faoliyatning turli sohalarida ham qimmatli va foydalidir.
    """
    await message.answer(text, reply_markup=foundation_keyboard)


@dp.message_handler(text='Professional 🤓')
async def professional_handler(message: types.Message):
    await message.answer('Professional kurslarni tanlang:', reply_markup=professional_keyboard)


@dp.message_handler(text='Kids 👦')
async def kids_handler(message: types.Message):
    photo = open('static/img/kids.jpg', 'rb')
    text = """
    💻  Kursing davomiyligi 1 yil 8 oy bo’lib, haftada 1 kun 3 soat dan bo’lib o’tadi. Kurs davomida siz:

—  Scratch;
— Typing;
— Microsoft Office (Word, Excel, Power Point);
— Software & Hardware;
— Robototexnika «Arduino»;
— Python;
— Photoshop;
— 3D Modelling;
— Front-End;
— App Inventor;

💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov: 700 000  so'm.
    """
    await message.answer_photo(photo=photo, caption=text, reply_markup=contact_inline)


@dp.message_handler(text='Kerakli noutbuk 💻')
async def kakli_noutbuk(message: types.Message):
    photo = open('static/img/noutbuk.jpg', 'rb')
    text = """
    👨🏻‍💻 Dasturlash uchun talab qilinadigan minimum noutbuk, agar yangi olmoqchi bo’lsangiz:

🔸 Kami bilan Core i5 (10-avlod) yoki AMD Ryzen 5 (Core i7 bo’lsa yaxshi)
🔸 Tezkor xotira RAM kami bilan 8GB (16 bo'lsa yaxshi)\- Asosiy Xotira SSD kami bilan 256 GB

💻 Agar Apple MacBook olmoqchi bo’lsangiz va pulingiz yetarli bo’lsa:

🔹 Kami bilan M1 Protsessor
🔹 Kami bilan 8GB RAM xotira
🔹 Kami bilan 256GB doimiy SSD xotira

🖥 Agar oldingi kompyuteringiz bo’lsa uning texnik holatini quyidagilarga keltirib olishingiz maqsadga muvofiq:

🔻 RAM xotira 8GB kamida;
🔻 Agar HDD xotira bo’lsa, uni kamida 256GB SSDga almashtirish yoki HDD yoniga o’rnatish
    """

    await message.answer_photo(photo=photo, caption=text, reply_markup=contact_inline)


@dp.message_handler(text='Back  ↩️')
async def back(message: types.Message):
    await message.answer("Siz asosiy saxifaga o'tdingiz:", reply_markup=start_keyboard)