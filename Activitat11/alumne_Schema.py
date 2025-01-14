def jugador_schema(jugador):
    return {
        "id_jugador": jugador[0],
        "nombre": jugador[1],
        "apellido": jugador[2]
    }


def categorias_schema(categorias):
    return{
        "id_categorias": categorias[0],
        "nombre" : categorias[1]
    }
    
def palabra_Schema(palabra):
    return{
        "id_palabras": palabra[0],
        "palabra": palabra[1],
        "categoria": palabra[2],
        "fecha_creacion": palabra[3],
        "idioma": palabra[4],
        "categoria_id": palabra[5],
    }