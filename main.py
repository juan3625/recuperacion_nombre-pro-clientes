from fastapi import FastAPI
from app.enrutadores.usuarios import api_usuarios
from app.enrutadores.items_orden import api_items
from app.enrutadores.ordenes import api_ordenes
from conexion_bd import crear_tablas
from fastapi.responses import RedirectResponse
 
app = FastAPI(lifespan=crear_tablas)
 
app.include_router(api_usuarios, tags=["Usuarios"])
app.include_router(api_items, tags=["Items"])
app.include_router(api_ordenes, tags=["Ordenes"])

@app.get("/", include_in_schema=False)
async def raiz():
    return RedirectResponse(url="/docs")