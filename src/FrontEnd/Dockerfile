FROM ubuntu:22.04

# Instalar Python y dependencias de Flet
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3-pip \
    libgtk-3-0 \
    libglib2.0-0 \
    libx11-6 \
    libxcursor1 \
    libxrandr2 \
    libxinerama1 \
    libxi6 \
    libxext6 \
    libxdamage1 \
    libxcomposite1 \
    libxrender1 \
    libgstreamer1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    libgstreamer-app1.0-0 \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY src/FrontEnd/ .
RUN pip install --no-cache-dir -r requirements_frontend.txt

COPY src/FrontEnd/ .

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python3", "mainApp.py"]