# VOICELESS — расшифровка голосовых сообщений в ТГ

## Запуск

Соберите и запустите Docker-контейнеры:

```docker-compose up --build```

Документация будет доступна по адресу http://localhost:8000/docs

## Стэк

1. Bot:
    - aiogram;
    - httpx;
2. Transcriber:
    - speech_regnizer;
    - PuDub;
    - FastAPI;
    - Pydantic;