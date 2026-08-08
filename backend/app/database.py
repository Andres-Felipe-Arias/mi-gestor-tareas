from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Definimos la ruta de la base de datos (se creará un archivo 'gestor_tareas.db')
SQLALCHEMY_DATABASE_URL = "sqlite:///./gestor_tareas.db"

# 2. Creamos el motor de conexión de SQLAlchemy
# connect_args={"check_same_thread": False} es necesario solo para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Creamos la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Clase base para construir nuestros modelos de tablas en models.py
Base = declarative_base()


# 5. Función de dependencia para obtener la sesión de la BD en las rutas de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()