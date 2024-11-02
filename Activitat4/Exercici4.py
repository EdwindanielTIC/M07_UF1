import numpy as np

def funcion():
    mmatriz = np.random.randint(0, 81, size=(3, 4))
    print("\nMatriz principal (3x4):")
    print(mmatriz)

    ultima_fila = mmatriz[-1, :] # con esta linea extraigo la ultima fila
    

    matriz_reducida = mmatriz[:-1, :].T  # Transponertar lo que hace es convertir las filas en columnas
    matriz_modificada = np.column_stack((matriz_reducida, ultima_fila)) # este punto es importante por que agrega las colunmas y filas nuevas
    print("\nMatriz modificada (4x3) antes de ajustar la última columna:")
    print(matriz_modificada)

    primer_valor = matriz_modificada[0, -1] 
    matriz_modificada[:, -1] = primer_valor 

    print("\nMatriz final con la última columna modificada:")
    print(matriz_modificada)


funcion()
