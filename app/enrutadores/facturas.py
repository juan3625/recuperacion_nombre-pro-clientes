from fastapi import  APIRouter, HTTPException, status
from modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer, FacturaLeerCompuesta
from modelos.clientes import Cliente
from listas import lista_facturas, lista_clientes
from conexion_bd import Session_dependencia
from sqlmodel import select

rutas_facturas = APIRouter()

#lista_clientes:list[Cliente] = []
#lista_facturas:list[Factura] = []

@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion: Session_dependencia):
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


@rutas_facturas.get("/facturas{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int, sesion: Session_dependencia):
    factura_encontrada = sesion.get(Factura, factura_id)
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe",
        )
    return factura_encontrada



@rutas_facturas.post("/facturas{cliente_id}", response_model=Factura)
async def Crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion:Session_dependencia):


    cliente_encontrado = sesion.get(Cliente, cliente_id)
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )
    
    Factura_dict = datos_factura.model_dump()
    Factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(Factura_dict)
    
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val

    

@rutas_facturas.patch("/facturas{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass


@rutas_facturas.delete("/facturas{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass