# Bulfon-Quevedo-Concesionario

**ConcesionarioAuto** es una aplicación desarrollada con Django para gestionar una concesionaria de automóviles. Permite a los usuarios ver una lista de automóviles, detalles de cada auto, realizar comentarios, dejar reseñas, y más. Los administradores pueden añadir, editar y eliminar vehículos y comentarios. Además, la aplicación incluye una API que permite interactuar con los datos de los automóviles y los usuarios.

## Características

- **Lista de Automóviles**: Visualiza todos los automóviles disponibles en la concesionaria.
  ![List](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/blob/main/images/img1.jpeg)
- **Detalles del Automóvil**: Ver información detallada sobre cada auto, incluyendo marca, modelo, precio y año.
  ![Car_Detail](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/blob/main/images/img2.jpeg)
- **Comentarios**: Los usuarios pueden dejar comentarios sobre los automóviles.
- **Reseñas**: Los usuarios pueden dejar reseñas y calificaciones de los automóviles.
- **Autenticación**: Sistema de registro e inicio de sesión para usuarios.
  ![Login](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/blob/main/images/img3.jpeg)
- **Roles de Usuario**: Diferenciación entre usuarios normales y usuarios con rol de administrador (staff).
  ![Register](https://github.com/quevedoagostina/Bulfon-Quevedo-Concesionario/blob/main/images/img4.jpeg)
- **Gestión de Automóviles**: Los administradores pueden agregar, editar y eliminar automóviles y comentarios.
- **Carga de Imágenes**: Soporte para la carga de imágenes de los automóviles.
- **API REST**: Acceso a la lista de automóviles, detalles de comentarios y creación de usuarios, especialmente para usuarios Staff.
- **Traducciones**: Una página permite cambiar el idioma entre español e inglés.

## Requisitos Previos

Asegúrate de tener los siguientes requisitos instalados en tu sistema:

- Python 3.6 o superior
- Django 5.0.4 o superior
- pip (Python package installer)
- Un entorno virtual de Python (recomendado)

## Instalación

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

## API REST

### Endpoints Disponibles

1. **Listado de Automóviles**
   - **URL**: `/api/cars/`
   - **Método**: `GET`
   - **Descripción**: Devuelve un listado de todos los automóviles, incluyendo información de marca y modelo.
  
2. **Comentarios de un Auto Específico**
   - **URL**: `/api/cars/<car_id>/comments/`
   - **Método**: `GET`
   - **Descripción**: Devuelve el listado de comentarios asociados a un automóvil específico.
  
3. **Crear Usuario (solo Staff)**
   - **URL**: `/api/users/create/`
   - **Método**: `POST`
   - **Descripción**: Permite a los usuarios con permisos de Staff crear nuevos usuarios.
   - **Body**: 
     ```json
     {
       "username": "new_client_user",
       "email": "newclient@example.com",
       "password": "securepassword123"
     }
     ```

### Autenticación en la API

Para crear usuarios mediante el endpoint `POST /api/users/create/`, debes autenticarte con un usuario que tenga permisos de Staff. Si estás usando autenticación basada en token o sesión, asegúrate de enviar las credenciales correspondientes en el cliente de API.

## Internacionalización

La aplicación permite cambiar el idioma a español en al menos una página seleccionada. Para probar las traducciones, asegúrate de tener los archivos `.po` y `.mo` generados en la carpeta `locale` (consulta la documentación para más detalles sobre cómo hacerlo).

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
│   ├── api_urls.py           
│   ├── apps.py                
│   ├── models.py              
│   ├── serializers.py         
│   ├── tests.py               
│   ├── urls.py                
│   └── views.py               
├── concesionarioauto/         
│   ├── __init__.py
│   ├── asgi.py                
│   ├── settings.py            
│   ├── urls.py                
│   ├── wsgi.py                
├── locale/                    
│   └── es/LC_MESSAGES/
│       ├── django.po          
│       └── django.mo          
├── images/                    
│   ├── img1.jpeg
│   ├── img2.jpeg
│   ├── img3.jpeg
│   └── img4.jpeg
├── API_DOCUMENTATION.md       
├── manage.py                  
└── db.sqlite3                
```

## Documentación de API

Para más detalles sobre la API, consulta el archivo [API_DOCUMENTATION.md](API_DOCUMENTATION.md) para ver ejemplos de cada endpoint y los datos que recibe/devuelve.

