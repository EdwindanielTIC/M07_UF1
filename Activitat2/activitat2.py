var1 = float(input("Introduce el número: "))
print(var1)

var2 = float(input("Introduce un número de IVA (4, 10, 21): "))
print(var2)

if var2 == 4 or var2 == 10 or var2 == 21:
    resultado = var1 + (var1 * (var2 / 100))  
    print("El resultado es el siguiente: " + str(resultado))
else:
    while var2 != 4 and var2 != 10 and var2 != 21:
        print("El IVA no es correcto")
        var2 = float(input("Introduce un número de IVA (4, 10, 21): "))
    resultado = var1 + (var1 * (var2 / 100))  
    print("El resultado es el siguiente: " + str(resultado))
