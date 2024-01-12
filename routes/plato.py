from fastapi import APIRouter, HTTPException, status
from config.bd import conn
from models.plato import platos
from sqlalchemy import select
from schemas.plato import Plato

plato = APIRouter()

@plato.get("/", response_model=list[Plato], tags = ["platos"])
@plato.get("/platos", response_model=list[Plato], tags = ["platos"])
def getAllPlatos():
    return conn.execute(platos.select()).fetchall()

@plato.get("/platos/{id}",response_model=Plato, tags = ["platos"])
def getPlato(id: int):
    plato = conn.execute(platos.select().where(platos.c.id==id)).first() 
    if plato:
        return plato
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

@plato.post("/platos", response_model=Plato, tags = ["platos"])
def altaPlato(plato: Plato):
    nuevoPlato = {"nombre": plato.nombre, "precio":plato.precio, "tipo":plato.tipo}
    resultado = conn.execute(platos.insert().values(nuevoPlato))
    conn.commit()
    return conn.execute(platos.select().where(platos.c.id == resultado.lastrowid)).first()

@plato.put("/platos/{id}", response_model=Plato, tags = ["platos"])
def editarPlato(id: int, plato:Plato):
    platoSeleccionado = conn.execute(platos.select().where(platos.c.id==id)).first() 
    if platoSeleccionado:
        conn.execute(platos.update().values(nombre = plato.nombre, precio = plato.precio, tipo = plato.tipo).where(platos.c.id == id))
        conn.commit()
        return conn.execute(platos.select().where(platos.c.id==id)).first()
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

@plato.delete("/platos/{id}",response_model=Plato, tags = ["platos"])
def eliminarPlato(id: str):
    eliminado = conn.execute(platos.select().where(platos.c.id==id)).first() 
    if eliminado:
        conn.execute(platos.delete().where(platos.c.id == id))
        return eliminado
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)



