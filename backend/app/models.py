from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relación: Un usuario puede tener muchas tareas
    tareas = relationship("Tarea", back_populates="propietario")


class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    completada = Column(Boolean, default=False)
    prioridad = Column(String, default="media")  # "baja", "media", "alta"
    created_at = Column(DateTime, default=datetime.utcnow)

    # Clave foránea hacia la tabla usuarios
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    # Relación inversa
    propietario = relationship("Usuario", back_populates="tareas")