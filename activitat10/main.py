from fastapi import FastAPI
from typing import List
from opciones_sc import options_schema
import read 
import conn as cn
import create as cr

app = FastAPI()


if __name__ == "__main__":   
 conn = cn.connection_db()
 cr.create_table()
 

@app.get("get")
async def root():
    return {"message": "Actividad 10 fastapy"}

@app.get("/tematicas_juego", response_model= List[dict])
async def obtener_opciones():
    return options_schema(read.read_db())


@app.get("/penjat/tematica/{option}", response_model = List[dict])
async def get_word(option: str):
   word = options_schema(read.read_word_db(option))
   print("")
   print("IMPRESSIÓ WORD del mètode GET_WORD")
   print(type(word))
   print(word)
  
   return word
