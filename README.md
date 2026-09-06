# practica02-IS

Proyecto web desarrollado con Django. El proyecto Django se llama `portafolio` y contiene la aplicación `perfil`.

## Requisitos

- Git
- Python 3.8 o superior

## Clonar y ejecutar el proyecto

1. Clona el repositorio y entra en su carpeta:

	```bash
	git clone https://github.com/ulisesvina/practica02-is/
	cd practica02-IS
	```

2. Crea un entorno virtual:

	En macOS o Linux:

	```bash
	python3 -m venv .venv
	```

	En Windows:

	```powershell
	py -m venv .venv
	```

3. Activa el entorno virtual:

	En macOS o Linux:

	```bash
	source .venv/bin/activate
	```

	En Windows:

	```powershell
	.venv\Scripts\Activate.ps1
	```

4. Instala las dependencias:

	```bash
	python -m pip install -r requirements.txt
	```
5. Enciende el servidor de desarrollo:

	```bash
	python manage.py runserver
	```

6. Abre `http://127.0.0.1:8000/` en el navegador. Para detener el servidor, pulsa `Ctrl+C`.

## Diferencia entre proyecto y aplicación en Django

Un **proyecto** es la configuración completa de un sitio Django. Define, entre otras cosas, la configuración general, las URL principales y los puntos de entrada del servidor. En este caso, `portafolio` es el proyecto.

Una **aplicación** es un componente que implementa una funcionalidad concreta y reutilizable, con sus propios modelos, vistas, plantillas, archivos estáticos y migraciones. En este caso, `perfil` es una aplicación instalada dentro del proyecto `portafolio`. Un proyecto puede contener varias aplicaciones.

## Por qué no se debe subir `.venv` y para qué sirve `requirements.txt`

La carpeta `.venv` contiene una instalación local de Python: ejecutables, paquetes compilados y rutas específicas de la máquina y del sistema operativo. Subirla al repositorio aumenta innecesariamente su tamaño, puede incluir archivos incompatibles con otros sistemas y mezcla el entorno de una persona con el código fuente. Por eso `.venv` debe mantenerse fuera del repositorio mediante `.gitignore`.

`requirements.txt` resuelve el problema de compartir dependencias sin compartir toda la instalación local. Enumera los paquetes y sus versiones; otra persona puede crear su propio entorno virtual y ejecutar `python -m pip install -r requirements.txt` para instalar una configuración equivalente de forma reproducible.