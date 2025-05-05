
FROM python:3.10.10-slim AS prod


RUN apt-get update && apt-get install -y --no-install-recommends\
    libreoffice-writer \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /TELEBOTGRAM

COPY pyproject.toml poetry.lock /TELEBOTGRAM/


RUN poetry config virtualenvs.create false


RUN poetry install --only main --no-root


RUN apt-get purge -y && rm -rf /var/lib/apt/lists/*


COPY . /TELEBOTGRAM/