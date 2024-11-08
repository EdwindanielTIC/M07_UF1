import psycopg2
from connection import read_db
def insertar_estudiante(id=None, nombre=None, apellido=None, edad=None, direccion=None, telefono=None):
    try:
        conn = read_db()
        cursor = conn.cursor()
        
        insert_query = """
        INSERT INTO EstudiantesTIC (id, nombre, apellido, edad, direccion, telefono)
        VALUES (%s, %s, %s, %s, %s, %s)
        """    

        cursor.execute(insert_query, (id, nombre, apellido, edad, direccion, telefono))
        # en este caso, el cursor lo que hace es que me actualiza la bbdd, hace un INSERT en alumnostic
        # luego, coge los parametros que he dado y los actualizara
        # En resumen , lo que me hara el cursor.execute es actulizar la base de datos.
        conn.commit()
        print("Registro insertado con éxito.")
        
    except Exception as e:
        print("Ocurrió un error:", e)
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


## borrar volumenes.