FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /web_django
WORKDIR /web_django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /web_django/

RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_django/
