FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

CMD ["python3", "-m", "core.aira"]
