# Bulfon-Quevedo-Concesionario

ConcesionarioAuto es una app desarrollada con Django para gestionar una concesionaria de automóviles. Permite a los usuarios ver una lista de automóviles, detalles de cada auto, realizar comentarios, dejar reseñas y más. Los administradores del sitio pueden añadir, editar y eliminar vehículos y comentarios.

## Características

- **Lista de Automóviles**: Visualiza todos los automóviles disponibles en la concesionaria.
![List](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/main/images/img1.jpeg)
- **Detalles del Automóvil**: Ver información detallada sobre cada auto, incluyendo marca, modelo, precio y año.
![Car_Detail](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/main/images/img2.jpeg)
- **Comentarios**: Los usuarios pueden dejar comentarios sobre los automóviles.
- **Reseñas**: Los usuarios pueden dejar reseñas y calificaciones de los automóviles.
- **Autenticación**: Sistema de registro e inicio de sesión para usuarios.
![Login](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/main/images/img3.jpeg)
- **Roles de Usuario**: Diferenciación entre usuarios normales y usuarios con rol de administrador (staff).
![Register](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/main/images/img4.jpeg)
- **Gestión de Automóviles**: Los administradores pueden agregar, editar y eliminar automóviles y comentarios.
- **Carga de Imágenes**: Soporte para la carga de imágenes de los automóviles.

## Requisitos Previos

Asegúrate de tener los siguientes requisitos instalados en tu sistema:

- Python 3.6 o superior
- Django 5.0.4 o superior
- pip (Python package installer)
- Un entorno virtual de Python (recomendado)

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clona el repositorio

```bash
git clone https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario
cd Bulfon-Quevedo-Concesionario
```

### 2. Crea un entorno virtual

```bash
python3 -m venv env
```

### 3. Activa el entorno virtual

- En Windows:

  ```bash
  .\env\Scripts\activate
  ```

- En macOS y Linux:

  ```bash
  source env/bin/activate
  ```

### 4. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 5. Configura la base de datos

Aplica las migraciones para crear la base de datos SQLite:

```bash
python manage.py migrate
```

### 6. Ejecuta el script para crear datos de prueba

Si deseas comenzar con datos de prueba, puedes ejecutar el siguiente script que creará los automóviles en la base de datos:

```bash
python manage.py shell < autos/script_crear_autos.py
```

### 7. Inicia el servidor de desarrollo

```bash
python manage.py runserver
```

Visita `http://127.0.0.1:8000/` en tu navegador para acceder a la aplicación.

## Uso

### Usuarios Administradores

1. Inicia sesión en `/admin` con las credenciales de administrador para acceder al panel de administración de Django.
2. Agrega, edita o elimina automóviles y categorías desde el panel de administración.

### Usuarios Normales

1. Regístrate o inicia sesión a través de la interfaz de usuario.
2. Navega por la lista de automóviles.
3. Comenta y deja reseñas en los automóviles de tu elección.

## Estructura del Proyecto

```
concesionarioauto/
├── autos/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── car_detail.html
│   │   ├── car_form.html
│   │   ├── car_list.html
│   │   └── registration/
│   │       ├── login.html
│   │       └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── concesionarioauto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
└── db.sqlite3
```
