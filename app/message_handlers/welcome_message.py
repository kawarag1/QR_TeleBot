from app.bot.bot_instance import bot

@bot.message_handler(commands=['start'])
async def welcome_message(message):
    await bot.send_message(message.chat.id, f'Привет! Я телеграмм бот для создания QR-кодов!')
