FROM python:3.12-slim

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY src/BackEnd .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/BackEnd/ .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "mainApi:app", "--host", "0.0.0.0", "--port", "8000"]