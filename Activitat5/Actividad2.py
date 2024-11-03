import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("Archivos/List of world cities by population density.csv")

# Limpiar los datos: extraer solo números y convertir a tipo numérico
df['Population'] = df['Population'].str.extract('(\d+)').astype(float)
df['Density (/km²)'] = pd.to_numeric(df['Density (/km²)'], errors='coerce')
df['Area (km²)'] = pd.to_numeric(df['Area (km²)'].str.extract('(\d+\.\d+)')[0], errors='coerce')

# Seleccionar solo las primeras 10 ciudades
df_10ciudades = df.head(10).copy()


# Función para mostrar el total de población por ciudad
def mostrar_poblacion_por_ciudad():
    total_poblacion = df_10ciudades[['City', 'Population']].dropna()
    print("Total de población por ciudad:")
    print(total_poblacion)
    plt.figure(figsize=(8, 8))
    plt.pie(total_poblacion['Population'], labels=total_poblacion['City'], autopct='%1.1f%%')
    plt.title("Total de población por ciudad")
    plt.legend(total_poblacion['City'], loc="best")
    plt.show()


# Función para mostrar la densidad de población por km² por ciudad
def mostrar_densidad_por_km2():
    densidad_por_ciudad = df_10ciudades[['City', 'Density (/km²)']].dropna()
    print("Densidad de población por km² por ciudad:")
    print(densidad_por_ciudad)
    plt.figure(figsize=(8, 8))
    plt.pie(densidad_por_ciudad['Density (/km²)'], labels=densidad_por_ciudad['City'], autopct='%1.1f%%')
    plt.title("Densidad de población por km² por ciudad")
    plt.legend(densidad_por_ciudad['City'], loc="best")
    plt.show()


# Función para mostrar la densidad de población por m² por ciudad
def mostrar_densidad_por_m2():
    df_10ciudades.loc[:, 'Density (/m²)'] = df_10ciudades[
    'Density (/km²)'] / 1_000_000  # Convertir densidad de km² a m²
    densidad_por_m2 = df_10ciudades[['City', 'Density (/m²)']].dropna()
    print("Densidad de población por m² por ciudad:")
    print(densidad_por_m2)
    plt.figure(figsize=(8, 8))
    plt.pie(densidad_por_m2['Density (/m²)'], labels=densidad_por_m2['City'], autopct='%1.1f%%')
    plt.title("Densidad de población por m² por ciudad")
    plt.legend(densidad_por_m2['City'], loc="best")
    plt.show()


