from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class UsuarioEstructura(SQLModel):
    nombres: str = Field(default=None)
    correo: str = Field(default=None)
    detalle: Optional[str] = Field(default=None)

class IngresarUsuario(UsuarioEstructura):
    pass

class ActualizarUsuario(UsuarioEstructura):
    pass

class Usuario(UsuarioEstructura, table=True):
    __tablename__ = "usuarios"
    id: Optional[int] = Field(default=None, primary_key=True)
    
    ordenes: List["Orden"] = Relationship(
        back_populates="usuario", 
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

class MostrarUsuario(UsuarioEstructura):
    id: int