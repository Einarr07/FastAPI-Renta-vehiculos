from pydantic import BaseModel
from typing import Optional

class ObtenerUsuarios(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellido: str
    correo: str
    contraseña: str