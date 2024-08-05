#!/bin/sh

# Load environment variables from .env file
export $(grep -v '^#' /backend/.env | xargs)

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3
