# Plan de Mejoramiento Actualizado

Proyecto académico desarrollado en el marco de la formación del **SENA**. Consiste en una API REST construida con **FastAPI** para la gestión de usuarios, órdenes e ítems de orden, utilizando **SQLModel** como ORM sobre una base de datos SQLite.

## 📋 Descripción

Esta API permite administrar el ciclo completo de información de un sistema de órdenes:

- **Usuarios**: registro y administración de las personas que generan órdenes.
- **Órdenes**: creación y gestión de órdenes asociadas a un usuario, con cálculo automático del total.
- **Ítems de orden**: productos o conceptos individuales que componen cada orden.

## 🛠️ Tecnologías utilizadas

- [Python 3.14](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) — framework para construir la API
- [SQLModel](https://sqlmodel.tiangolo.com/) — ORM basado en Pydantic y SQLAlchemy
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI para correr la aplicación
- SQLite — base de datos

## 📁 Estructura del proyecto

```
nombre-pro-clientes/
├── app/
│   ├── main.py                  # Punto de entrada de la aplicación
│   ├── conexion_bd.py           # Configuración de la conexión a la base de datos
│   ├── enrutadores/             # Rutas / endpoints de la API
│   │   ├── usuarios.py
│   │   ├── ordenes.py
│   │   └── items_orden.py
│   └── modelos/                 # Modelos de datos (SQLModel)
│       ├── usuarios.py
│       ├── ordenes.py
│       └── items_orden.py
├── requeriments.txt             # Dependencias del proyecto
└── README.md
```

## 🚀 Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/juan3625/recuperacion_nombre-pro-clientes.git
   cd recuperacion_nombre-pro-clientes
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # En Windows con Git Bash
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requeriments.txt
   ```

4. Ejecuta el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Abre en tu navegador la documentación interactiva de la API:
   ```
   http://127.0.0.1:8000/docs
   ```

## 📌 Endpoints principales

| Recurso  | Método | Ruta                     | Descripción                          |
|----------|--------|--------------------------|---------------------------------------|
| Usuarios | GET    | `/usuarios`              | Listar todos los usuarios             |
| Usuarios | GET    | `/usuarios/{id}`         | Obtener un usuario por ID             |
| Usuarios | POST   | `/usuarios`              | Crear un nuevo usuario                |
| Usuarios | PATCH  | `/usuarios/{id}`         | Actualizar un usuario                 |
| Usuarios | DELETE | `/usuarios/{id}`         | Eliminar un usuario                   |
| Órdenes  | GET    | `/ordenes`                | Listar todas las órdenes              |
| Órdenes  | GET    | `/ordenes/{id}`           | Obtener una orden con sus ítems       |
| Órdenes  | POST   | `/ordenes/{usuario_id}`   | Crear una orden para un usuario       |
| Órdenes  | PATCH  | `/ordenes/{id}`           | Actualizar una orden                  |
| Órdenes  | DELETE | `/ordenes/{id}`           | Eliminar una orden                    |
| Ítems    | GET    | `/items`                  | Listar todos los ítems                |
| Ítems    | GET    | `/items/{id}`             | Obtener un ítem por ID                |
| Ítems    | POST   | `/items/{orden_id}`       | Crear un ítem dentro de una orden     |
| Ítems    | PATCH  | `/items/{id}`             | Actualizar un ítem                    |
| Ítems    | DELETE | `/items/{id}`             | Eliminar un ítem                      |

## 👤 Autor

Proyecto desarrollado por **Yeimy Padilla** como parte del proceso de formación del SENA — Plan de Mejoramiento.
