import psycopg2
import conn as cn
import alumne_Schema as al

def leer_jugador(id_jugador : int):
    try:
                conn = cn.connection_db()
                cur = conn.cursor()
                
                query = "SELECT id_jugador,nombre,apellido FROM jugador WHERE id_jugador = %s"
                cur.execute(query, (id_jugador,))
                jugador = cur.fetchone()
                
                if not jugador:
                    return "No se ha encontrado el jugador"
                
                # return {
                #     "id_jugador": jugador[0],
                #     "nombre": jugador[1],
                #     "apellido": jugador[2]
                # }
                
                return al.jugador_schema(jugador)
                
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta:, el error esta en la consulta ")