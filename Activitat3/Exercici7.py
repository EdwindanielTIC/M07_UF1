while True:
            try:
                edades = {}
                edadIndicada = int(input("Dinos la cantidad de personas que quieres agregar "))
                
                for _ in range(edadIndicada):
                    
                       if nombre == nombre:
                        print("El nombre ya existe")
                    
                        nombre = input("Dinos tu nombre ")
                        edad = int(input("Dinos tu edad"))
                        edades[nombre] = edad
    
                print(edades)
                break 
            except ValueError:
                print("Introduce un numero")
            