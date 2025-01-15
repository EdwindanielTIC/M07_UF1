import psycopg2
import conn as cn
import alumne_Schema 
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
                
                return alumne_Schema.jugador_schema(jugador)
                
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta")
    
    
def categorias(nombre: str):
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        
        query_categorias = "INSERT INTO categorias (nombre) VALUES (%s)"
        cur.execute(query_categorias, (nombre,))
        conn.commit()
        print("Se ha insertado correctamente")
        return alumne_Schema.categorias_schema((cur.lastrowid, nombre))
        
    
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta {e} ")
    

def palabras(palabra: str, categoria: str, idioma: str):
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        
        query_palabras = "INSERT INTO palabras (palabra, categoria, idioma) VALUES (%s, %s, %s)"
        cur.execute(query_palabras, (palabra, categoria, idioma))
        conn.commit()
        print("Se ha insertado correctamente")
        
        
        ## El siguiente codigo lo que hara sera devolver la palabra que se ha insertado
        query_select = "SELECT * FROM palabras WHERE id_palabras = %s"
        cur.execute(query_select, (cur.lastrowid,))
        nueva_palabra = cur.fetchone()
        
        
        return alumne_Schema.palabra(nueva_palabra)
        
    
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta {e} ")
    
    
    

