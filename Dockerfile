FROM python:3.11-alpine

COPY ./requirements.txt /code/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN --mount=type=cache,target=/root/.cache/pip \
        pip install --default-timeout=600 -r /code/requirements.txt

WORKDIR /code
