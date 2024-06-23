from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..conexion import Base

class Vehiculos(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    marca = Column(String(20), nullable=False)
    modelo = Column(String(50), nullable=False)
    anio_fabricacion = Column(Integer, nullable=False)
    placa = Column(String(7), nullable=False, unique=True)
    color = Column(String(10), nullable=False)
    tipo_vehiculo = Column(String(30), nullable=False)
    kilometraje = Column(Integer, nullable=False)
    descripcion = Column(String(500))

    reservas = relationship("Reservas", back_populates="vehiculo")
