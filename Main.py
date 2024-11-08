import create as CreacionBD #funcona
import read as LeerBD # funciona
import update as ModificarAlunmoBD #funciona
import delete as EliminarAlumnoBD # funciona
import connection as ConexionBD #funciona
import create_table as CreacionTablaBD ## funciona


while True:
    try:
        menu = int(input("Introduce un número:\n 1 : create\n 2 : read\n 3 : update\n 4 : Delete\n 5 : connection\n 6 : create_table \n "))

        if 1 <= menu <= 5:
            print(f"Has escogido la opción {menu}")

            if menu == 1:
                
                # Este punto la palabra None es muy importante, porque si por ejemplo, no queremos
                #modificar apellido, la palabra none nos ayuda a omitir estos campos en la consulta
           
                print("Creacion de alumno")
                print()
                id = int(input("ID Alumno: ")) 
                nombre = input("El nombre será: ") or None
                apellido = input("El apellido es:  ") or None
                edad = input("La edad es: ") or None
                direccion = input("La dirección es: ") or None
                telefono = input("El número de teléfono es: ") or None

                
                edad = int(edad) if edad else None
                telefono = int(telefono) if telefono else None
                
                CreacionBD.insertar_estudiante(id,nombre, apellido, edad, direccion, telefono)
                
            if menu == 2:
                LeerBD.read_alumno()
                
            if menu == 3:
                
                print("Modificar alumno ")
                print()
                id = int(input("ID Alumno a actualizar: "))
                nombre = input("El nombre nuevo será: ") or None
                apellido = input("El nuevo apellido es: ") or None
                edad = input("La nueva edad es: ") or None
                direccion = input("La nueva dirección es: ") or None
                telefono = input("El nuevo número de teléfono es: ") or None

                edad = int(edad) if edad else None
                telefono = int(telefono) if telefono else None
                
                ModificarAlunmoBD.update_Estudiante(id,nombre,apellido,edad,direccion,telefono)
                
            if menu == 4:
                
                print("Eliminar alumno ")
                print()
                id_introducido = int(input("Introduce el ID del alumno a eliminar"))
                EliminarAlumnoBD.eliminar_alumno(id_introducido)
                
            if menu == 5:
                
                print("Mostrando alumnos ")
                print()
                ConexionBD.read_db()
            
            if menu == 6:
                print("Creacion de tabla")
                CreacionTablaBD.create_table()
                
        else:
            print("Está fuera de rango, debe ser del 1 al 6")

    except ValueError:
        print("Debe de ser un numero, NO caracter")

