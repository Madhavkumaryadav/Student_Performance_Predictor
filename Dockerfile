FROM python:3.11-slim-bookworm

WORKDIR /app

COPY . /app

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends awscli \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip \
    && pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-10000} app:app"]
