import os

from dotenv import find_dotenv, load_dotenv

from aiogram import Router, F, Bot
from aiogram.types import Message

import httpx

from utils.file_utils import download_voice, delete_voice
from utils.net_utils import send_file


load_dotenv(find_dotenv())

TRANSCRIBATOR_URL = os.getenv("TRANSCRIBATOR_URL")


user_private_router = Router()

@user_private_router.message(F.voice)
async def process_voice(message: Message, bot: Bot):
    await message.answer("Voice")

    voice_id = message.voice.file_id

    file = await download_voice(voice_id, bot)

    response = await send_file(file)

    await delete_voice(voice_id)
    
    await message.answer(response.json()["message"])
    