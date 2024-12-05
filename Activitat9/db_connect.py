import psycopg2

conn = psycopg2.connect(
    database="databaseAct9",
    user="postgres",
    password="EdwinDaniel",
    host = "localhost",
    port="5432"
)

connection = conn.cursor()

print(connection)