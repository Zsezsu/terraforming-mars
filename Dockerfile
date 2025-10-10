# syntax=docker/dockerfile:1
FROM python:3.11-slim

# System deps for psycopg2-binary (very light), logs, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc build-essential \
  && rm -rf /var/lib/apt/lists/*

# Work inside /app (container path; no need to exist on host)
WORKDIR /app

# Install deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project (server.py, templates/, static/, database/, etc.)
COPY . .

# Flask must bind to 0.0.0.0 in containers
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# Use gunicorn for a prod-like server. If your module isn't server:app, change it.
CMD ["gunicorn", "server:app", "--workers", "2", "--threads", "4", "--timeout", "120", "--bind", "0.0.0.0:5000", "--no-sendfile", "--access-logfile", "-"]