FROM python:3.7-alpine
MAINTAINER chahatpreet Singh Grewal

ENV   PYTHONUNBUFFERED 1

COPY  ./requirements.txt /requiremnts.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-builds-deps gcc libc-dev linux-headers postgresql-dev
RUN pip install -r/requiremnts.txt
RUN apk del .temp-builds-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
