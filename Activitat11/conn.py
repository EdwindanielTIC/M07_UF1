import psycopg2

def connection_db():
    
    conn = psycopg2.connect(
        database = "penjat",
        user= "postgres",
        password = "1234",
        host = "localhost",
        port = "5432"
        
    )

    print("Estas conectado a la base de datos !!")
    return conn

