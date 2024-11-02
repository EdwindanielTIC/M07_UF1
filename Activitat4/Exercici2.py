import numpy as np

def funcion1():
    array1 = [88,23,39,41]
    imprimirArray1 = np.array(array1)

    print(imprimirArray1)
    longitudUno = imprimirArray1.size
    dimesionUno = imprimirArray1.shape
    tipoElemento = imprimirArray1.dtype
    Tamañomatriz = imprimirArray1.nbytes
    print(f"El numero total de elemtos es : {longitudUno}")
    print(f"Numero total de elementos  :  {dimesionUno}")
    print(f"El tipo de elemeto :  {tipoElemento}")
    print(f"Tamaño de la matriz :  {Tamañomatriz} bytes")


def funcion2():
    array2 = [[46.4, 21.7, 38.4],[41.2, 58.8, 68.9]]
    imprimirArray2 = np.array(array2)
    print(imprimirArray2)
    
    numeroElemetnos = imprimirArray2.size
    dimesion = imprimirArray2.shape
    tipoElemento = imprimirArray2.dtype
    Tamañomatriz = imprimirArray2.nbytes
    
    print(f"El numero total de elemtos es : {numeroElemetnos} ")
    print(f"la dimension de la matriz es : {dimesion}")
    print(f"El tipo de elemento es : {tipoElemento}")
    print(f"El tamaño de la matriz es : {Tamañomatriz} bytes")
    
    
def funcion3():
    array3 = np.array([[12],[4],[9],[8]])
    print(array3)
    
    NumeroElementos = array3.size
    dimensionElementos = array3.shape
    tipoElementos = array3.dtype
    TamañoElemetnos = array3.nbytes
    
    
    print(f"El numero total de elemtos es : {NumeroElementos} ")
    print(f"la dimension de la matriz es :  {dimensionElementos}")
    print(f"El tipo de elemento es : {tipoElementos}")
    print(f"El tamaño de la matriz es : {TamañoElemetnos} bytes")
    
    

    
# matriz.size: Devuelve el número total de elementos en la matriz.
# matriz.shape: Devuelve la dimensión de la matriz como una tupla (número de filas y columnas).
# matriz.dtype: Devuelve el tipo de datos de los elementos internos en la matriz.
# matriz.nbytes: Devuelve el tamaño total en bytes que ocupa la matriz en memoria.
    

    


