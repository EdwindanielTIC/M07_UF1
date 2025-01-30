from db_connect.connect import connection_db
import Schemas.Schema as Schema

def createTable(conn):
    try:
        cur = conn.cursor()
        sql= ''' CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_surname VARCHAR(255) NOT NULL,
                user_age int,
                user_email VARCHAR(255) NOT NULL)
        '''
        
        cur.execute(sql)
        conn.commit()
        return "la tabla users ha sido creada correctamente"
    except Exception as e:
        print(f"Error en la funcion de crear la tabla: {str(e)}")
        

def createUSuario(user_id: int, user_name: str, user_surname: str, user_age: int, user_email: str): 
    try:
        conn = connection_db()
        cur = conn.cursor()
        query = "INSERT INTO users (user_id, user_name, user_surname, user_age, user_email) VALUES (%s, %s, %s, %s, %s) RETURNING *"
        # con el returnin * me devuelve todos los datos del usuario insertado.
       
        cur.execute(query, (user_id, user_name, user_surname, user_age, user_email))
        
        usuarioInsertado = cur.fetchone()
        conn.commit()
        return  Schema.user_schema(usuarioInsertado)
    except Exception as e:
        return f"NO se ha podido insertar el usuario: {e}"
    finally:
        cur.close()
        conn.close()