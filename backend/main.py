from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Sistema RAG")

# Ruta absoluta hacia la carpeta frontend en el contenedor
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

# Si la carpeta existe, montamos los archivos estáticos (CSS, JS, imágenes, etc.)
if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
def read_root():
    # Retorna tu index.html cuando visitas la raíz http://localhost:8000
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "El archivo index.html no se encontró en la carpeta frontend/"}