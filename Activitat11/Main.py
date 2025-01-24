import psycopg2
from psycopg2 import sql
import conn as cn
import create as cr
import db_juego
from pydantic import BaseModel
from datetime import datetime

from fastapi import FastAPI, HTTPException

app = FastAPI()


if __name__ == "__main__":   
    conn = cn.connection_db()
    cr.create_table(conn)

class usuarios_BM(BaseModel):
    id_jugador: int
    nombre: str
    apellido: str

class categoriasBM(BaseModel):
    id_categorias: int = None
    nombre: str

class palabrasBM(BaseModel):
    id_palabras: int = None  # Opcional porque se genera automáticamente
    palabra: str
    categoria: str
    fecha_creacion: datetime  # Opcional, manejado por la base de datos
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
        
        jugador = db_juego.leer_jugador(id_jugador)
        if not jugador:
                raise HTTPException(status_code=404, detail="No se ha encontrado el jugador")
        return usuarios_BM(**jugador)  
     
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
    

@app.post("/categorias", response_model=categoriasBM, tags=["categorias"])
def create_categorias(categoria: categoriasBM):
    try:
        nueva_categoria = db_juego.categorias(categoria.nombre)
        print("Se ha insertado correctamente ")
        return nueva_categoria
       
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
  
  
@app.post("/palabras", response_model=palabrasBM)
def create_palabras(palabrasDelJuego: palabrasBM):
    try:
        print(f"Datos recibidos: {palabrasDelJuego}")
        nueva_palabra = db_juego.palabras(
            palabra=palabrasDelJuego.palabra,
            categoria=palabrasDelJuego.categoria,
            idioma=palabrasDelJuego.idioma,
            categoria_id=palabrasDelJuego.categoria_id
        )
        return nueva_palabra
    except Exception as e:
        print(f"Error interno: {e}")  # Debug: Imprimir error en la consola
        raise HTTPException(status_code=500, detail=str(e))

