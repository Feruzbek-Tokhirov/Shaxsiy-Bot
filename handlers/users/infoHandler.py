from aiogram import types

from keyboards.inline.contactinline import contact_inline, ijtimoiy_inline
from loader import dp
from keyboards.default.infoKeyboard import info_keyboard


@dp.message_handler(text='Biz Haqimizda 📔')
async def info(message: types.Message):
    await message.answer(
        "📍 Bizning manzil: Mirzo Ulug'bek tumani, Mirzo Ulug'bek ko'chasi 54A (https://shorturl.at/iJKSV)",
        reply_markup=info_keyboard)


@dp.message_handler(text="Umumiy Ma'lumot  📰")
async def info(message: types.Message):
    text = """
    📌 iSystem IT Akademmiyasi - bu Axborot Texnologiyalarini o'qitishga ixtisoslashgan akademiya. Biz talabalarga IT sohasida yuqori natijalarga erishish mumkin bo'lgan keng ko'lamli kurslar va dasturlarni taklif etamiz. iSystem IT Akademiyasi haqida asosiy ma'lumotlar:

1️⃣  Kurslar va dasturlar: iSystem IT Akademiyasi Python va Java Backend, Veb-dasturlash, Mobil dasturlash, Ma'lumotlar bazalari, Sun'iy intellekt, ma'lumotlarni tahlil qilish va shu kabi turli xil IT sohalarini qamrab olgan kurslar va o'quv dasturlarini taklif etadi. Kurslar talabalarning turli darajadagi bilimlariga mos keladigan Boshlang'ich(Foundation) yoki Professional yo'nalishlarga bo'linadi.

2️⃣  O'qituvchilar: iSystem IT Akademiyasi o'z sohalarida mutaxassis bo'lgan tajribali va malakali o'qituvchilar guruhiga ega. Ular IT sohasida amaliy tajribaga ega va talabalarga tegishli bilim va ko'nikmalarni taqdim etishga qodir.

3️⃣  Amaliy yondashuv: iSystem IT Akademiyasi amaliy o'rganishga e'tibor qaratadi, bu yerda talabalar 70% amaliy 30% nazariy bilim olib, haqiqiy tajribaga ega bo'ladilar. Bu talabalarga o'z bilimlarini amalda qo'llashga va yuqori natija uchun zarur bo'lgan amaliy ko'nikmalarni rivojlantirishga yordam beradi.

4️⃣  Moslashuvchanlik: iSystem IT Akademiyasi moslashuvchan o'rganish imkoniyatlarini, jumladan, ertalabki, kunduzgi, kechki va dam olish kunlaridagi darslarni, shuningdek, onlayn kurslarni taklif etadi, bu esa turli o'quv jadvali va majburiyatlarga ega talabalar uchun o'rganishni osonlashtiradi.

5️⃣  Ishga kirishda yordam: iSystem IT Akademiyasi talabalarining kasbiy rivojlanishini qo'llab-quvvatlaydi. Bunga rezyume, CV yozishda yordam berish, suhbatga tayyorgarlik ko'rish, ish qidirish va kasbiy ko'nikmalarni rivojlantirish bo'yicha maslahatlar kiradi.

🏢  iSystem IT Academy - bu IT sohasida muvaffaqiyat qozonishni istagan talabalarga yuqori sifatli ta'lim akademiyasi.
    """

    await message.answer(text, reply_markup=contact_inline)


@dp.message_handler(text="Afzalliklar  📌")
async def info(message: types.Message):
    text = """
    🏢 iSystem IT Akademiyasi boshqa akademiyalardan bir nechta farqlarga ega, bu esa talabalar uchun ajoyib tanlovdir. 

✨ iSystem IT Academy o'zining yuqori darajadagi ta'limi bilan mashhur va o'z sohalarida mutaxassis bo'lgan tajribali o'qituvchilar tomonidan ishlab chiqilgan kurslarni taklif etadi. O'quv dasturlari yangilangan va zamonaviy IT sohasi talablariga javob beradi.

✔️  Ta'lim sifati
✔️  Amaliy yo'nalish
✔️  Ta'limning moslashuvchanligi
✔️  Tajribali o'qituvchilar
✔️  Ishga kirishda qo'llab-quvvatlash
✔️  Moslashuvchan o'quv jadvali
✔️  Dasturlarning dolzarbligi

⭐️ iSystem IT Akademiyasini sifatli ta'lim va IT sohasida muvaffaqiyatli martaba boshlashga intilayotgan talabalar uchun jozibali tanlovga aylantiradigan farqlardan biri.
    """

    await message.answer(text, reply_markup=contact_inline)


@dp.message_handler(text='Ijtimoiy tarmoqlarimiz 🌍')
async def tarmoqlarimiz(message: types.Message):
    photo = open('static/img/isystem.jpg', 'rb')
    text = "Bizni kuzatib boring: "
    await message.answer_photo(photo=photo, caption=text, reply_markup=ijtimoiy_inline)
