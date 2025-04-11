import telebot
import png
import pyqrcode
import os



bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, f'Привет! Я телеграмм бот для создания QR-кодов!')



@bot.message_handler(commands=['make'])
def reply(message):
    bot.send_message(message.chat.id, "Отправьте ссылку, которую хотите превратить в qr-код")

@bot.message_handler(func=lambda message:True)
def make_qr(message):
    try:
        url = message.text
        qrcode = pyqrcode.create(url)
        qrcode.png("qrcode.png", scale = 6)
        with open("qrcode.png", mode="rb") as file:
            bot.send_photo(message.chat.id, photo=file, caption="Ваш QR-код")
        os.remove("qrcode.png")
    except Exception as e:
        bot.send_message(message.chat.id, f"Извините< произошла какая-то ошибка")




    



        









bot.infinity_polling(none_stop = True)
