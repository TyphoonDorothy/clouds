FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy the whole lab5 folder
COPY lab5 /app/lab5

# make sure Python can import modules inside /app/lab5
ENV PYTHONPATH=/app/lab5

# default port (Azure will set PORT if needed)
ENV PORT=5000
EXPOSE ${PORT}

# ensure gunicorn runs from lab5 and uses the wsgi module there
WORKDIR /app/lab5

# use --chdir as extra safety, bind to env PORT
CMD ["sh", "-c", "gunicorn --workers 4 --chdir /app/lab5 --bind 0.0.0.0:${PORT} wsgi:app"]
