from sqlalchemy import Column, Integer, String, Date
from ..conexion import Base

# Vista de clientes
class Clientes(Base):
    """
    Modelo de SQLAlchemy para la tabla de clientes.

    Attributes:
        id (int): Identificador único de cada cliente (clave primaria).
        cedula (str): Número de cédula del cliente, único y no nulo.
        nombre (str): Nombre del cliente, no nulo.
        apellido (str): Apellido del cliente, no nulo.
        ciudad (str): Ciudad de residencia del cliente, no nulo.
        correo (str): Dirección de correo electrónico del cliente, única y no nula.
        direccion (str): Dirección de residencia del cliente, no nula.
        telefono (str): Número de teléfono del cliente, no nulo.
        fecha_nacimiento (Date): Fecha de nacimiento del cliente, no nula.
    """

    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cedula = Column(String(10), unique=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    ciudad = Column(String(30), nullable=False)
    correo = Column(String(50), unique=True, nullable=False)
    direccion = Column(String(150), nullable=False)
    telefono = Column(String(10), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)