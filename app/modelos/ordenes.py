from pydantic import computed_field
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List

from .items_orden import ItemOrden
from .usuarios import Usuario, MostrarUsuario

class OrdenEstructura(SQLModel):
    fecha_registro: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def total_calculado(self) -> float:
        suma = 0.0
        # Validamos si existe el atributo items para evitar errores
        if not hasattr(self, 'items') or not self.items:
            return suma
        for item in self.items:
            suma += item.costo_unidad * item.cant
        return suma

class NuevaOrden(OrdenEstructura):
    pass

class ModificarOrden(OrdenEstructura):
    pass

class Orden(OrdenEstructura, table=True):
    __tablename__ = "ordenes"
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(default=None, foreign_key="usuarios.id")
    
    usuario: Usuario = Relationship(back_populates="ordenes")
    items: List[ItemOrden] = Relationship(back_populates="orden")

class VerOrden(OrdenEstructura):
    id: int
    usuario: MostrarUsuario

class VerOrdenDetalle(VerOrden):
    items: List[ItemOrden] = []