#!/bin/sh

python django_app.py migrate --no-input
python django_app.py collectstatic --no-input

#python django_app.py runserver 0.0.0.0:8000 --noreload

gunicorn django_project.telegrambot.telegrambot.wsgi:application --bind 0.0.0.0:8000
