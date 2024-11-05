# primer paso debo crear una tabla y luego añadir un registo
import psycopg2

def create_table():

        try: 
                # crear una conexión a la base de datos
                conn = psycopg2.connect(
                database = "UF2",  # nombre de la base de datos, no me conectaba bien, porque no habia creado la base de datos llamda UF2
                user = 'postgres',
                password= 'DAWM7',
                host = 'localhost',
                port = '5432'
                )
                
                cursor = conn.cursor()
                ## HE LLAMADO LA TABLA EstudiantesTIC pero en pgadmin me aparece todo en minuscula, preguntar roger
                sql = '''CREATE TABLE EstudiantesTIC ( 
                        ID SERIAL PRIMARY KEY,
                        Nombre Varchar(50) NOT NULL,
                        Apellido Varchar(50) NOT NULL,
                        Edad int,
                        Direccion Varchar(50),
                        Telefono int
                )'''


                cursor.execute(sql)
                conn.commit()
                print("La tabla ha sido creada con exito ")
                
        except Exception as e:
         print("Error, no se ha podido crear la tabla")
        finally:
         conn.close()