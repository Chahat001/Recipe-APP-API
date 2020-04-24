FROM python:3.7-alpine
MAINTAINER chahatpreet Singh Grewal

ENV   PYTHONUNBUFFERED 1

COPY  ./requirements.txt /requiremnts.txt

RUN pip install -r/requiremnts.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
