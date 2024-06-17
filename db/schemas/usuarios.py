from pydantic import BaseModel, Field, EmailStr


class CrearUsuarios(BaseModel):
    id: str = Field(..., min_length=10, max_length=10)
    nombre: str
    apellido: str
    correo: EmailStr
    contraseña: str

class ObtenerUsuarios(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str

    class Config:
        from_attributes = True

class CredencialesUsuario(BaseModel):
    correo: EmailStr = Field(..., min_length=1)
    contraseña: str = Field(..., min_length=1)
