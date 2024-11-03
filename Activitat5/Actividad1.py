import matplotlib.pyplot as plt
import pandas as pd

def punto_uno(ax):
    #Cargar en la variable df los datos del archivo .csv
    df = pd.read_csv("Archivos/df_covid19_countries.csv", usecols=['total_cases', 'location', 'date'])
    
    #Convertir 'date' a datetime y extraer el período del mes
    df['date'] = pd.to_datetime(df['date'])
    df['Mes'] = df['date'].dt.to_period('M')
    
    #Filtrar países y meses
    paises_muestra = ['Peru', 'Spain', 'Paraguay', 'China', 'Uruguay', 'Afghanistan', 'Chile', 'Italy', 'France', 'Russia']
    meses = ['2020-07', '2020-08', '2020-09', '2020-10']
    
    df = df[df['location'].isin(paises_muestra) & df['Mes'].astype(str).isin(meses)]
    
    #Agrupar por casos totales por mes y país
    agrupar = df.groupby(['Mes', 'location'])['total_cases'].sum().unstack()
    
    #Gráfico
    agrupar.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Total de casos mensuales por país")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Total de casos")
    ax.legend(title="País", bbox_to_anchor=(1.05, 1), loc='upper left')

def punto_dos(ax):
    #Cargar el archivo .csv con las columnas necesarias
    df = pd.read_csv("Archivos/df_covid19_countries.csv", usecols=['total_deaths', 'location', 'date'])
    
    #Convertir 'date' a datetime y extraer el período del mes
    df['date'] = pd.to_datetime(df['date'])
    df['Mes'] = df['date'].dt.to_period('M')
    
    #Filtrar países y meses
    paises_muestra = ['Peru', 'Spain', 'Paraguay', 'China', 'Uruguay', 'Afghanistan', 'Chile', 'Italy', 'France', 'Russia']
    meses_2021 = ['2021-01', '2021-02', '2021-03', '2021-04']
    
    df = df[df['location'].isin(paises_muestra) & df['Mes'].astype(str).isin(meses_2021)]
    
    #Agrupar por muertes totales por mes y país
    muertes_por_mes_pais = df.groupby(['Mes', 'location'])['total_deaths'].sum().unstack()
    
    #Gráfico
    muertes_por_mes_pais.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Muertes totales mensuales por país (2021)")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Total de muertes")
    ax.legend(title="País", bbox_to_anchor=(1.05, 1), loc='upper left')

def punto_tres(ax):
    #Cargar el archivo .csv con las columnas necesarias
    df = pd.read_csv("Archivos/df_covid19_countries.csv", usecols=['reproduction_rate', 'location', 'date'])
    
    #Convertir 'date' a datetime y extraer el período del mes
    df['date'] = pd.to_datetime(df['date'])
    df['Mes'] = df['date'].dt.to_period('M')
    
    #Filtrar países y meses
    paises_muestra = ['Peru', 'Spain', 'Paraguay', 'China', 'Uruguay', 'Afghanistan', 'Chile', 'Italy', 'France', 'Russia']
    meses = ['2021-05', '2021-06', '2021-07', '2021-08']
    
    df = df[df['location'].isin(paises_muestra) & df['Mes'].astype(str).isin(meses)]
    
    #Agrupar por tasa de reproducción promedio por mes y país
    tasa_reproduccion_por_mes_pais = df.groupby(['Mes', 'location'])['reproduction_rate'].mean().unstack()
    
    #Gráfico
    tasa_reproduccion_por_mes_pais.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Tasa de reproducción mensual por país")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Tasa de reproducción")
    ax.legend(title="País", bbox_to_anchor=(1.05, 1), loc='upper left')

