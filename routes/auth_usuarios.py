from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.conexion import session_local
from db.models.usuarios import Usuarios
from db.schemas.usuarios import CredencialesUsuario
from passlib.context import CryptContext

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"Mensaje": "No encontrado"}}
)


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

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_contraseña(contraseña_plana: str, contraseña_encriptada: str) -> bool:
    """
    Verifica si la contraseña en texto plano coincide con la contraseña encriptada.

    Args:
        contraseña_plana (str): La contraseña en texto plano ingresada por el usuario.
        contraseña_encriptada (str): La contraseña encriptada almacenada en la base de datos.

    Returns:
        bool: True si las contraseñas coinciden, False en caso contrario.
    """
    return pwd_context.verify(contraseña_plana, contraseña_encriptada)

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(credenciales: CredencialesUsuario, db: Session = Depends(obtener_bd)):
    """
    Autentica a un usuario utilizando su correo y contraseña.

    Args:
        credenciales (CredencialesUsuario): El correo y la contraseña del usuario.

    Returns:
        dict: Un mensaje de éxito o error.
    """
    usuario = db.query(Usuarios).filter(Usuarios.correo == credenciales.correo).first()
    
    if not usuario or not verificar_contraseña(credenciales.contraseña, usuario.contraseña):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"mensaje": "Inicio de sesión exitoso"}
