FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY lab5 ./lab5
EXPOSE 5000
WORKDIR /app/lab5
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
