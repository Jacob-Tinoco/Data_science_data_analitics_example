import pandas as pd
import numpy as np

# Cargar el conjunto de datos
df = pd.read_csv(r"C:\Users\jacob\OneDrive\Escritorio\Python\Tecnical_TEXT_04.02.35\Solución_prueba_tecnica_100225_V1.5.0_JT\data_prosseced\test_set_Preproceced_090225_V1.0.0_JT.csv", low_memory=False)

# Agrupar los datos por estación de origen y destino
station_pairs = df.groupby(['start_station', 'end_station']).size().reset_index(name='count')
station_pairs = station_pairs.sort_values('count', ascending=False)

# Mostrar las 10 rutas más utilizadas
print('Rutas más utilizadas:')
print(station_pairs.head(10))

# Número total de viajes
total_trips = len(df)
print(f'Número total de viajes: {total_trips}')

# Duración media de los viajes
mean_duration = df['duration'].mean()
print(f'Duración media de los viajes: {mean_duration:.2f} minutos')

# Frecuencia de uso por estación
station_usage = df.groupby('start_station').size().reset_index(name='count')
station_usage = station_usage.sort_values('count', ascending=False)
print('Frecuencia de uso por estación:')
print(station_usage)

# Ordenar las estaciones por el número total de viajes
top_stations_by_trips = station_usage.sort_values('count', ascending=False)
print('Estaciones más concurridas por número de viajes:')
print(top_stations_by_trips.head(10))

# Ordenar las estaciones por la duración media de los viajes
station_durations = df.groupby('start_station')['duration'].mean().reset_index(name='mean_duration')
top_stations_by_duration = station_durations.sort_values('mean_duration', ascending=False)
print('Estaciones más concurridas por duración media de los viajes:')
print(top_stations_by_duration.head(10))