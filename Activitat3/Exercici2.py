mesosDeAny = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

while True:
    entrada = input("Introduce un número del 1 al 12 o 0 si quieres salir del programa: ")
    try:
        numero = int(entrada)
        
        if numero == 0:
            print("Saliendo del programa.")
           
        elif 1 <= numero <= 12:
            print(f"El mes es el siguiente: {mesosDeAny[numero - 1]}")
        else:
            print("El valor está fuera del rango, introduce un número entre 1 y 12.")
    
    except ValueError:
        
        print("Introduce un valor correcto.")


## cuando debo utilizar try/except ValueError?
# cuando quiero que el usuario introduzca un numero y si en vez del numero me introduce un caracter, esta funcion hara que diera error.
# captura y maneja errores , tambien informa al usuario de errores y mantenerlos controalos