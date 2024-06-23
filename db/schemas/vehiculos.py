from pydantic import BaseModel, Field
from typing import Optional

class CrearVehiculos(BaseModel):
    id: Optional[int] = None
    marca: str
    modelo: str
    anio_fabricacion: str = Field(..., min_length=4, max_length=4)
    placa: str
    color: str
    tipo_vehiculo: str
    kilometraje: str = Field(..., min_length=1,max_length=6)
    descripcion: str

    class Config:
        from_attributes = True

class ObtenerVehiculo(BaseModel):
    id: int
    marca: str
    modelo: str
    anio_fabricacion: int
    placa: str
    color: str
    tipo_vehiculo: str
    kilometraje: int
    descripcion: str

class ActualizarVehiculo(BaseModel):
    marca: str
    modelo: str
    anio_fabricacion: str = Field(..., min_length=4, max_length=4)
    placa: str
    color: str
    tipo_vehiculo: str
    kilometraje: str = Field(..., min_length=1,max_length=6)
    descripcion: str

    class Config:
        from_attributes = True

class EliminarVehiculo(BaseModel):
    mensaje: str
