from pydantic import BaseModel, Field

class ObtenerReservas(BaseModel):
    id: int
    codigo: int
    descripcion: str
    id_cliente: int
    id_vehiculo: int

class CrearReservas(BaseModel):
    codigo: str
    descripcion: str
    id_cliente: str 
    id_vehiculo: str 

    class Config:
        from_attributes = True

class ActualizarReserva(BaseModel):
    descripcion: str
    id_cliente: str
    id_vehiculo: str

class EliminarReserva(BaseModel):
    mensaje: str
