from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
API_KEY = env.str("API_KEY")  # rapidapi.com dan api olish
EXTRA_API_KEY = env.str("EXTRA_API_KEY")  # rapidapi.com dan qo'shimcha api olish
CHANNEL_USERNAME = env.str("CHANNEL_USERNAME")  # kanal/guruh linki
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
