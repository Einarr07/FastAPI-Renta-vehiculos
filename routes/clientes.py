from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from db.conexion import session_local
from db.models.clientes import Clientes
from db.schemas.clientes import ObtenerClientes
from sqlalchemy.exc import IntegrityError


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
@router.get("/", response_model=list[ObtenerClientes])
async def obtener_clientes(db: Session = Depends(obtener_bd)):
    clientes = db.query(Clientes).all()
    return clientes

# Definir un post para registrar usuarios
@router.post("/", response_model= ObtenerClientes, status_code=status.HTTP_201_CREATED)
async def crear_cliente(entrada: ObtenerClientes, db: Session = Depends(obtener_bd)):
    cliente = Clientes(
        cedula = entrada.cedula,
        nombre = entrada.nombre,
        apellido = entrada.apellido, 
        ciudad = entrada.ciudad, 
        correo = entrada.correo, 
        direccion = entrada.direccion, 
        telefono = entrada.telefono, 
        fecha_nacimiento  = entrada.fecha_nacimiento
    )

    db.add(cliente)

    try:
        db.commit()
        db.refresh(cliente)
    except IntegrityError as e:
        error_msg = str(e)
        print(f"Error de integridad: {error_msg}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear cliente")

    return cliente

