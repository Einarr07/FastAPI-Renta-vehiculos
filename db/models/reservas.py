from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..conexion import Base

class Reservas(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo = Column(Integer, unique=True)
    descripcion = Column(String(500))
    id_cliente = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    id_vehiculo = Column(Integer, ForeignKey("vehiculos.id"), nullable=False)

    cliente = relationship("Clientes", back_populates="reservas")
    vehiculo = relationship("Vehiculos", back_populates="reservas")
