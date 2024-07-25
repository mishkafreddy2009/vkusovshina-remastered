FROM python:3.12.4

WORKDIR /app/

# COPY ./pyproject.toml /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app/app
