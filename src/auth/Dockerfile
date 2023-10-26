FROM python:3.12.0-slim-bullseye

# Install system-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential default-libmysqlclient-dev pkg-config

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 5000

CMD ["python", "server.py"]