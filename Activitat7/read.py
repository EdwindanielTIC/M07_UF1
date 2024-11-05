import psycopg2

def read_alumno():
    try:
        # Establecer la conexión
        conn = psycopg2.connect(
        database = "UF2",  
        user = 'postgres',
        password= 'DAWM7',
        host = 'localhost',
        port = '5432'     
        )
        
        cursor= conn.cursor()
        
        mostrar_registros = """
        SELECT * FROM estudiantestic
        """
        cursor.execute(mostrar_registros)
        
        registros = cursor.fetchall() 
        # con lo siguiente, lo que hago es recorrer los registros que tengo en db
        # si los encunetra me los devolvera. Para hacerme una idea , el SELECT Y EL FETCHALL VAN DE LA MANO
        # El Select me selecciona todo lo de la bbdd y el fetchall me los trae a pyton
        if registros:
            for registros in registros:
                print(registros)
        else:
         print("No hay registros")

    except Exception as e:
        print("Alumno no encontrado")
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("conexion cerrada con exito ")

read_alumno()