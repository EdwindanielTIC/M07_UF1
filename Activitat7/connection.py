import psycopg2

## CONECTANDO LA BASE DE DATOS HECHO

def read_db():

  print("Conexión exitosa")
  return psycopg2.connect(
        database = "UF2",  # nombre de la base de datos, no me conectaba bien, porque no habia creado la base de datos llamda UF2
        user = 'postgres',
        password= 'DAWM7',
        host = 'localhost',
        port = '5432'
    )


read_db()

