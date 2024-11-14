FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'project.settings'

COPY requirements.txt requirements.txt

RUN apt update -y && apt upgrade -y && pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod +x project/deploy/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/opt/app/project/deploy/entrypoint.sh"]