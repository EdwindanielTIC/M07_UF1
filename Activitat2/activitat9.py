
palabra = input("Dinos la primera palabra: ")
palabra2 = input("Dinos la segunda palabra: ")

palabranuevauno = palabra2[:2] + palabra[2:]
palabranuevados = palabra[:2] + palabra2[2:]

print("Primera palabra", palabranuevauno)
print("Segunda palabra", palabranuevados)

