FROM python:3.12-slim


RUN apt-get update && \
    apt-get install -y curl gnupg2 unixodbc unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:8000"]
