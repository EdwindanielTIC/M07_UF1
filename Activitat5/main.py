import Actividad3 as act3
import Actividad2 as act2
import Actividad1 as act1
import matplotlib.pyplot as plt

def main():

    #Actividad 1
    print("Ejecutando funciones de Actividad 1 (Casos de COVID por país):\n")

    # Crear la figura y los subgráficos para Actividad 1
    fig, axs = plt.subplots(3, 1, figsize=(12, 18))

    # Llamar a las funciones de Actividad 1 para generar los gráficos en subgráficos
    act1.punto_uno(axs[0])
    act1.punto_dos(axs[1])
    act1.punto_tres(axs[2])

    # Ajustar el diseño para evitar superposiciones y mostrar el gráfico completo
    plt.tight_layout()
    plt.show()

    #Actividad 2
    print("\n MOSTRANDO ACTIVIDAD 2")
    print()

    print("Ejecutando funciones de Actividad 2 (Datos de ciudades):\n")

    # Llamar a las funciones individuales de Actividad 2 para mostrar gráficos circulares
    act2.mostrar_poblacion_por_ciudad()
    act2.mostrar_densidad_por_km2()
    act2.mostrar_densidad_por_m2()
    print("\n MOSTRANDO ACTIVIDAD 3")
    print()
    ## actividad 3


    ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

    # Llamar a las funciones de `Actividad3` para obtener datos
    clock_speeds = act3.m_clock_speed(ids)
    megapixels = act3.m_megapixels(ids)
    battery_power = act3.m_battery_power(ids)
    print()
    # Gráfico de clock speed
    plt.figure(figsize=(10, 5))
    plt.bar(clock_speeds['id'], clock_speeds['clock_speed'], color='blue')
    plt.xlabel('ID del móvil')
    plt.ylabel('Clock Speed')
    plt.title("Clock Speed según el ID del móvil")
    plt.legend(['Clock Speed'])
    plt.show()
    print()
    # Gráfico de megapixels
    plt.figure(figsize=(10, 5))
    plt.bar(megapixels['id'], megapixels['pc'], color='green')
    plt.xlabel('ID del móvil')
    plt.ylabel('Megapixels')
    plt.title("Megapixels según el ID del móvil")
    plt.legend(['Megapixels'])
    plt.show()
    print()
    # Gráfico de battery power
    plt.figure(figsize=(10, 5))
    plt.bar(battery_power['id'], battery_power['battery_power'], color='red')
    plt.xlabel('ID del móvil')
    plt.ylabel('Battery Power')
    plt.title("Battery Power según el ID del móvil")
    plt.legend(['Battery Power'])
    plt.show()

if __name__ == "__main__":
    main()
