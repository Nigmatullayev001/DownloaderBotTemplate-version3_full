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

# Social Media Downloaders

## Pinterest Downloader V1  
[JustMobi API - Pinterest Downloader](https://rapidapi.com/JustMobi/api/pinterest-downloader-download-pinterest-image-video-and-reels/playground/)

## Pinterest Downloader V2  
[Vikas5914 API - Pinterest Downloader](https://rapidapi.com/vikas5914/api/pinterest-video-and-image-downloader/playground/)

## Facebook Downloader V2  
[3205 API - Facebook Downloader](https://rapidapi.com/3205/api/facebook17/playground/apiendpoint_1be6aca0-afb7-4f3a-a4a0-720dcd5cf5c1)

## Instagram Downloader  
[SafeSite15 API - Instagram Downloader](https://rapidapi.com/safesite15/api/instagram-downloader-download-instagram-stories-videos4/pricing)

## YouTube Media Downloader  
[DataFanatic API - YouTube Media Downloader](https://rapidapi.com/DataFanatic/api/youtube-media-downloader/pricing)

## TikTok Video Downloader  
[ElisBushaj2 API - TikTok Video Downloader](https://rapidapi.com/elisbushaj2/api/tiktok-video-downloader-api)


