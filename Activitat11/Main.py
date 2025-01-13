import psycopg2 
import create as cr
import conn as cn
import json
from pydantic import BaseModel

import fastapi as app

app = app.FastAPI()

class usuarios_BM(BaseModel):
    id: int
    apellido: str
    nombre: str
    apellido: str
   


@app.get("/jugadores/{id}", tags=["jugadores"])
def get_jugadores(id: int):
    for x in cn.cursor:
        if x[id] == id:
            return x
        
    return "No se ha encontrado el jugador"



