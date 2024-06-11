from pydantic import BaseModel
from typing import Optional

class ObtenerClientes(BaseModel):
    id: Optional[int] = None
    cedula: str
    nombre: str
    apellido: str 
    ciudad: str 
    correo: str 
    direccion: str 
    telefono: str 
    fecha_nacimiento : str

    class Config:
        from_attributes = True

class ActualizarClientes(BaseModel):
    nombre: str
    apellido: str 
    ciudad: str 
    direccion: str 
    telefono: str 
    fecha_nacimiento : str