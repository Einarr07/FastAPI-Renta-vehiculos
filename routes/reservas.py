from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from db.conexion import session_local
from db.models.reservas import Reservas
from db.schemas.reservas import ObtenerReservas, CrearReservas, ActualizarReserva, EliminarReserva
from db.models.clientes import Clientes
from db.models.vehiculos import Vehiculos

router = APIRouter(
    prefix="/reservas",
    tags=["reservas"],
    responses={404: {"Mensaje": "No encontrado"}}
)

def obtener_bd():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ObtenerReservas, status_code=status.HTTP_201_CREATED)
async def crear_reserva(entrada: CrearReservas, db: Session = Depends(obtener_bd)):
    cliente_existente = db.query(Clientes).filter_by(id=entrada.id_cliente).first()
    vehiculo_existente = db.query(Vehiculos).filter_by(id=entrada.id_vehiculo).first()

    if not cliente_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El id del cliente no existe")
    if not vehiculo_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El id del vehiculo no existe")

    reserva = Reservas(
        codigo=entrada.codigo,
        descripcion=entrada.descripcion,
        id_cliente=entrada.id_cliente,
        id_vehiculo=entrada.id_vehiculo
    )

    db.add(reserva)

    try:
        db.commit()
        db.refresh(reserva)
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear una reserva")
    
    return reserva

@router.get("/", response_model=list[ObtenerReservas], status_code=status.HTTP_200_OK)
async def obtener_reservas(db: Session = Depends(obtener_bd)):
    reservas = db.query(Reservas).all()
    return reservas

@router.get("/{id}", response_model=ObtenerReservas, status_code=status.HTTP_200_OK)
async def id_reservas(id: int, db: Session = Depends(obtener_bd)):
    reserva = db.query(Reservas).filter_by(id=id).first()
    if not reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva no encontrada")
    
    return reserva

@router.put("/{codigo}", response_model=ObtenerReservas, status_code=status.HTTP_200_OK)
async def actualizar_reservas(codigo: int, entrada: ActualizarReserva, db: Session=Depends(obtener_bd)):
    reserva = db.query(Reservas).filter_by(codigo=codigo).first()
    if not reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Código no existente")
    
    reserva.descripcion = entrada.descripcion
    reserva.id_cliente = entrada.id_cliente
    reserva.id_vehiculo = entrada.id_vehiculo

    db.commit()
    db.refresh(reserva)
    
    return reserva

@router.delete("/{id}", response_model=EliminarReserva, status_code=status.HTTP_200_OK)
async def eliminar_reserva(id: int, db: Session=Depends(obtener_bd)):
    reserva = db.query(Reservas).filter_by(id=id).first()
    if not reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    db.delete(reserva)
    db.commit()
    respuesta = EliminarReserva(mensaje="Reserva eliminada exitosamente")
    return respuesta