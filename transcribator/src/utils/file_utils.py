import os

from pydub import AudioSegment


async def save_file(file) -> str:
    file_name = file.filename

    dest_path = file_name

    with open(dest_path, "wb") as f:
        content = file.file.read()
        f.write(content)

    return dest_path


async def delete_file(file_path: str) -> None:    
    if os.path.exists(file_path):
        os.remove(file_path)


async def convert_audio(file_path: str) -> str:    
    audio = AudioSegment.from_ogg(file_path)

    output_file = file_path.replace("ogg", "wav")

    audio.export(out_f=output_file, format="wav")

    await delete_file(file_path)

    return output_file
