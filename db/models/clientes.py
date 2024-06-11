from sqlalchemy import Column, Integer, String
from ..conexion import Base

# Vista de clientes
class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cedula = Column(String(11), unique=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    ciudad = Column(String(30), nullable=False)
    correo = Column(String(255), unique=True, nullable=False)
    direccion = Column(String(20), nullable=False)
    telefono = Column(String(10), nullable=False)
    fecha_nacimiento = Column(String(20), nullable=False)
