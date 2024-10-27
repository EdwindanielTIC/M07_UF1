      
while True:
   
   try: 
      numeroUsiario = (int(input("Introduce un numero y te muestro la tabla de multiplicar "))) # para que el try-except me funcione, debo de introducir el input dentro, 
      # 
      for x in range(1,10+1):
           # multiplicacion = numeroUsiario * x
            print (f"{numeroUsiario} X {x} =  {numeroUsiario * x}")
      
   except ValueError:
      print("Introduce un valor correcto")


      
      
