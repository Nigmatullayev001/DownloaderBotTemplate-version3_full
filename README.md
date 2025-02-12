# Loyihaning README Fayi

Ushbu loyiha botni sozlashni o'z ichiga oladi, bu esa to'g'ri konfiguratsiya uchun muhit o'zgaruvchilariga muhtoj. Quyida `.env` faylini sozlash va botni ishga tushirish bo'yicha ko'rsatmalar keltirilgan.

## Talablar

Boshlashdan oldin quyidagi narsalar mavjudligini tekshirib chiqing:
- **Telegram Bot tokeni**: [BotFather](https://core.telegram.org/bots#botfather) dan olingan token.
- **API kalitlari** (agar kerak bo'lsa), bot o'zaro aloqada bo'ladigan tashqi xizmatlar uchun.
- **Telegram kanal yoki guruh**ga admin huquqlari, agar bot undan foydalanishi kerak bo'lsa.

## `.env` Faylini Sozlash

Loyihangiz papkasida `.env` faylini yarating. Quyidagi ma'lumotlarni `.env` fayliga nusxalab joylashtiring va o'z ma'lumotlaringiz bilan almashtiring:

```env
# YANGI .env FAYL YARATING VA
# QUYIDAGI MA'LUMOTLARNI YOZING:

# ADMINLARNI ID sini kiritish kerak,
ADMINS=123456789

# BOT TOKEN botfather dan olinadi
BOT_TOKEN=1234567891011:ABDEFGHLJKLMNO-142F

# Api keyni kiriting
API_KEY=481565499-54gfdASDA

# Qo'shimcha api key
EXTRA_API_KEY=481565499-54gfdASDA

# majburiy azo uchun bot ni kanal/guruhga admin qilish kerak
CHANNEL_USERNAME=@username

# ip
ip=localhost
