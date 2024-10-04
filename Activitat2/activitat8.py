palabras = input("dino tres palabras ")
Separaracion = palabras.split(" ")
print(Separaracion)

if 1 <= len(Separaracion) <= 3:
    
    for palabras in Separaracion:
        print(f"paraula: {palabras}")
        
else :
    print("si us plau, introdueiz 1 i 3 paraules")

    