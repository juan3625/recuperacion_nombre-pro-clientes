from fastapi import APIRouter, HTTPException, status
from app.modelos.ordenes import Orden, NuevaOrden, ModificarOrden, VerOrden, VerOrdenDetalle
from app.modelos.usuarios import Usuario
from conexion_bd import Session_dependencia
from sqlmodel import select

api_ordenes = APIRouter()

@api_ordenes.get("/ordenes", response_model=list[VerOrden])
async def listar_ordenes(db_session: Session_dependencia):
    return db_session.exec(select(Orden)).all()

@api_ordenes.get("/ordenes/{orden_id}", response_model=VerOrdenDetalle)
async def listar_orden(orden_id: int, db_session: Session_dependencia):
    orden_encontrada = db_session.get(Orden, orden_id)
    if not orden_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ninguna orden asociada al ID: {orden_id}"
        )
    return orden_encontrada

@api_ordenes.post("/ordenes/{usuario_id}", response_model=Orden)
async def crear_orden(usuario_id: int, payload: NuevaOrden, db_session: Session_dependencia):
    usuario_encontrado = db_session.get(Usuario, usuario_id)
    if not usuario_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El usuario con id {usuario_id}, no existe."
        )

    orden_dict = payload.model_dump()
    orden_dict["usuario_id"] = usuario_id
    orden_val = Orden.model_validate(orden_dict)

    db_session.add(orden_val)
    db_session.commit()
    db_session.refresh(orden_val)
    return orden_val

@api_ordenes.patch("/ordenes/{orden_id}", response_model=Orden)
async def editar_orden(orden_id: int, payload: ModificarOrden, db_session: Session_dependencia):
    orden_encontrada = db_session.get(Orden, orden_id)
    if not orden_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ninguna orden asociada al ID: {orden_id}"
        )

    datos_nuevos = payload.model_dump(exclude_unset=True)
    orden_encontrada.sqlmodel_update(datos_nuevos)

    db_session.add(orden_encontrada)
    db_session.commit()
    db_session.refresh(orden_encontrada)
    return orden_encontrada

@api_ordenes.delete("/ordenes/{orden_id}", response_model=Orden)
async def eliminar_orden(orden_id: int, db_session: Session_dependencia):
    orden_encontrada = db_session.get(Orden, orden_id)
    if not orden_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ninguna orden asociada al ID: {orden_id}"
        )

    db_session.delete(orden_encontrada)
    db_session.commit()
    return orden_encontrada