FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api

COPY requirements.txt /api/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8033
COPY . /api/

CMD ["gunicorn", "--workers=3", "--bind=:8033", "--preload", "--threads=20", "run_api:app"]