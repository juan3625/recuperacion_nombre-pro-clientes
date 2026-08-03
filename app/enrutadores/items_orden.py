from fastapi import APIRouter, HTTPException, status
from app.modelos.items_orden import ItemOrden, CrearItem, ModificarItem
from app.modelos.ordenes import Orden
from conexion_bd import Session_dependencia
from sqlmodel import select

api_items = APIRouter()  

@api_items.get("/items", response_model=list[ItemOrden])
async def listar_items(db_session: Session_dependencia):
    return db_session.exec(select(ItemOrden)).all()

@api_items.get("/items/{id_item}", response_model=ItemOrden)
async def listar_item(id_item: int, db_session: Session_dependencia):
    item_encontrado = db_session.get(ItemOrden, id_item)
    if not item_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ningún registro asociado al ID: {id_item}"
        )
    return item_encontrado

@api_items.post("/items/{orden_id}", response_model=ItemOrden)
async def crear_item(orden_id: int, payload: CrearItem, db_session: Session_dependencia):
    orden_encontrada = db_session.get(Orden, orden_id)
    if not orden_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ninguna orden asociada al ID: {orden_id}"
        )
    
    item_dict = payload.model_dump()
    item_dict["orden_id"] = orden_id
    item_val = ItemOrden.model_validate(item_dict)

    db_session.add(item_val)
    db_session.commit()
    db_session.refresh(item_val)
    return item_val

@api_items.patch("/items/{id_item}", response_model=ItemOrden)
async def editar_item(id_item: int, payload: ModificarItem, db_session: Session_dependencia):
    item_encontrado = db_session.get(ItemOrden, id_item)
    if not item_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ningún registro asociado al ID: {id_item}"
        )

    datos_nuevos = payload.model_dump(exclude_unset=True)
    item_encontrado.sqlmodel_update(datos_nuevos)

    db_session.add(item_encontrado)
    db_session.commit()
    db_session.refresh(item_encontrado)
    return item_encontrado

@api_items.delete("/items/{id_item}", response_model=ItemOrden)
async def eliminar_item(id_item: int, db_session: Session_dependencia):
    item_encontrado = db_session.get(ItemOrden, id_item)
    if not item_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ningún registro asociado al ID: {id_item}"
        )

    db_session.delete(item_encontrado)
    db_session.commit()
    return item_encontrado
