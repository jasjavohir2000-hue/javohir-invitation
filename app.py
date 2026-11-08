
import os
import telebot
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "✨ JAVOHIR INVITATION ga xush kelibsiz!\n\n"
        "To‘y va tadbirlar uchun premium elektron taklifnomalar.\n\n"
        "Buyurtma berish uchun /order buyrug‘ini yuboring."
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['order'])
def order(message):
    bot.send_message(
        message.chat.id,
        "💍 Buyurtma berish uchun quyidagi ma'lumotlarni yozing:\n\n"
        "1. Ism-familiya\n"
        "2. Tadbir sanasi\n"
        "3. Tadbir vaqti\n"
        "4. Manzil\n"
        "5. Telefon raqam"
    )

@bot.message_handler(func=lambda message: True)
def other(message):
    bot.send_message(
        message.chat.id,
        "Xabaringiz qabul qilindi. Buyurtma uchun /order ni bosing."
    )

@app.route('/')
def home():
    return "JAVOHIR INVITATION BOT IS RUNNING!"

@app.route('/' + os.environ.get("WEBHOOK_SECRET", "secret"))
def webhook():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
