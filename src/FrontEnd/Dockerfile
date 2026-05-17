FROM python:3.12-slim

# Crear usuario no-root para ejecutar aplicación
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY src/FrontEnd/ .
RUN pip install --no-cache-dir -r requirements_frontend.txt

# Copiar código de aplicación
COPY src/FrontEnd/ .

# Cambiar propiedad a usuario no-root
RUN chown -R appuser:appuser /app

# Cambiar a usuario no-root
USER appuser

CMD ["python", "mainApp.py"] 