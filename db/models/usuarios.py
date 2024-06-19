from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from ..conexion import Base

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    correo = Column(String(50), unique=True, nullable=False)
    contraseña = Column(String(100), nullable=False)

    clientes = relationship("Clientes", back_populates="usuarios")