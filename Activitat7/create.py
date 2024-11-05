import psycopg2

def insertar_estudiante():
    try:
        # Esto tengo que ponerlo siempre que quiera crear algo en pgadmi, ya que es lo que se encarga de conectar la base de datos
        conn = psycopg2.connect(
            database="UF2",
            user="postgres",
            password="DAWM7",
            host="localhost",
            port="5432"
        )
        
    
        cursor = conn.cursor()
        
        insert_query = """
        INSERT INTO estudiantestic (id, nombre, apellido, edad, direccion, telefono)
        VALUES (%s, %s, %s, %s, %s, %s)
        """    
        
        nuevo_estudiante = ("04332170", "Edwin Daniel", "Ramirez Cubias", 25, "Calle Encarnacion", "634763265")
 
        cursor.execute(insert_query, nuevo_estudiante)
        
  
        conn.commit()
        print("Registro insertado con éxito.")
        
    except Exception as e:
        print("Ocurrió un error:", e)
    
    finally:
     
        if cursor:
            cursor.close()
        if conn:
            conn.close()

