from fastapi import FastAPI
from app.database import engine, Base

# Crea las tablas en la base de datos SQLite si no existen
Base.metadata.create_all(bind=engine)

# Instancia principal de la aplicación (debe llamarse 'app')
app = FastAPI(title="API de Gestor de Tareas")

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a la API del Gestor de Tareas!"}

from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Gestor de Tareas")

# Incluimos las rutas de autenticación
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a la API del Gestor de Tareas!"}