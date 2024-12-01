# Use official Python image as base image
FROM python:3.9-slim

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    xvfb \
    novnc \
    x11vnc \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install websockify for noVNC
RUN pip install websockify

# Set working directory inside the container
WORKDIR /app

# Copy your application into the container
COPY src /app/src

# Expose VNC port (5900) and noVNC web port (6080)
EXPOSE 5900 6080

# Copy noVNC files
RUN git clone https://github.com/novnc/noVNC.git /opt/novnc

# Set the default command to start noVNC and your app
CMD ["sh", "-c", "xvfb-run --server-args='-screen 0 1024x768x16' python3 /app/src/text_editor.py & x11vnc -display :99 -nopw -forever & /opt/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080"]

