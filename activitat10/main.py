from fastapi import FastAPI
from typing import List
from opciones import options_schema
import read 

app = FastAPI()

@app.get("get")
async def root():
    return {"message": "Actividad 10 fastapy"}

@app.get("/tematicas_juego", response_model= List[dict])
async def obtener_opciones():
    return options_schema(read.read_db())


