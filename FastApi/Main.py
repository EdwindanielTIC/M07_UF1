from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

app.title = "Mi primera aplicacion con FastApi de alumnos"

class Item(BaseModel): ## esto lo conecto con el post
    id: int
    name: str
    Apellido: str
    Edad:int
    Direccion : Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "Ejecutando condigo get"}

## CREANDO GET

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in Item:
        raise HTTPException (status_code = 404, detail= "Página no encontrada")
    return {"item": Item[item_id]}

## CREANDO POST

@app.post("/Items")
async def creando_items(item:Item):
    return item







