from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from db.conexion import session_local
from db.models.clientes import Clientes
from db.schemas.clientes import ObtenerClientes, ActualizarClientes, EliminarCliente
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/clientes",
    tags=["clientes"],
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

@router.get("/", response_model=list[ObtenerClientes], status_code=status.HTTP_200_OK)
async def obtener_clientes(db: Session = Depends(obtener_bd)):
    """
    Obtiene una lista de todos los clientes.

    Args:
        db (Session, optional): La sesión de base de datos. Defaults to Depends(obtener_bd).

    Returns:
        list[ObtenerClientes]: Lista de clientes.
    """
    clientes = db.query(Clientes).all()
    return clientes

@router.get("/{id}", response_model=ObtenerClientes, status_code=status.HTTP_200_OK)
async def id_cliente(id: int, db: Session = Depends(obtener_bd)):
    """
    Obtiene un cliente por su ID.

    Args:
        id (int): El ID del cliente a obtener.

    Returns:
        ObtenerClientes: Los detalles del cliente.
    """
    cliente = db.query(Clientes).filter_by(id=id).first()
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    
    return cliente


@router.post("/", response_model=ObtenerClientes, status_code=status.HTTP_201_CREATED)
async def crear_cliente(entrada: ObtenerClientes, db: Session = Depends(obtener_bd)):
    """
    Crea un nuevo cliente.

    Args:
        entrada (ObtenerClientes): Datos del nuevo cliente.
        db (Session, optional): La sesión de base de datos. Defaults to Depends(obtener_bd).

    Returns:
        ObtenerClientes: El cliente creado.
    """
    cliente = Clientes(
        cedula = entrada.cedula,
        nombre = entrada.nombre,
        apellido = entrada.apellido, 
        ciudad = entrada.ciudad, 
        correo = entrada.correo, 
        direccion = entrada.direccion, 
        telefono = entrada.telefono, 
        fecha_nacimiento = entrada.fecha_nacimiento
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

@router.put("/{id}", response_model=ObtenerClientes, status_code=status.HTTP_201_CREATED)
async def actualizar_cliente(id: int, entrada: ActualizarClientes, db: Session = Depends(obtener_bd)):
    """
    Actualiza los datos de un cliente existente.

    Args:
        id (int): Identificador del cliente a actualizar.
        entrada (ActualizarClientes): Nuevos datos del cliente.
        db (Session, optional): La sesión de base de datos. Defaults to Depends(obtener_bd).

    Returns:
        ObtenerClientes: El cliente actualizado.
    """
    cliente = db.query(Clientes).filter_by(id=id).first()
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    
    cliente.nombre = entrada.nombre
    cliente.apellido = entrada.apellido
    cliente.ciudad = entrada.ciudad
    cliente.direccion = entrada.direccion
    cliente.telefono = entrada.telefono
    cliente.fecha_nacimiento = entrada.fecha_nacimiento
    db.commit()
    db.refresh(cliente)
    return cliente

@router.delete("/{id}", response_model=EliminarCliente, status_code=status.HTTP_200_OK)
async def eliminar_cliente(id: int, db: Session = Depends(obtener_bd)):
    """
    Elimina un cliente existente.

    Args:
        id (int): Identificador del cliente a eliminar.
        db (Session, optional): La sesión de base de datos. Defaults to Depends(obtener_bd).

    Returns:
        EliminarCliente: Confirmación de eliminación.
    """
    cliente = db.query(Clientes).filter_by(id=id).first()
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    
    db.delete(cliente)
    db.commit()
    respuesta = EliminarCliente(mensaje="Cliente eliminado exitosamente")
    return respuesta
