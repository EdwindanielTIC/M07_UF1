# README actividad 7 

Archivo Create_table:

Al ejecutar el código, podemos ver que se me ha creado con éxito la base de datos:

![image](https://github.com/user-attachments/assets/6fde2682-482e-4c5d-9e33-fe0ab937dd78)

Es curioso que he llamado los nombre con mayúsculas las primeras palabras y luego en pgadmin me aparece todo en minuscula, pero funciona

![image](https://github.com/user-attachments/assets/0a090ef1-4700-4917-9671-90eeab0a9656)

Archivo Create

Al crear la tabla, he agregado un registro y se ha ejecutado con éxito. Todos los atributos del alumno los solicitó mediantes consola y se deben de introducir manualmente: 

![image](https://github.com/user-attachments/assets/a2a5b5b5-1d91-4e05-88d1-679d7de3c824)

Ahora voy a pgami y podemos ver como si me aparece el alumno introducido: 

![image](https://github.com/user-attachments/assets/d87b4e80-6592-4566-8e93-4d8ed73a8512)

Esta parte es sumamente importante, al principio no se me ejecutaba bien la base de datos, porque Estudiantes TIC tenia que estar entre comillas “EstudiantesTIC ” porque al parecer cuando se mezcla las mayusculas con minusculas deben de ir en comillas,  lo mismo pasará con lo demás, con ID,Nombre etc.. deben de ir en comillas para que me funcione bien

![image](https://github.com/user-attachments/assets/fa9b2169-61c6-48a6-8ecb-e720503c17a3)

read.py

He ejecutado el código y me ha dado lo siguiente:
Aquí cabe destacar una cosa muy importante, el cursor.fetchall().  Si no pongo esto, no podrá acceder ni mostrar los registros y el código solo ejecutará la consulta sin hacer nada con los resultados.

![image](https://github.com/user-attachments/assets/bd61118a-7a72-40f5-bd70-f6016731df70)


FUNCION DELETE

He realizado la función DELETE y podemos ver que funciona perfectamente, para poderla llevar a cabo he tenido que utilizar rowcount en cursor ya que si no ponía esta función no se me elimina. 

Como podemos observar, ejecuto la función desde el menú,le solicito al cliente que me introduzca el ID para eliminar el alumno, la consola no me devuelve ningún error y me lo elimina.

![image](https://github.com/user-attachments/assets/77afbb2e-72aa-45a4-835a-6245c1b58e74)

Luego he ido a pgAdmin para comprobar que realmente se eliminó .

![image](https://github.com/user-attachments/assets/1b7f5585-9cc7-47c8-8f43-1c55aadbb183)

Luego para comprobar que realmente funciona correctamente, he introducido en el main un input (el mismo id) y como ya ha sido borrado, lo introduzco para que me devuelva “Alumno no encontrado con ese ID”

![image](https://github.com/user-attachments/assets/816f56e7-2296-4526-80be-55a356af2554)

UPDATE
Esta parte ha sido la que más me ha costado y la que he necesitado más ayuda, como podemos ver , he buscado un alumno con su id y lo he actualizado.

![image](https://github.com/user-attachments/assets/a471b26f-5892-42c5-a294-68f1a8f94362)

Voy a pgadmin y muestro primero sin actualizar : 
![image](https://github.com/user-attachments/assets/a4b9df3e-9966-4430-a2cd-3531241f282e)

Ahora muestro el alumno actualizado : 
Como podemos ver, el código funciona perfectamente.

![image](https://github.com/user-attachments/assets/fec2adce-151d-420c-a760-21df4e344efb)


Archivo main

En el archivo main, he creado un pequeño menú donde el cliente le aparecerán 6 opciones , esas 6 funciones : create, read,update, delete, connection y create_table.

![image](https://github.com/user-attachments/assets/f11f5c90-042f-40dc-b8c8-23493153cbfa)

El menú que les aparecerá será el siguiente : como se puede ver, apareceran las 6 opciones.
![image](https://github.com/user-attachments/assets/01215aed-9cc5-4403-96d0-7d9d96ee1e2a)

¿Que pasaria si el cliente introduce un número mayor a 5 o introduce un carácter ?
Pues en primer lugar, si introduce un número mayor a 6 , le aparecerá un mensaje diciendo que debe de ser un número del 1 al 6. 
Si introduce un caracter le aparecerá el mensaje debe de ser un número, No carácter
![image](https://github.com/user-attachments/assets/7b9e37c7-bcff-4fdb-8641-512026056e18)

![image](https://github.com/user-attachments/assets/f3b42b5b-1f34-447b-beff-3e8ec0ea5d9a)

