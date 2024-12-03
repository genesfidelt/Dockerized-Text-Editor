# Use official Python image as base image
FROM python:3.9-slim

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy your application into the container
COPY src /app/src

# Set the default command to run your application
CMD ["python3", "/app/src/text_editor.py"]
