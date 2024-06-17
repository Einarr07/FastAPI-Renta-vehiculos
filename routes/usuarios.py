from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from db.conexion import session_local
from db.schemas.usuarios import ObtenerUsuarios, CrearUsuarios
from db.models.usuarios import Usuarios
from passlib.context import CryptContext

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"Mensaje": "No encontrado"}}
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def obtener_bd():
    """
    Función de utilidad para obtener una sesión de base de datos.

    Returns:
        Session: Una sesión de base de datos.
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def encriptar_contraseña(contraseña: str) -> str:
    """
    Encripta la contraseña utilizando bcrypt.

    Args:
        contraseña (str): La contraseña en texto plano.

    Returns:
        str: La contraseña encriptada.
    """
    return pwd_context.hash(contraseña)

@router.post("/", response_model=ObtenerUsuarios, status_code=status.HTTP_201_CREATED)
async def crear_usuario(entrada: CrearUsuarios, db: Session = Depends(obtener_bd)):
    usuario = Usuarios(
        id=entrada.id,
        nombre=entrada.nombre,
        apellido=entrada.apellido,
        correo=entrada.correo,
        contraseña=encriptar_contraseña(entrada.contraseña)
    )

    db.add(usuario)

    try:
        db.commit()
        db.refresh(usuario)
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear usuario")
    
    return usuario

@router.get("/", response_model=list[ObtenerUsuarios], status_code=status.HTTP_200_OK)
async def obtener_usuarios(db: Session = Depends(obtener_bd)):
    usuarios = db.query(Usuarios).all()
    return usuarios

@router.get("/{id}", response_model=ObtenerUsuarios, status_code=status.HTTP_200_OK)
async def id_usuarios(id: int, db: Session = Depends(obtener_bd)):
    usuario = db.query(Usuarios).filter_by(id=id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    return usuario
