from sqlalchemy import Column, Integer, String, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from ..conexion import Base

class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cedula = Column(BigInteger, ForeignKey("usuarios.id"), unique=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    ciudad = Column(String(30), nullable=False)
    correo = Column(String(50), unique=True, nullable=False)
    direccion = Column(String(150), nullable=False)
    telefono = Column(String(10), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)

    usuarios = relationship("Usuarios", back_populates="clientes")
    reservas = relationship("Reservas", back_populates="cliente")
