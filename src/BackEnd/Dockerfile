FROM python:3.12-slim

# Crear usuario no-root para ejecutar aplicación
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requeriments_backend.txt .
RUN pip install --no-cache-dir -r requeriments_backend.txt

# Copiar código de aplicación
COPY . .

# Cambiar propiedad a usuario no-root
RUN chown -R appuser:appuser /app

# Cambiar a usuario no-root
USER appuser

EXPOSE 8000

CMD ["uvicorn", "mainApi:app", "--host", "0.0.0.0", "--port", "8000"]