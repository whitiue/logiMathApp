FROM python:3.12-slim

# Crear usuario no-root para ejecutar aplicación
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requeriments_frontend.txt .
RUN pip install --no-cache-dir -r requeriments_frontend.txt

# Copiar código de aplicación
COPY . .

# Cambiar propiedad a usuario no-root
RUN chown -R appuser:appuser /app

# Cambiar a usuario no-root
USER appuser

# Para Kivy, si necesitas display, considera usar X11 forwarding o VNC
CMD ["python", "mainApp.py"] 