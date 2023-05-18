FROM python:3.10.7

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install curl python3-brlapi -y

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r ./requirements.txt

