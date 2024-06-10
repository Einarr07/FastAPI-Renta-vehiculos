def clientes_esquema(clientes) -> dict:
    return {
        "id": clientes["id"],
        "cedula": clientes["cedula"],
        "nombre": clientes["nombre"],
        "apellido": clientes["apellido"],
        "ciudad": clientes["ciudad"],
        "correo": clientes["correo"],
        "direccion": clientes["direccion"],
        "telefono": clientes["telefono"],
        "fecha_nacimiento":clientes["fecha_nacimiento"]
    }