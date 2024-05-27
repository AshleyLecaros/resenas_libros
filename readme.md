# Proyecto: Plataforma de Reseñas de Libros

Este proyecto es la creacion de una pagina web para ver y publicar reseñas de librps.

## Descripción

Desarrollar un sitio web dinámico y responsivo que facilite la gestión de reseñas de libros,
permitiendo a los usuarios escribir reseñas, calificar libros y seguir a autores. Esta
plataforma ofrecerá una experiencia de usuario fluida y adaptable en diversos dispositivos,
garantizando que los usuarios puedan interactuar de manera intuitiva y accesible.
La plataforma contará con múltiples niveles de acceso, asegurando que cada usuario
tenga funcionalidades específicas según su rol. Los usuarios tendrán la capacidad de
escribir y editar reseñas. Los administradores del sitio tendrán acceso completo.

### Prerrequisitos 📋

Lista de software y herramientas, incluyendo versiones, que necesitas para instalar y ejecutar este proyecto:

- Sistema Operativo (por ejemplo, Ubuntu 20.04, Windows 10 u otro que sea compatible)
- Lenguaje de programación Python version 3.10.10 
- pip (gestor de paquetes de Python)
- Framework Django versión 4.2.11 
- Base de Datos: PostgreSQL versión 14.11
- Editor de código (Visual Studio Code, Sublime Text, etc.)
- Bootstrap (usando el CDN)

### Empezando 🚀

Estas instrucciones te guiarán para obtener una copia de este proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

- Clonar el repositorio en tu maquina local utilizando el comando:

```bash
git clone git@github.com:AshleyLecaros/resenas_libros.git

```
- Luego de clonar el repositorio desde la carpeta contenedora del proyecto ejecuta el comando para intalar ambiente virtal:

''' python -m venv nombre_ambiente_virtual' ''  

- Activa tu ambiente virtual:

'''  source nombre_ambiente_virtual/bin/activate '''  

- Instala las dependencias del proyecto que se encuentran en el archivo requirements.txt usando pip.

''' pip install -r requirements.txt '''

- Configura la base de datos: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_basedatos',
        'USER': 'usuario_basedatos',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

- Crea la Base de datos con el mismo nombre del paso anterior:

''' createdb nombre_basedatos''' o con ''' CREATE DATABASE nombre_basedatos si es que lo haces desde Postgres

- Aplica las migraciones del proyecto: 

''' python manage.py migrate'''   si haces cambios debes correr el comando '''python manage.py makemigratios''' y luego ''' python manage.py migrate'''

- el proyecto contiene un archivo JSON (datos.json) con datos semillas puedes cargar los datos a tu base de datos con el siguiente comando: 

'''python manage.py loaddata datos.json'''

- Finalmente, inicia el servidor de desarrollo de Django y verifica que todo esté funcionando correctamente.

'''python manage.py runserver'''


## Credenciales de acceso segun tipo de usuario: 

    # Para Usuario Tipo Administrador:
      - Email: administrador@mail.com
      - contraseña: Abc123#

    # Para Usuario Tipo Lector:
      - Email: lector@mail.com
      - Contraseña: Abc123#


## Autor

Este proyecto fue creado por [Ashley Michell](https://github.com/AshleyLecaros)