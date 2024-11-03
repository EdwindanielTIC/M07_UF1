import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("Archivos/Mobile_price (2).csv")

# Función para obtener el clock speed según el ID del móvil
def m_clock_speed(ids):
    clock_speeds = df[df['id'].isin(ids)][['id', 'clock_speed']]
    print(clock_speeds)
    return clock_speeds

# Función para obtener los megapíxeles según el ID del móvil
def m_megapixels(ids):
    megapixels = df[df['id'].isin(ids)][['id', 'pc']]
    print(megapixels)
    return megapixels

# Función para obtener la batería según el ID del móvil
def m_battery_power(ids):
    battery_power = df[df['id'].isin(ids)][['id', 'battery_power']]
    print(battery_power)
    return battery_power
