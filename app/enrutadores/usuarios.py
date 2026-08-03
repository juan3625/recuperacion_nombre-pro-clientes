from fastapi import APIRouter, HTTPException, status
from app.modelos.usuarios import Usuario, IngresarUsuario, ActualizarUsuario
from conexion_bd import Session_dependencia
from sqlmodel import select

api_usuarios = APIRouter()  

@api_usuarios.get("/usuarios", response_model=list[Usuario])
async def listar_usuarios(db_session: Session_dependencia):
    return db_session.exec(select(Usuario)).all()

@api_usuarios.get("/usuarios/{usuario_id}", response_model=Usuario)
async def listar_usuario(usuario_id: int, db_session: Session_dependencia):
    usuario_bd = db_session.get(Usuario, usuario_id)
    if not usuario_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ningún registro asociado al ID: {usuario_id}"
        )
    return usuario_bd

@api_usuarios.post("/usuarios", response_model=Usuario)
async def crear_usuario(payload: IngresarUsuario, db_session: Session_dependencia):
    usuario_val = Usuario.model_validate(payload.model_dump())
    db_session.add(usuario_val)
    db_session.commit()
    db_session.refresh(usuario_val)
    return usuario_val

@api_usuarios.patch("/usuarios/{usuario_id}", response_model=Usuario)
async def editar_usuario(usuario_id: int, payload: ActualizarUsuario, db_session: Session_dependencia):
    usuario_bd = db_session.get(Usuario, usuario_id)
    if not usuario_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ningún registro asociado al ID: {usuario_id}"
        )
    usuario_dict = payload.model_dump(exclude_unset=True)
    usuario_bd.sqlmodel_update(usuario_dict)
    db_session.add(usuario_bd)
    db_session.commit()
    db_session.refresh(usuario_bd)
    return usuario_bd

@api_usuarios.delete("/usuarios/{usuario_id}", response_model=Usuario)
async def eliminar_usuario(usuario_id: int, db_session: Session_dependencia):
    usuario_bd = db_session.get(Usuario, usuario_id)
    if not usuario_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se localizó ningún registro asociado al ID: {usuario_id}"
        )
    db_session.delete(usuario_bd)
    db_session.commit()
    return usuario_bd
