import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv

from handlers.user_private import user_private_router

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv("TG_TOKEN"))

dispatcher = Dispatcher()

dispatcher.include_routers(
    user_private_router,
)


@dispatcher.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Start")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    
    await dispatcher.start_polling(bot)


asyncio.run(main())