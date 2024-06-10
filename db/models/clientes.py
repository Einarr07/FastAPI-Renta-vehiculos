from pydantic import BaseModel
from typing import Optional

# Vista de clientes
class Clientes(BaseModel):
    id: Optional[int] = None
    cedula: int
    nombre: str
    apellido: str
    ciudad: str
    correo: str
    direccion: str
    telefono: str
    fecha_nacimiento: str

    class Config:
        orm_mode = True

# Crear clientes
class ClientesCreacion(BaseModel):
    cedula: int
    nombre: str
    apellido: str
    ciudad: str
    correo: str
    direccion: str
    telefono: str
    fecha_nacimiento: str
