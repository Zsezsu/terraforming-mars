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
ENV PYTHONUNBUFFERED=1
ENV PORT=10000

# Render will set $PORT; we default to 10000 for local runs
EXPOSE 10000

# Run Gunicorn (env vars expand in shell-form)
CMD gunicorn -w ${WEB_CONCURRENCY:-2} -k gthread -b 0.0.0.0:${PORT:-10000} --threads ${GTHREADS:-4} --timeout 120 server:app

