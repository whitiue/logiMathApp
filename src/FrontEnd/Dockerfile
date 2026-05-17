FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
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
    gstreamer1.0-plugins-base \
    libgstreamer-plugins-base1.0-0 \
    libgstreamer-plugins-good1.0-0 \
    libgstreamer-plugins-bad1.0-0 \
    gstreamer1.0-alsa \
    gstreamer1.0-pulseaudio \
    libmpv1 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 appuser
WORKDIR /app
COPY src/FrontEnd/ .
RUN pip install --no-cache-dir -r requirements_frontend.txt
RUN chown -R appuser:appuser /app
USER appuser
CMD ["python3", "mainApp.py"]