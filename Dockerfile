FROM python:3.12-slim

# Don't write pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Don't buffer stdout and stderr
ENV PYTHONUNBUFFERED=1

# Non interactive mode when installing debian packages
ENV DEBIAN_FRONTEND=noninteractive
# Set the locale
ENV LANG=C.UTF-8

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app