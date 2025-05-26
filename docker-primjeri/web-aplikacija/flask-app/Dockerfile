FROM python:3.13-alpine

COPY app /app

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]

# CMD ["sh"]




