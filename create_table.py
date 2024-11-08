# primer paso debo crear una tabla y luego añadir un registo
import psycopg2
from connection import read_db

def create_table():

        try:    
                conn = read_db()
                cursor = conn.cursor()
                ## HE LLAMADO LA TABLA EstudiantesTIC pero en pgadmin me aparece todo en minuscula, preguntar roger
                sql = '''CREATE TABLE EstudiantesTIC ( 
                        ID SERIAL PRIMARY KEY,
                        Nombre Varchar(150) NOT NULL,
                        Apellido Varchar(150) NOT NULL,
                        Edad int,
                        Direccion Varchar(150),
                        Telefono int
                )'''

                cursor.execute(sql)
                conn.commit()
                print("La tabla ha sido creada con exito ")
                
        except Exception as e:
         print("Error, no se ha podido crear la tabla")
        finally:
         conn.close()