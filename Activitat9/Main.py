import psycopg2
from pydantic import BaseModel
from db_connect.connect import connection_db as cn
from crud.create import createTable, createUSuario 
from crud.read import read_user
from fastapi import FastAPI, HTTPException
from Schemas.Schema import User

app = FastAPI()



if __name__ == "__main__":
    try:
        conn = cn()
        print(".......Creando tabla users.......")
        print(createTable(conn))
    except Exception as e:
        print(f"Error: {e}") 
        
@app.put("/Users") ## este put va con el createUSuario de crud.create   
async def añadiendoUsuario(user: User): ## el user es el de baseModel que este en el schema
    mensaje = createUSuario(user.user_id ,user.user_name, user.user_surname, user.user_age, user.user_email) 
    # Muy importante que estos nombres coincidan con los nombres de la tabla,de la que inserto en el parametro de la funcion CreateUsuario, debe conicdir en cantidad tmb
    
    if "Error" in mensaje:
        raise HTTPException(status_code=500, detail=mensaje)
    return {"message": mensaje}


@app.get("/Users/{user_id}")
async def obtenerUsuario(user_id: int):
    try:
        usuario = read_user(user_id) ## con la siguiente consulta, hago la conecion a la bbdd y me devuelve el usuario con el id
        if not usuario:
            raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
        
        return usuario  ## devolvera el diccionario con los datos introducidos del usuario
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
  
 
