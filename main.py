import asyncio

from app.bot.bot_instance import bot
from app.message_handlers.url_handler import *
from app.message_handlers.welcome_message import *



async def main():
    try:
        # await bot.infinity_polling()
        await bot.infinity_polling()
    except Exception as e:
        print(f"Bot crashed: {e}")
    



if __name__ == "__main__":
    print(len(bot.message_handlers))
    asyncio.run(main())
