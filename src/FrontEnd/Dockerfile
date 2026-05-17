FROM python:3.12-slim

# Instalar dependencias de GTK y otras librerías que Flet necesita
RUN apt-get update && apt-get install -y \
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
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY src/FrontEnd/ .
RUN pip install --no-cache-dir -r requirements_frontend.txt

COPY src/FrontEnd/ .

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "mainApp.py"]