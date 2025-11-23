from fastapi import FastAPI, UploadFile

from utils.file_utils import save_file
from utils.transcribe_audio import transcribe

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/transcribe/")
async def transcribe_voice(file: UploadFile):
    file_path = await save_file(file)

    res = await transcribe(file_path)

    return {"message": res}
