import psycopg2
from connection import read_db

def eliminar_alumno(id_introducido):
    try:
        conn = read_db()
        cursor = conn.cursor()
        
        eliminar = "DELETE FROM estudiantestic WHERE id = %s"
        
        try:
            cursor.execute(eliminar, (id_introducido,))  
            conn.commit() 
            
            if cursor.rowcount == 0: # Se encarga de eliminar o actualizar un registro.
                # si es igual a 0 significa que no se encontro ningun id con lo que se introdujo
                # si es mayo a 0 nos dice cuantas lineas fueron afectadas
                print("Alumno no encontrado con ese ID.")
            else:
                print("Registro eliminado exitosamente.")
        
        except psycopg2.Error as e:
            print("Error al ejecutar la eliminación:", e)

    except psycopg2.Error as e:
        print("Error de conexión:", e)
        
    finally:
        if 'conn' in locals():  # Verifica que conn fue inicializado
            conn.close()
