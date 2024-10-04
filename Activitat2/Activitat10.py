import random

numeroadivinar = random.randint(1, 100)
intentos = 0
Acierto = False

print("Endevina el número entre 1 i 100!")


while not Acierto:
    intentos = int(input("Introdueix el teu número: "))
    intentos += 1

    if intentos < numeroadivinar:
        print("El número és més gran!")
    elif intentos > numeroadivinar:
        print("El número és més petit!")
    else:
        Acierto = True
        print(f"has acertado el numero en {intentos} intentos")
