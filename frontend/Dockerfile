FROM python:3.8.3-alpine3.10

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]