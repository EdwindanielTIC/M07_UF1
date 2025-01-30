import psycopg2
from db_connect.connect import connection_db
from Schemas.Schema import user_schema  # Asegúrate de importar esta función

def read_user(user_id: int):
 
    try:
        conn = connection_db()
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE user_id = %s"
        cur.execute(query, (user_id,))  # Importante: (user_id,) debe ser una tupla con una coma
        usuario = cur.fetchone()
        
        if usuario:
            return user_schema(usuario)  # Devuelve un diccionario 
        
        return "No existe usuario con es id" 
    
    except Exception as e:
        raise Exception(f"Error al leer el usuario: {e}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
