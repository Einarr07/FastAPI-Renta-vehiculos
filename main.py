from fastapi import FastAPI
from db.conexion import Base, engine, session_local
from starlette.responses import RedirectResponse
from routes import clientes, usuarios, auth_usuarios, vehiculos, reservas

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    responses={404: {"Mensaje": "No encontrado"}}
)

# Routers
app.include_router(clientes.router)
app.include_router(usuarios.router)
app.include_router(auth_usuarios.router)
app.include_router(vehiculos.router)
app.include_router(reservas.router)

@app.get("/")
def main():
    """
    Redirecciona al usuario a la documentación de la API.

    Returns:
        RedirectResponse: Redirecciona al usuario a la documentación.
    """
    return RedirectResponse(url="/docs/")
