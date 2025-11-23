import os

import httpx

TRANSCRIBATOR_URL = os.environ.get("TRANSCRIBATOR_URL")

async def send_file(file: str) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        with open(file, 'rb') as f:
            files = {"file": (file, f, "audio/ogg")}
            result = await client.post(f"{TRANSCRIBATOR_URL}transcribe/", files=files)
    
    return result