FROM python:3.7.6-buster
MAINTAINER Lukasz Admin

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN pip install -r /requirements.txt



RUN useradd -ms /bin/bash admin
RUN mkdir /app

COPY ./app/ /app
WORKDIR /app
RUN chown -R admin:admin /app
RUN chmod 755 /app
USER admin
