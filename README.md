# Repositorio Estandar en Django
Este repositorio está diseñado construido para realizar un rápido despliegue en Render.com o servidor local con plantillas fundamentales y escenciales para todo proyecto, con UI de Bootsrap 5 y diseño flexible.

## Tabla de contenido
- [Repositorio Estandar en Django](#repositorio-estandar-en-django)
  - [Tabla de contenido](#tabla-de-contenido)
    - [Requisitos](#requisitos)
    - [Objetivo](#objetivo)
    - [¿Qué contiene?](#qué-contiene)
      - [Problemas que contiene](#problemas-que-contiene)
    - [Instrucciones para instalación y puesta en marcha](#instrucciones-para-instalación-y-puesta-en-marcha)

### Requisitos
- Requiere Poetry
  - A través de Poetry se instalan todas las dependencias y se ejecuta la puesta en marcha local.
  - Para instalar [haga click acá [Instalación Poetry]](https://python-poetry.org/docs/#installation)

### Objetivo
- Preparado para ser desplegado rápidamente en Render.com o servidor local.

### ¿Qué contiene?
- Sistema de registro y autenticación
- Diseño con Bootstrap 5
- Plantillas generales
  - Pagina principal
  - Página de login (funciona)
  - Página de registro (funciona)
  - Página de "mi cuenta"
  - Página de cambio de contraseña (funciona)

#### Problemas que contiene
- Página de login
  - Cuando alguno de los campos no es correcto (usuario/contraseña) el frontend no lo indica de manera explítica, pero si funciona el sistema de logueo. Es solo frontend.
- Página de registro
  - Inverso al punto anterior, si funciona cuando una cuenta nueva se quiere registrar y hay fallas en campos del formulario
- Página de cambio de contraseña
  - Cuando se cambia la contraseña, no envia mensaje de éxito

### Instrucciones para instalación y puesta en marcha
1. Clonar el repositorio
   ```bash
   git clone https://github.com/pablofontaine/Standard-Django-template.git
   ```
2. Elegir el nombre del proyecto
   - **No debe contener espacios vacios:**
     - Correcto: "nombre_del_proyecto"
     - Incorrecto: "nombre del proyecto"
   - **Preferentemente utilizar minúsculas**
     - Adecuado: "nombre_del_proyecto"
     - Inadecuado: "Nombre_Del_Proyecto"

3. Renombrar carpetas, configuraciones y/o variables.
   > ¡ADVERTENCIA! Este paso es muy importante, de lo contrario no funcionará.
   1. Capeta "standard_django_template" --> "nombre_del_proyecto"
   2. Reemplazar TODAS las variables dentro del repositorio que mencionen "standard_django_template" por "nombre_del_proyecto".
   > Visual Studio Code y otros editores de código permiten realizar esto de manera masiva. Es recomendable hacerlo de esta manera para evitar que falten lugares donde cambiar.

   > En Visual Studio Code (Linux) presiona Ctrl+Shift+F y reemplaza.

4. Elimina "poetry.lock" y "pyproject.toml"
   ```bash
   rm ./poetry.lock
   rm ./pyproject.toml
   ```
5. Inicia nuevamente Poetry y completa los campos personalizados (Package name, version, description, author, license, compatibilities, etc.)
   ```bash
    poetry init
   ```
   1. Responde NO a las siguientes preguntas:
      ```
      Would you like to define your main dependencies interactively? no
      Would you like to define your development dependencies interactively? no
      ```
6. Dirigete al archivo "pyproject.toml" recién creado y cambia:
   ```toml
   [tool.poetry.dependencies]
   python = "^3.10"
   ```
   por lo siguiente:
   ```toml
   [tool.poetry.dependencies]
   python = "^3.11"
   django = "^5.0"
   dj-database-url = "^2.1.0"
   psycopg2-binary = "^2.9.9"
   whitenoise = {extras = ["brotli"], version = "^6.6.0"}
   gunicorn = "^21.2.0"
   ```
7. Instala las dependencias.
   ```bash
   poetry install
   ```
    > Esto re-creará el archivo poetry.lock
8. Inicia el entorno virtual, haz las migraciones, crea un superusuario e inicia servidor
   ```bash
   poetry shell
   ```
   ```bash
   poetry run ./manage.py migrate
   ```
   ```bash
   poetry run ./manage.py createsuperuser
   ```
   ```bash
   poetry run ./manage.py runserver
   ```
