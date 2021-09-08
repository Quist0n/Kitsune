FROM python:3.8

RUN apt-get update \
    && apt-get install -y \
        nginx \
        libpq-dev \
        curl \
    && pip3 install uwsgi

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

COPY ./nginx.conf /etc/nginx/sites-enabled/default

ENV LANG=C.UTF-8

CMD service nginx start \
    && uwsgi -s /tmp/kemono.sock \
    --chmod-socket=666 \
    --manage-script-name \
    --mount /=server:app \
    --processes 1 \
    --threads 2 \
    --master \
    --listen 40000 \
    --disable-logging \
    --log-5xx \
    --enable-threads
