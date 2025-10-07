FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.10

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql-client \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Use a dedicated working directory for the app
WORKDIR /app

# Copy only the files we need during image build. The workspace will be mounted at runtime by docker-compose.
COPY requirements.txt /app/

RUN pip3 install -r /app/requirements.txt
