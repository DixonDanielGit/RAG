# 1. Usar una imagen oficial de Python ligera (slim) para ahorrar recursos en el VPS
FROM python:3.10-slim

# 2. Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalar dependencias del sistema necesarias para compilar algunas librerías si fuera necesario
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copiar e instalar las dependencias de Python primero (optimiza el caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código del backend al contenedor
COPY . .

# 6. Exponer el puerto estándar donde correrá FastAPI
EXPOSE 8000

# 7. Comando para iniciar la aplicación usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]