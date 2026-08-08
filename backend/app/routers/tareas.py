from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Tarea, Usuario
from app.schemas import TareaCreate, TareaUpdate, TareaOut
from app.security import get_current_user

router = APIRouter(prefix="/tareas", tags=["Tareas"])

# 1. Crear Tarea
@router.post("/", response_model=TareaOut, status_code=status.HTTP_201_CREATED)
def crear_tarea(
    tarea: TareaCreate, 
    db: Session = Depends(get_db), 
    current_user: Usuario = Depends(get_current_user)
):
    nueva_tarea = Tarea(**tarea.dict(), usuario_id=current_user.id)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

# 2. Obtener todas las tareas del usuario actual
@router.get("/", response_model=List[TareaOut])
def obtener_tareas(
    db: Session = Depends(get_db), 
    current_user: Usuario = Depends(get_current_user)
):
    return db.query(Tarea).filter(Tarea.usuario_id == current_user.id).all()

# 3. Actualizar Tarea
@router.put("/{tarea_id}", response_model=TareaOut)
def actualizar_tarea(
    tarea_id: int, 
    tarea_update: TareaUpdate, 
    db: Session = Depends(get_db), 
    current_user: Usuario = Depends(get_current_user)
):
    query = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == current_user.id)
    tarea_db = query.first()

    if not tarea_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no autorizada")

    datos_actualizados = tarea_update.dict(exclude_unset=True)
    query.update(datos_actualizados)
    db.commit()
    db.refresh(tarea_db)
    return tarea_db

# 4. Eliminar Tarea
@router.delete("/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT) # status 204
def eliminar_tarea(
    tarea_id: int, 
    db: Session = Depends(get_db), 
    current_user: Usuario = Depends(get_current_user)
):
    query = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == current_user.id)
    tarea_db = query.first()

    if not tarea_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no autorizada")

    query.delete()
    db.commit()
    return None