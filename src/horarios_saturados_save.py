import pandas as pd

# Leer el archivo CSV original
df = pd.read_csv(r"data_prosseced\test_set_Preproceced_090225_V1.0.0_JT.csv", low_memory=False)

# Agrupar por estaciones de inicio y fin
station_pairs = df.groupby(['start_station', 'end_station']).size().reset_index(name='count')
top_routes = station_pairs.sort_values('count', ascending=False).head(10)

# Crear una lista para almacenar los resultados
results = []

print('Top 10 rutas más utilizadas:')
print(top_routes)

# Iterar sobre las rutas más utilizadas
for idx, route in top_routes.iterrows():
    start_station = route['start_station']
    end_station = route['end_station']
    filtered_data = df[(df['start_station'] == start_station) & (df['end_station'] == end_station)]
    filtered_data['hour'] = pd.to_datetime(filtered_data['start_time']).dt.hour
    hourly_counts = filtered_data.groupby(['start_station', 'end_station', 'hour', 'passholder_type']).size().reset_index(name='count')
    top_hours = hourly_counts.sort_values('count', ascending=False).head(4)
    
    print(f'\nTop 4 horarios más saturados para la ruta iniciando en: {start_station} -> concluyendo en: {end_station}:')
    print(top_hours)

    # Agregar los resultados a la lista
    for _, hour_route in top_hours.iterrows():
        results.append({
            'start_station': start_station,
            'end_station': end_station,
            'hour': hour_route['hour'],
            'passholder_type': hour_route['passholder_type'],
            'count': hour_route['count']
        })

# Crear un DataFrame a partir de los resultados
results_df = pd.DataFrame(results)

# Guardar los resultados en un archivo CSV
results_df.to_csv('top_routes_hours.csv', index=False, header=True)
