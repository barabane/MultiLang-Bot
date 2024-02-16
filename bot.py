import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from keyboards import main_keyboard

from routers import add_router

load_dotenv()


async def main():
    bot = Bot(token=os.getenv("BOT_KEY"))
    dp = Dispatcher()

    dp.include_routers(add_router.router)

    @dp.message(CommandStart())
    async def start_handler(msg: types.Message):
        await msg.answer("Главное меню", reply_markup=main_keyboard())

    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
