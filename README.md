# Renta de vehiculos con FastAPI y MySQL

## Crear un entorno virtual

Para la creación de un entorno virtual deberemos tener Python previamente instalado y ejecutar el siguiente comando:

```bash
virtualenv -p python env
```

Una vez hayamos creado nuestro entorno virtual nos moveremos dentro de este con el siguiente comando:

```bash
.\env\Scripts\activate
```

Cuando ya nos encontremos dentro de este podremos instalar todas las bibliotecas que vayamos a necesitar en nuestro proyecto
y crearemos un archivo requirements.txt donde se encontrarán todas las dependencias de nuestro proyecto.
Para crearlo necesitaremos el siguiente comando:

```bash
pip freeze > requirements.txt
```

Y en caso de que necesitemos instalar las dependencias de otro entorno virtual lo haremos mediante el siguiente comando:

```bash
pip install -r requirements.txt
```

Finalmente, para salir del entorno virtual que hemos creado utilizaremos 

```bash
deactivate
```
## Activación del servidor 

Para poder utilizar FastAPI necesitaremos un servidor ASGI (Asynchronous Server Gateway Interface), el cual es
una especificación para servidores web y frameworks web en  Python que permite la comunicación asincrónica entre 
servidores web y aplicaciones web.

```bash
pip install "uvicorn[standard]"
```

para correr el servidor deberemos ingresar el siguiente comando:

```bash
uvicorn main:app --reload
```


