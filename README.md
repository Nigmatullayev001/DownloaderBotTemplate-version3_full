# Project README

This project involves setting up a bot that requires environment variables for proper configuration. Below is a guide to help you configure the necessary `.env` file and get your bot running.

## Prerequisites

Before starting, make sure you have the following:
- A **Telegram Bot token** from [BotFather](https://core.telegram.org/bots#botfather).
- **API keys** (if applicable) for any services your bot interacts with.
- Access to the relevant **Telegram channel or group** for admin privileges (if needed).

## Setting up the `.env` file

Create a `.env` file in the root of your project folder. Copy and paste the following information into the `.env` file and replace the placeholders with your own values:

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
