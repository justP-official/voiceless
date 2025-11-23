from speech_recognition import AudioFile, Recognizer


from .file_utils import convert_audio, delete_file

async def transcribe(file_name: str) -> str:
    file_name = await convert_audio(file_name)

    recognizer = Recognizer()

    with AudioFile(file_name) as source:
        audio = recognizer.record(source)

        result = recognizer.recognize_sphinx(audio)

    await delete_file(file_path=file_name)

    return result

    
