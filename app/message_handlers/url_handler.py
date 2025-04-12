from telebot.asyncio_handler_backends import BaseMiddleware
from telebot import types

from app.bot.bot_instance import bot
from app.services.url_service import UrlService
from app.services.qr_service import QRService


@bot.message_handler(func = lambda m:True)
async def send_qr(message: types.Message):
    try:
        if not message.text:
            await bot.reply_to(message, "Пожалуйста, отправьте текстовую ссылку")
            return
        
        result = await UrlService.is_url_like(message.text)
        if result:
            await QRService.make_qr(bot ,message)
        else:
            await bot.reply_to(message, "Это не похоже на ссылку!")
    except Exception as e:
        await bot.reply_to(message, f"Произошла ошибка: {str(e)}")
        print(str(e))
        