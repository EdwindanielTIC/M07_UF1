import connection as conecxion
import create as creaciondb
import create_table as creandoTabla
import read as LeerEstudiantes
 
 #Procederemos a la creacion de menus
 
"""ejecutando  la funcion de conexión"""
conecxion.read_db()
"""Crear Tabla"""
creandoTabla.create_table()
"""Creando registros"""
creaciondb.insertar_estudiante()
"""leer estudiantes"""
LeerEstudiantes.read_alumno()


