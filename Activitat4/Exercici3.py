import random
import numpy as np



def crearMatriz():
  NumeroFilas = int(input("Dinos el numero de filas"))
  NumeroColumnas = int(input("Dinos el numero de columnas"))
  
  matrizRamdon = np.random.randint(1,101, size =(NumeroFilas,NumeroColumnas))
 
  print(matrizRamdon)
  
  NumeroFilasNuevo = int(input("Dinos el nuevo numero de filas"))
  NumeroColumnasNuevo = int(input("Dinos el nuevo numero de columnas"))
  
  if NumeroFilas * NumeroColumnas != NumeroFilasNuevo * NumeroColumnasNuevo:
      print("No se puede cambiar el tamaño de la matriz")
      return matrizRamdon
  
  redimensionMatriz  = matrizRamdon.reshape((NumeroFilasNuevo,NumeroColumnasNuevo))
  print(redimensionMatriz)
 

  
  return redimensionMatriz

def valorMaximo():
        matriz = crearMatriz()
        maximo = np.max(matriz)
        print(f"el valor maximo es {maximo}")


valorMaximo()

def valorMinimo():
    matriz = crearMatriz()
    minimo = matriz.min()
    print(f"el valor minimo es {minimo}")

valorMinimo()
    

