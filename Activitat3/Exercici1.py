
while True:
    try:
        numeroIntroducido = int(input(" por favor, introduce tu numero entre 10 - 100 "))       
        break
    except ValueError:
        print("introduce un valor correcto")
        

if 10 <= numeroIntroducido <= 100:
            for x in range(1,numeroIntroducido + 1):
                print(x)
else:
            print("introduce un valor entre 10 y 100")
    


 
