from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)
    #cliente: Cliente 
    #transacciones: list[Transaccion] = []

    
@computed_field
@property
def vr_total(self) -> float:
        total_factura = 0.0
        if not self.transacciones:
            return total_factura

        for transaccion in self.transacciones:
            total_factura += transaccion.vr_unitario * transaccion.cantidad

        return total_factura



class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    cliente : Cliente = Relationship(back_populates="factura")
    transacciones: list[Transaccion] = Relationship(back_populates="factura")

class FacturaLeer(FacturaBase):
    id: int
    cliente: ClienteLeer

class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transaccion] = []