from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from db.conexion import session_local
from db.models.clientes import Clientes, ClientesCreacion
from db.schemas.clientes import clientes_esquema
router = APIRouter(
    prefix="/clientes",
    tags=["clientes"],
    responses={404: {"Mensaje": "No encontrado"}}
)

def obtener_bd():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# Definir un get para obtener una lista de todos los clientes
@router.get("/", response_model=list[clientes_esquema])
async def obtener_clientes(db: Session = Depends(obtener_bd)):
    return db.query(Clientes).all()


