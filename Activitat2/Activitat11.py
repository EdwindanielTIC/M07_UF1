
numero = int(input("Dinos el numero y te muestro su tabla de multiplicar"))

print(f"la tabla de multiplicar del numero {numero} es :")
for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} * {i} = {resultat}")
