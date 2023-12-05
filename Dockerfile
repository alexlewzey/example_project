FROM python:3.10

RUN apt-get update && \
    apt-get install -y gcc python3-dev

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-cache

COPY . /app

