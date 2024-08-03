# pull official base image
FROM python:3.12.41-slim

# set working directory
RUN mkdir /backend
WORKDIR /backend
# COPY requirements.txt /backend/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/.venv
ENV PATH=$VIRTUAL_ENV/bin:$PATH


# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql libpq-dev cron \
  && apt-get clean

# install dependencies
RUN python -m venv $VIRTUAL_ENV && pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock ./
ARG RELEASE=false
RUN ! $RELEASE && poetry install --no-cache --no-root --only dev || $RELEASE
RUN poetry install --no-cache --no-root --only main

# Add health check
HEALTHCHECK --interval=10s CMD python manage.py check

# copy entrypoint.sh
COPY scripts/entrypoint.sh /
RUN sed -i 's/\r$//g'  /entrypoint.sh
RUN chmod +x /entrypoint.sh

# add app
COPY . /backend/

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
