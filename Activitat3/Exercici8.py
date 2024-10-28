numeroUsuarios = input("Introduce 10 numero")

Separacion = numeroUsuarios.split(" ")

numeroUsuarios = [int (x) for x in Separacion]
print(f"Numero usuario {numeroUsuarios}")

sumaNUmero = 0

if len(numeroUsuarios) == 10:
    
    for x in numeroUsuarios:
        sumaNUmero += x
    print(f"suma total {sumaNUmero}")

media = sumaNUmero / len(numeroUsuarios)

print(f"la media es {media}")

ElementosNuevos = [media,sumaNUmero]

for x in ElementosNuevos:
    numeroUsuarios.append(x)

print(numeroUsuarios)






