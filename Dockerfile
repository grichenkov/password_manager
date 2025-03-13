FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install "requests<2.32"

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

ENV HOST=0.0.0.0
ENV PORT=8000


CMD poetry run password-manager --host $HOST --port $PORT
