# Documentación de la API

Esta API permite interactuar con el sistema de concesionaria para realizar operaciones en automóviles, comentarios y usuarios. Los endpoints están organizados para ofrecer acceso a información detallada de los automóviles, sus comentarios y permitir la creación de usuarios (exclusivo para Staff).

## Endpoints Disponibles

### 1. Listado de Automóviles
**URL**: `/api/cars/`  
**Método**: `GET`  
**Descripción**: Obtiene un listado de todos los automóviles registrados en el sistema, incluyendo datos anidados de la marca y modelo.

#### Ejemplo de Respuesta
```json
[
  {
    "id": 1,
    "model": {
      "id": 1,
      "name": "Modelo X",
      "brand": {
        "id": 1,
        "name": "Marca Y"
      }
    },
    "category": {
      "id": 1,
      "name": "SUV",
      "description": "Vehículo deportivo utilitario"
    },
    "year": 2020,
    "price": "30000.00",
    "image": "/media/cars/car1.jpg",
    "description": "Automóvil en excelentes condiciones"
  },
  ...
]
```

### 2. Comentarios de un Auto Específico
**URL**: `/api/cars/<car_id>/comments/`  
**Método**: `GET`  
**Descripción**: Obtiene un listado de los comentarios de un automóvil específico. El parámetro `car_id` representa el ID del automóvil.

#### Ejemplo de Respuesta
```json
[
  {
    "id": 1,
    "car": 1,
    "user": 2,
    "content": "Excelente auto, muy cómodo y económico.",
    "created_at": "2024-10-01T12:34:56Z",
    "updated_at": "2024-10-02T15:45:12Z"
  },
  ...
]
```

### 3. Crear Usuario (solo Staff)
**URL**: `/api/users/create/`  
**Método**: `POST`  
**Descripción**: Permite a los usuarios con permisos de Staff crear nuevos usuarios en el sistema. Solo los usuarios autenticados con rol de Staff pueden acceder a este endpoint.

#### Cuerpo de la Solicitud (Body)
```json
{
  "username": "new_client_user",
  "email": "newclient@example.com",
  "password": "securepassword123"
}
```

#### Ejemplo de Respuesta
```json
{
  "id": 123,
  "username": "new_client_user",
  "email": "newclient@example.com"
}
```

### Notas Importantes

- **Autenticación**: Para acceder al endpoint de creación de usuarios, es necesario autenticarse como un usuario Staff. Este endpoint no está disponible para usuarios sin permisos especiales.
- **Errores Comunes**:
  - `403 Forbidden`: Aparece cuando un usuario no Staff intenta crear un nuevo usuario.
  - `404 Not Found`: Aparece cuando se intenta acceder a comentarios de un automóvil que no existe.