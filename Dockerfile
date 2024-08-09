FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'project.settings'

COPY project/requirements/base.txt base.txt

RUN  apt update -y && apt upgrade -y && pip install --upgrade pip && pip install -r base.txt

COPY . .

RUN chmod +x /opt/app/project/deploy/entrypoint.sh

EXPOSE 8000

CMD ["/opt/app/project/deploy/entrypoint.sh"]