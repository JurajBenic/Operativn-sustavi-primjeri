FROM python:3.13-alpine

RUN mkdir /app
COPY app.py /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# Keep the container running by default
CMD ["sh"]




