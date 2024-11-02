import numpy as np  
#para hacer el siguiente ejercicio, tengo dos opciones, una es escribir los numero del 1 al 49 manualmente, 
# o la segunda opcion es hacer un arange(1,50) que me hago un rango del 1 al 49 y es mucho mas facil 

# diagonal = np.array([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
#                      24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,
#                      43,44,45,46,47,48,49])
def ejercicio1():
    ndarray = np.arange(1,50)
    arrayDiagonal = np.diag(ndarray)
    print(arrayDiagonal)
    NumeroElementos = arrayDiagonal.size
    dimesionMatriz = arrayDiagonal.shape
    TipoElementos = arrayDiagonal.dtype
    tamañoMatriz = arrayDiagonal.nbytes
    
    print( )

    print(f" Numero total elementos : {NumeroElementos}")
    print(f" La dimension de la matriz es : {dimesionMatriz}")
    print(f" Tipo de elementos de la matriz : {TipoElementos}")
    print(f" El tamaño de la matriz es : {tamañoMatriz}")





