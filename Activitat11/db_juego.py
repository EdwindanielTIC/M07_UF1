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
        
        query_categorias = "INSERT INTO categorias (nombre) VALUES (%s) RETURNING id_categorias"
        cur.execute(query_categorias, (nombre,))
        
        id_categoria = cur.fetchone()[0]
        conn.commit()
        
        print("Se insertado correctamente")
        return alumne_Schema.categorias_schema((id_categoria,nombre))
      
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta {e} ")
    



def palabras(palabra: str, categoria: str, idioma: str, categoria_id: int):
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        
        query_palabras = """
        INSERT INTO palabras (palabra, categoria, idioma, categoria_id) 
        VALUES (%s, %s, %s, %s) RETURNING *
        """
        values = (palabra, categoria, idioma, categoria_id)
        
        # me imprimirar la consulta y los valores para controlar los posibles errores 
        print(f"Ejecutando consulta: {query_palabras} con valores {values}")
        
        cur.execute(query_palabras, values)
        conn.commit()
        
        nueva_palabra = cur.fetchone()
        return alumne_Schema.palabra(nueva_palabra)
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta: {e}")
    finally:
        cur.close()
        conn.close()
    
    
    

