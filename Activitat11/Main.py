import psycopg2
from psycopg2 import sql
import conn as cn
import create as cr
from db_juego import leer_jugador, categorias, palabras
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException

app = FastAPI()


if __name__ == "__main__":   
    conn = cn.connection_db()
    cr.create_table(conn)

class usuarios_BM(BaseModel):
    id_jugador: int
    nombre: str
    apellido: str

class categorias_BM(BaseModel):
    id_categoria: int
    nombre: str

class palabras_BM(BaseModel):
    id: int
    palabra: str
    categoria: str
    fecha_creacion: str
    idioma: str
    categoria_id: int
    
class registro_juego_BM(BaseModel):
    id: int
    id_jugador: int
    id_palabra: int
    puntuacio: int
    temps_joc: int
    data_hora: str
    estat_partida: str

    

@app.get("/jugadores/{id_jugador}", response_model=usuarios_BM, tags=["jugadores"])
def get_jugadores(id_jugador: int):
    try:
        
        jugador = leer_jugador(id_jugador)
        if not jugador:
                raise HTTPException(status_code=404, detail="No se ha encontrado el jugador")
        return usuarios_BM(**jugador)  
     
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

@app.post("/categorias", response_model=categorias_BM, tags=["categorias"])
def create_categorias(nombre: str):
    try: 
        categoria_Juego = categorias(nombre)
        return categorias_BM(nombre=categoria_Juego)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
  
  
@app.post("/palabras", response_model=palabras_BM, tags=["palabras"])
def create_palabras(palabra: str, categoria: str, idioma: str):
    try: 
        palabra_Juego = palabras(palabra, categoria, idioma)
        return palabras_BM(palabra=palabra_Juego)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
