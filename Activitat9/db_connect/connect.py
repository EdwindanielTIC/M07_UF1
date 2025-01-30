import psycopg2
from psycopg2 import OperationalError

def connection_db():
    try:
        conn = psycopg2.connect(
            database="DbJSON",
            user="postgres",
            password="EdwinDaniel",
            host="localhost",
            port="5432"
        )
        print("Conexión establecida correctamente")
        return conn
    except OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")
        
