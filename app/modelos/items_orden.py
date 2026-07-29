from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class ItemBase(SQLModel):
    cant: int = Field(default=0)
    costo_unidad: float = Field(default=0.0)
    obs: str = Field(default="")

class CrearItem(ItemBase):
    pass

class ModificarItem(ItemBase):
    pass

class ItemOrden(ItemBase, table=True):
    __tablename__ = "items_orden"
    id: Optional[int] = Field(default=None, primary_key=True)
    orden_id: Optional[int] = Field(default=None, foreign_key="ordenes.id")
    
    orden: Optional["Orden"] = Relationship(back_populates="items")

class VerItem(ItemBase):
    id: int