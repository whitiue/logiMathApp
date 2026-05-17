FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-11-jdk \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Descargar e instalar Android SDK
RUN mkdir -p /home/appuser/Android/sdk && \
    cd /home/appuser/Android/sdk && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip && \
    unzip -q commandlinetools-linux-9477386_latest.zip && \
    rm commandlinetools-linux-9477386_latest.zip

ENV ANDROID_SDK_ROOT=/home/appuser/Android/sdk
ENV PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$ANDROID_SDK_ROOT/platform-tools

RUN useradd -m -u 1000 appuser
WORKDIR /app
COPY src/FrontEnd/ .
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R appuser:appuser /app /home/appuser/Android
USER appuser
CMD ["flet", "build", "apk", "--release"]