from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from typing import Annotated

# Credenciales de tu PostgreSQL local
usuario_db = "postgres"
password_db = "1234.admin"
host_db = "localhost"
puerto_db = "5432"
nombre_bd = "nombre_pro_clientes" 

# URL de conexión armada para PostgreSQL
url_bd = f"postgresql://{usuario_db}:{password_db}@{host_db}:{puerto_db}/{nombre_bd}"

# Motor para PostgreSQL (ya no necesita el check_same_thread de SQLite)
motor_bd = create_engine(url_bd)

def crear_tablas(app):
    SQLModel.metadata.create_all(motor_bd)
    yield

def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion

Session_dependencia = Annotated[Session, Depends(obtener_sesion)]