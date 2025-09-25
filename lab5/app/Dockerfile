FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y curl gnupg2 apt-transport-https unixodbc unixodbc-dev && \
    # Add Microsoft GPG key
    curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/microsoft.gpg && \
    # Add Microsoft repository for Debian 12 (bookworm is closest to trixie for ODBC drivers)
    echo "deb [arch=amd64,armhf,arm64] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    # Install Microsoft ODBC driver
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 || \
    # Fallback: try without specific version if msodbcsql18 fails
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:8000"]