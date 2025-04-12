import os
import pyqrcode
from telebot import async_telebot
from telebot import types


from app.bot.bot_instance import bot



class QRService():
   async def make_qr(bot: async_telebot, message: types.Message):
        try:
            url = message.text
            qrcode = pyqrcode.create(url)
            qrcode.png("qrcode.png", scale = 6)
            with open("qrcode.png", mode="rb") as file:
                await bot.send_photo(message.chat.id, photo=file, caption="Ваш QR-код")
            os.remove("qrcode.png")
        except Exception as e:
            await bot.send_message(message.chat.id, f"Извините< произошла какая-то ошибка")
            await print(e)