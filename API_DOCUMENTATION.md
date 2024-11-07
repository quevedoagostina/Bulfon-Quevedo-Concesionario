# Documentación de la API

Esta API permite interactuar con el sistema de concesionaria para realizar operaciones en automóviles, comentarios y usuarios. Los endpoints están organizados para ofrecer acceso a información detallada de los automóviles, sus comentarios y permitir la creación de usuarios (exclusivo para Staff).

### Endpoints de la API

A continuación se presentan los endpoints de la API con ejemplos en **Postman** y **curl** para cada acción.

---

### 1. Listar todos los autos
- **URL**: `/api/cars/`
- **Método**: `GET`

**Postman**:
1. Selecciona `GET` en el método HTTP.
2. Ingresa la URL: `http://127.0.0.1:8000/api/cars/`
3. Haz clic en `Send`.

**curl**:
```bash
curl -X GET http://127.0.0.1:8000/api/cars/
```

---

### 2. Crear un auto
- **URL**: `/api/cars/`
- **Método**: `POST`

**Postman**:
1. Selecciona `POST`.
2. URL: `http://127.0.0.1:8000/api/cars/`.
3. En `Body`, selecciona `form-data`.
4. Añade los siguientes campos:

   | Key         | Value                | Type |
   |-------------|----------------------|------|
   | model       | 1                    | Text |
   | category    | 1                    | Text |
   | year        | 2020                 | Text |
   | price       | 30000.00             | Text |
   | image       | (archivo de imagen)  | File |
   | description | Auto nuevo           | Text |

5. Haz clic en `Send`.

**curl**:
```bash
curl -X POST http://127.0.0.1:8000/api/cars/ \
  -F "model=1" \
  -F "category=1" \
  -F "year=2020" \
  -F "price=30000.00" \
  -F "image=@/path/to/image.jpg" \
  -F "description=Auto nuevo"
```

---

### 3. Obtener detalles de un auto específico
- **URL**: `/api/cars/324/`
- **Método**: `GET`

**Postman**:
1. Selecciona `GET`.
2. URL: `http://127.0.0.1:8000/api/cars/324/`.
3. Haz clic en `Send`.

**curl**:
```bash
curl -X GET http://127.0.0.1:8000/api/cars/324/
```

---

### 4. Actualizar un auto específico
- **URL**: `/api/cars/324/`
- **Método**: `PUT`

**Postman**:
1. Selecciona `PUT`.
2. URL: `http://127.0.0.1:8000/api/cars/324/`.
3. En `Body`, selecciona `raw` y elige `JSON`.
4. Ingresa el siguiente JSON:

   ```json
   {
     "model": 1,
     "category": 1,
     "year": 2021,
     "price": 32000.00,
     "description": "Descripción actualizada del auto"
   }
   ```

5. Haz clic en `Send`.

**curl**:
```bash
curl -X PUT http://127.0.0.1:8000/api/cars/324/ \
  -H "Content-Type: application/json" \
  -d '{
        "model": 1,
        "category": 1,
        "year": 2021,
        "price": 32000.00,
        "description": "Descripción actualizada del auto"
      }'
```

---

### 5. Eliminar un auto específico
- **URL**: `/api/cars/324/`
- **Método**: `DELETE`

**Postman**:
1. Selecciona `DELETE`.
2. URL: `http://127.0.0.1:8000/api/cars/324/`.
3. Haz clic en `Send`.

**curl**:
```bash
curl -X DELETE http://127.0.0.1:8000/api/cars/324/
```

---

### 6. Crear un comentario
- **URL**: `/api/comments/`
- **Método**: `POST`

**Postman**:
1. Selecciona `POST`.
2. URL: `http://127.0.0.1:8000/api/comments/`.
3. En `Body`, selecciona `raw` y elige `JSON`.
4. Ingresa el siguiente JSON:

   ```json
   {
     "car": 324,
     "user": 2,
     "content": "Excelente auto, lo recomiendo."
   }
   ```

5. Haz clic en `Send`.

**curl**:
```bash
curl -X POST http://127.0.0.1:8000/api/comments/ \
  -H "Content-Type: application/json" \
  -d '{
        "car": 324,
        "user": 2,
        "content": "Excelente auto, lo recomiendo."
      }'
```

---

### 7. Obtener detalles de un comentario específico
- **URL**: `/api/comments/1/`
- **Método**: `GET`

**Postman**:
1. Selecciona `GET`.
2. URL: `http://127.0.0.1:8000/api/comments/1/`.
3. Haz clic en `Send`.

**curl**:
```bash
curl -X GET http://127.0.0.1:8000/api/comments/1/
```

---

### 8. Actualizar un comentario específico
- **URL**: `/api/comments/1/`
- **Método**: `PUT`

**Postman**:
1. Selecciona `PUT`.
2. URL: `http://127.0.0.1:8000/api/comments/1/`.
3. En `Body`, selecciona `raw` y elige `JSON`.
4. Ingresa el siguiente JSON:

   ```json
   {
     "car": 324,
     "user": 2,
     "content": "Comentario actualizado sobre el auto."
   }
   ```

5. Haz clic en `Send`.

**curl**:
```bash
curl -X PUT http://127.0.0.1:8000/api/comments/1/ \
  -H "Content-Type: application/json" \
  -d '{
        "car": 324,
        "user": 2,
        "content": "Comentario actualizado sobre el auto."
      }'
```

---

### 9. Eliminar un comentario específico
- **URL**: `/api/comments/1/`
- **Método**: `DELETE`

**Postman**:
1. Selecciona `DELETE`.
2. URL: `http://127.0.0.1:8000/api/comments/1/`.
3. Haz clic en `Send`.

**curl**:
```bash
curl -X DELETE http://127.0.0.1:8000/api/comments/1/
```

---

### 10. Listar comentarios de un auto específico
- **URL**: `/api/cars/324/comments/`
- **Método**: `GET`

**Postman**:
1. Selecciona `GET`.
2. URL: `http://127.0.0.1:8000/api/cars/324/comments/`.
3. Haz clic en `Send`.

**curl**:
```bash
curl -X GET http://127.0.0.1:8000/api/cars/324/comments/
```

---

### 11. Crear Usuario (solo Staff)
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
