from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# --- SCHEMAS DE USUARIO ---
class UsuarioBase(BaseModel):
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioOut(UsuarioBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- SCHEMAS DE AUTENTICACIÓN ---
class Token(BaseModel):
    access_token: str
    token_type: str

# --- SCHEMAS DE TAREAS ---
class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: Optional[bool] = False
    prioridad: Optional[str] = "media"

class TareaCreate(TareaBase):
    pass

class TareaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    completada: Optional[bool] = None
    prioridad: Optional[str] = None

class TareaOut(TareaBase):
    id: int
    created_at: datetime
    usuario_id: int

    class Config:
        from_attributes = True