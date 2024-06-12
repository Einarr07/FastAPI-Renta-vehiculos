from fastapi import FastAPI
from db.conexion import Base, engine, session_local
from starlette.responses import RedirectResponse
from routes import clientes

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    responses={404: {"Mensaje": "No encontrado"}}
)

# Routers
app.include_router(clientes.router)

# Dependencia para obtener la sesión de base de datos
def obtener_bd():
    """
    Función de utilidad para obtener una sesión de base de datos.

    Returns:
        Session: Una sesión de base de datos.
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    """
    Redirecciona al usuario a la documentación de la API.

    Returns:
        RedirectResponse: Redirecciona al usuario a la documentación.
    """
    return RedirectResponse(url="/docs/")
