from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.conexion import session_local
from db.models.vehiculos import Vehiculos
from db.schemas.vehiculos import CrearVehiculos, ObtenerVehiculo, ActualizarVehiculo, EliminarVehiculo

router = APIRouter(
    prefix="/vehiculos",
    tags=["vehiculos"],
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

@router.post("/", response_model=ObtenerVehiculo, status_code=status.HTTP_201_CREATED)
async def crear_vehiculo(entrada: CrearVehiculos, db: Session = Depends(obtener_bd)):
    vehiculo = Vehiculos(
        marca=entrada.marca,
        modelo=entrada.modelo,
        anio_fabricacion=entrada.anio_fabricacion,
        placa=entrada.placa,
        color=entrada.color,
        tipo_vehiculo=entrada.tipo_vehiculo,
        kilometraje=entrada.kilometraje,
        descripcion=entrada.descripcion
    )

    db.add(vehiculo)

    try:
        db.commit()
        db.refresh(vehiculo)
    except IntegrityError as e:
        error_msg = str(e)
        print(f"Error de integridad: {error_msg}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear vehiculo")
    
    return vehiculo

@router.get("/", response_model=list[ObtenerVehiculo], status_code=status.HTTP_200_OK)
async def obtener_vehiculos(db: Session = Depends(obtener_bd)):
    vehiculos = db.query(Vehiculos).all()
    return vehiculos

@router.get("/{placa}", response_model=ObtenerVehiculo, status_code=status.HTTP_200_OK)
async def placas_vehiculo(placa: str, db: Session = Depends(obtener_bd)):
    vehiculo = db.query(Vehiculos).filter_by(placa=placa).first()
    if not vehiculo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    
    return vehiculo

@router.put("/{id}", response_model=ObtenerVehiculo, status_code=status.HTTP_202_ACCEPTED)
async def actualizar_vehiculo(id: int, entrada: ActualizarVehiculo, db: Session=Depends(obtener_bd)):
    vehiculo = db.query(Vehiculos).filter_by(id=id).first()
    if not vehiculo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehiculo no encontrado")
    
    
    vehiculo.marca=entrada.marca
    vehiculo.modelo=entrada.modelo
    vehiculo.anio_fabricacion=entrada.anio_fabricacion
    vehiculo.placa=entrada.placa
    vehiculo.color=entrada.color
    vehiculo.tipo_vehiculo=entrada.tipo_vehiculo
    vehiculo.kilometraje=entrada.kilometraje
    vehiculo.descripcion=entrada.descripcion

    db.commit()   
    db.refresh(vehiculo)
    return vehiculo

@router.delete("/{id}", response_model=EliminarVehiculo, status_code=status.HTTP_200_OK)
async def eliminar_vehiculo(id: int, db: Session = Depends(obtener_bd)):
    vehiculo = db.query(Vehiculos).filter_by(id=id).first()
    if not vehiculo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    db.delete(vehiculo)
    db.commit()
    respuesta = EliminarVehiculo(mensaje="Vehículo eliminado exitosamente")
    return respuesta