FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

# Install ImageMagick and disable certain policies
RUN apt-get update && \
    apt-get install -y imagemagick && \
    mv /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xml.off
