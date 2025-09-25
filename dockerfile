FROM ubuntu:22.04

WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3 \
    python3-pip \ 
    python3-dev \
    unixodbc \
    unixodbc-dev \
    curl \
    gnupg2 \
    apt-transport-https \
 && rm -rf /var/lib/apt/lists/*


RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft.gpg \
 && echo "deb [arch=amd64,arm64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list \
 && apt-get update \
 && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
 && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "my_project:init_app()"]
