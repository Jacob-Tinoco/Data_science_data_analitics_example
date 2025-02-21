import pandas as pd

df = pd.read_csv(r"data_prosseced\test_set_Preproceced_090225_V1.0.0_JT.csv", low_memory=False)

station_pairs = df.groupby(['start_station', 'end_station']).size().reset_index(name='count')
top_routes = station_pairs.sort_values('count', ascending=False).head(10)


print('Top 10 rutas más utilizadas:')
print(top_routes)

for idx, route in top_routes.iterrows():
    start_station = route['start_station']
    end_station = route['end_station']
    filtered_data = df[(df['start_station'] == start_station) & (df['end_station'] == end_station)]
    filtered_data['hour'] = pd.to_datetime(filtered_data['start_time']).dt.hour
    hourly_counts = filtered_data.groupby(['start_station', 'end_station', 'hour', 'passholder_type']).size().reset_index(name='count')
    top_hours = hourly_counts.sort_values('count', ascending=False).head(4)
    
    print(f'\nTop 4 horarios más saturados para la ruta iniciando en: {start_station} ->  concluyendo en: {end_station}:')
    print(top_hours)