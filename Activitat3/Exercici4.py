numeros = input("Introduce 10 números separados por espacios y te los muestro ordenados: ")
separacion = numeros.split()  # Divide la entrada en una lista de cadenas

if len(separacion) == 10 :
    numeros = [int(x) for x in separacion]
    print(f"los numeros son {numeros}")
    
    numeros.sort()
#for i in range(len(numeros)):
   #for j in range(0,len(numeros)-i-1):
    #    if numeros[j]> numeros[j + 1]:
     #       numeros[j], numeros[j + 1 ]= numeros[j + 1],numeros[j]


print(f"de pequeño a mas grande {numeros}")
        
numeros.sort(reverse=True)

print(f"numeor de mas grande mas pequeños {numeros}")
    