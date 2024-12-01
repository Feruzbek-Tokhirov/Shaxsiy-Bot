from aiogram import types
from keyboards.default.courcesKeyboard import courses_keyboard
from keyboards.inline.contactinline import contact_inline
from loader import dp


@dp.message_handler(text='Java Backend')
async def java(message: types.Message):
    photo = open('static/img/java.jpg', 'rb')
    text1 = """
📌 Backend Java dasturlash tili veb-ilovalar va boshqa dasturiy ta'minot tizimlarining orqa qismini yaratish va saqlash uchun qo'llaniladigan dasturiy ta'minotni ishlab chiqish sohasi.

🌐 Backend Java-bu mijoz tomonidan (frontend) so'rovlarni ko'rib chiqadigan va ma'lumotlar bazalari bilan o'zaro aloqada bo'lgan, biznes mantig'ini bajaradigan, xavfsizlik, ma'lumotlarni qayta ishlash va boshqa funktsiyalarni ta'minlaydigan dasturlarning server tomoni.

📈 Backend rivojlanishi uchun dasturlash tili sifatida Java mashhurligi, keng ekotizimi va Bahor, kutish, Apache Struts va boshqa ko'plab kutubxonalar va ramkalar tufayli keng imkoniyatlarni taqdim etadi. Ular rivojlanishni osonlashtiradi va kengaytiriladigan va xavfsiz veb-ilovalarni yaratishda samaradorlik va ishonchlilikni ta'minlaydi.

👨🏻‍💻 Backend Java dasturchilari server kodini yaratish va optimallashtirish, ma'lumotlar bazasini boshqarish, so'rovlarni qayta ishlash, biznes mantig'ini amalga oshirish, dastur xavfsizligi va ishlashini ta'minlash bilan shug'ullanadi.

🦾 Backend Java kuchli, kengaytiriladigan va ishonchli veb-ilovalarni ishlab chiqishda muhim rol o'ynaydi va dasturiy ta'minot dunyosidagi ko'plab kompaniyalar va ishlab chiquvchilar uchun mashhur tanlovdir.
    """

    text2 = """
    💻  Kursing davomiyligi 6 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

— Javada ma'lumotlar ombori bilan ishlash(jdbc);
— Fayllarni server va databasega saqlash va olish;
— Spring security bilan ishlash;
— Spring framework(bean, core, context) spring mvc;
— Spring bootda loyiha qurish(clickup.com backend qismi);
— Spring framework jpa yordamida ma'lumotlar ombori bilan ishlash;
— Rest full api yoza olish;
 
💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov: 1 400 000  so'm.
    """
    await message.answer(text1)
    await message.answer_photo(photo=photo, caption=text2, reply_markup=contact_inline)


@dp.message_handler(text='Python Backend')
async def python(message: types.Message):
    photo = open('static/img/python.jpg', 'rb')
    text1 = """
📌 Backend Python  dasturlash tili veb-ilovalar va boshqa dasturiy tizimlarning orqa qismini yaratish va boshqarish uchun ishlatiladigan dasturiy ta'minotni ishlab chiqishni anglatadi.

👨🏻‍💻 Python backend-bu mijoz tomoni (frontend) so'rovlarini ko'rib chiqadigan va ma'lumotlar bazalari bilan o'zaro aloqada bo'lgan, biznes mantig'ini bajaradigan, xavfsizlik, ma'lumotlarni qayta ishlash va boshqa funktsiyalarni ta'minlaydigan dasturlarning server tomoni.

🐍 Python backend dasturlarini ishlab chiqishni osonlashtiradigan ko'plab kutubxonalar va ramkalarni taklif etadi. Backend rivojlanishi uchun ba'zi mashhur Python ramkalariga Django, Flask, Pyramid va Bottle kiradi. Ular marshrutlarni boshqarish, ma'lumotlar bazalari bilan ishlash, API ishlab chiqish va backend ishlab chiqish uchun zarur bo'lgan boshqa vazifalar uchun qulay vositalarni taqdim etadi.

🗂 Python ma'lumotlar fani va ma'lumotlarni tahlil qilishda ham keng qo'llaniladi, bu esa uni katta hajmdagi ma'lumotlarni qayta ishlash va mashinani o'rganish bilan bog'liq tizimlarni backend ishlab chiqish uchun foydali qiladi.

🪩 Backend Python ishlab chiquvchilari server kodini yaratish va optimallashtirish, ma'lumotlar bazasini boshqarish, so'rovlarni qayta ishlash, biznes mantig'ini amalga oshirish va ilovaning xavfsizligi va ishlashini ta'minlash bilan shug'ullanadi.

📚 Backend Python Python tilining soddaligi va ekspressivligi, keng funktsionalligi va kutubxonalar va ramkalarning boy ekotizimi tufayli ko'plab ishlab chiquvchilar uchun mashhur tanlovdir.
    """
    text2 = """
    💻  Kursing davomiyligi 6 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

—  Internet infrastrukturasi protokollar haqida tushuncha;
— Sof SQL bilan ishlash va murakkab so'rovlarni optimallashtirish;
— Fayllarni server va databasega saqlash va olish;
— Django web framework arxitekturasi ishlash mexanizmi;
— API ishlab chiqish, uchinchi tomon xizmatlari bilan integratsiya;
— Dokumentatsiya yaratish va undan foydalansh;
— Web texlogiyalari va ularning ishlash mexanizmi;
— Rest full api yoza olish;
— Konteynerlash texnologiyalari, Deploy qilish;
— Python web frameworklari afzalliklari va kamchiliklar;
 
💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov: 1 400 000  so'm.
    """
    await message.answer(text1)
    await message.answer_photo(photo=photo, caption=text2, reply_markup=contact_inline)


@dp.message_handler(text='Back  ↩️')
async def back(message: types.Message):
    await message.answer("Siz kurs sahifasiga o'tdingiz:", reply_markup=courses_keyboard)
