FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

ENV APP_PORT=8080

CMD ["python", "app.py"]
