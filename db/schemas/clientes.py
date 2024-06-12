from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime, date

class ObtenerClientes(BaseModel):
    """
    Modelo Pydantic para obtener información de clientes.

    Attributes:
        id (Optional[int]): Identificador único de cada cliente.
        cedula (str): Número de cédula del cliente.
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
        ciudad (str): Ciudad de residencia del cliente.
        correo (str): Dirección de correo electrónico del cliente.
        direccion (str): Dirección de residencia del cliente.
        telefono (str): Número de teléfono del cliente.
        fecha_nacimiento (date): Fecha de nacimiento del cliente.
    """

    id: Optional[int] = None
    cedula: str = Field(..., min_length=11, max_length=20)
    nombre: str
    apellido: str 
    ciudad: str 
    correo: str 
    direccion: str 
    telefono: str 
    fecha_nacimiento: date

    @validator("fecha_nacimiento", pre=True, always=True)
    def analizar_fecha(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%d-%m-%Y").date()
        return value
    
    @validator("cedula")
    def longitud_cedula(cls, validar_cedula):
        return validar_cedula

    class Config:
        from_attributes = True

class ActualizarClientes(BaseModel):
    """
    Modelo Pydantic para actualizar información de clientes.

    Attributes:
        nombre (str): Nuevo nombre del cliente.
        apellido (str): Nuevo apellido del cliente.
        ciudad (str): Nueva ciudad de residencia del cliente.
        direccion (str): Nueva dirección de residencia del cliente.
        telefono (str): Nuevo número de teléfono del cliente.
        fecha_nacimiento (date): Nueva fecha de nacimiento del cliente.
    """

    nombre: str
    apellido: str 
    ciudad: str 
    direccion: str 
    telefono: str 
    fecha_nacimiento: date

    @validator("fecha_nacimiento", pre=True, always=True)
    def analizar_fecha(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%d-%m-%Y").date()
        return value
    
    class Config:
        from_attributes = True

class EliminarCliente(BaseModel):
    """
    Modelo Pydantic para eliminar un cliente.

    Attributes:
        mensaje (str): Mensaje de confirmación de eliminación.
    """

    mensaje: str
