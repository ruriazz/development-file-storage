FROM python:3.8.10-alpine

RUN apk update && \
    apk add libmagic \
    --no-cache --update gcc

ENV PYTHONBUFFERED 1

COPY ./. /application/.

WORKDIR /application

RUN pip3 install --upgrade pip
RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

RUN flask routes

EXPOSE 80/tcp

CMD exec gunicorn app:app --bind=0.0.0.0:80 --workers=4 --max-requests=1000 --timeout=1800