areas_pis = ["Menjador" , 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# slicing [Inicio:Fin:Paso]

print(f"Segundo numero :  {areas_pis[1]}")
print(f"Ultimo elemento : {areas_pis[-1]}")
print(f"Area Terrassa : {areas_pis[7]}")

print(f"Los tres primeros elementos son : {areas_pis[:3]}")
print(f"del 3 al ultimo son : {areas_pis[3:]}")

sumaHabitacion = areas_pis[5] + areas_pis[-1]
print(f"primera habitacion {areas_pis[5]} segunda habitacion {areas_pis[-1]} la suma es {sumaHabitacion}")

areas_pis[9] = 100
print(f"area baño modificada {areas_pis}" )


nuevosElemetnos = ["pati interior", 2.78] 
for x in nuevosElemetnos:
    areas_pis.append(x)
    
print(f"Nuevo array {areas_pis}")


sumaAreas = areas_pis[1::2] # este punto lo que hago es empezar desde el primer producdo e ir saltado 2, ya que como sigue un patron, voy cogiendo los numero
print(f"la suma de todos los numeros es la siguiente {sumaAreas}")

resultado = 0
for x in sumaAreas:
    resultado += x

print(f"el resultado es {resultado} ")


    
   
    