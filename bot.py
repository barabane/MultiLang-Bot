import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()


async def main():
    bot = Bot(token=os.getenv("BOT_KEY"))
    dp = Dispatcher()

    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main(), debug=True)