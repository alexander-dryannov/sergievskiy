FROM python:3.14.6-alpine

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'project.settings'
ENV PIP_NO_CACHE_DIR=1

COPY requirements.txt requirements.txt

RUN apk update && apk upgrade && \
    apk add --no-cache curl libpq && \
    apk add --no-cache --virtual .build-deps build-base gcc musl-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

COPY . .

RUN chmod +x project/deploy/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/opt/app/project/deploy/entrypoint.sh"]