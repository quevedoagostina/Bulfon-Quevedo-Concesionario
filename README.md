# Bulfon-Quevedo-Concesionario

ConcesionarioAuto es una aplicación desarrollada con Django para gestionar una concesionaria de automóviles. Permite a los usuarios ver una lista de automóviles, detalles de cada auto, realizar comentarios y más. Los administradores del sitio pueden añadir, editar y eliminar vehículos y comentarios.

## Características

- **Lista de Automóviles**: Visualiza todos los automóviles disponibles en la concesionaria.
- **Detalles del Automóvil**: Ver información detallada sobre cada auto, incluyendo marca, modelo, precio y año.
- **Comentarios**: Los usuarios pueden dejar comentarios sobre los automóviles.
- **Autenticación**: Sistema de registro e inicio de sesión para usuarios.
- **Roles de Usuario**: Diferenciación entre usuarios normales y usuarios con rol de administrador (staff).
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
pip install django
```

```bash
pip -m pip install Pillow
```

### 5. Configura la base de datos

Aplica las migraciones para crear la base de datos SQLite:

```bash
python manage.py migrate
```

### 6. Carga datos de prueba (opcional)S

Si deseas comenzar con datos de prueba, puedes usar fixtures o scripts para cargar datos:

```bash
python manage.py loaddata datos_de_prueba.json
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
3. Comenta en los automóviles de tu elección.

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
