FROM python:3.12

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /lab5/app
COPY lab5/app /lab5/app

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
