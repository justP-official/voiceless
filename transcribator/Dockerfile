FROM python:3.13-slim

RUN apt-get -y update
RUN apt-get -y upgrade

RUN pip install --upgrade pip

RUN apt-get install -y ffmpeg

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]