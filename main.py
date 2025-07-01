import telebot
from dotenv import load_dotenv
import os
import random

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🌸 أهلاً بكِ في بوت AYA FLOWERS 🌸\nاختاري من القوائم!")

# نصيحة جمالية
@bot.message_handler(commands=['tip'])
def send_tip(message):
    with open("assets/tips.txt", "r", encoding="utf-8") as f:
        tips = f.readlines()
    bot.reply_to(message, "💄 " + random.choice(tips))

bot.infinity_polling()
