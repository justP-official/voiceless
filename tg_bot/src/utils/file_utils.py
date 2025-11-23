import os

from aiogram import Bot


async def download_voice(voice_id: str, bot: Bot) -> str:
    file = await bot.get_file(voice_id)
    file_name = file.file_path

    file_path = f"./tmp_audios/{voice_id}.ogg"

    await bot.download_file(file_name, file_path)

    return file_path


async def delete_voice(voice_id: str) -> None:
    file_path = f"./tmp_audios/{voice_id}.ogg"
    
    if os.path.exists(file_path):
        os.remove(file_path)
