import psycopg2
from connection import read_db

def update_Estudiante(id, nombre=None, apellido=None, edad=None, direccion=None, telefono=None):
    try:
        conn = read_db()
        cursor = conn.cursor()

        # Crea el diccionario de campos y valores
        fields = {"nombre": nombre, "apellido": apellido, "edad": edad, "direccion": direccion, "telefono": telefono}
        updates = {key: value for key, value in fields.items() if value is not None}
        # esto es lo que ayuda en la consulta a omitir a todo aquello que es none
       
        if updates:
            query = "UPDATE estudiantesTIC SET " + ", ".join([f"{key} = %s" for key in updates.keys()]) + " WHERE id = %s"
            cursor.execute(query, list(updates.values()) + [id])
            #execute --> el cursor es lo que hace la coneccion a la bbdd , a travez de esto se me ejecutara la consulta.
            # cursor.execute() toma los select,insert,update etc.. y los ejecuta en la base de datos
            conn.commit()
            print("Registro actualizado exitosamente.")

    except Exception as e:
        print(f"Error al actualizar el registro: {e}")

    finally:
        # Cierra el cursor y la conexión si existen
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()
