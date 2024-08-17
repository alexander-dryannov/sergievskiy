FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'project.settings'

COPY project/requirements/base.txt base.txt

RUN apt update -y && apt upgrade -y && pip install --upgrade pip && pip install -r base.txt

COPY . .

RUN chmod +x project/deploy/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/opt/app/project/deploy/entrypoint.sh"]