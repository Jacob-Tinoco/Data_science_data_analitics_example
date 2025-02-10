import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar el conjunto de datos
df = pd.read_csv(r"data_prosseced\test_set_Preproceced_090225_V1.0.0_JT.csv", low_memory=False)

# Asegurarse de que la columna 'start_date' esté en formato de fecha
df['start_date'] = pd.to_datetime(df['start_date'])

# Extraer el año de la columna 'start_date'
df['year'] = df['start_date'].dt.year

# Contar los viajes totales por año
total_trips_per_year = df.groupby('year').size().reset_index(name='total_trips')

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(total_trips_per_year['year'], total_trips_per_year['total_trips'], marker='o')
plt.title('Predicción a 3 años de Viajes en el sistema compartido de bicilcetas, ciudad: LA\n Periodo data-set: 2016-2021')
plt.xlabel('Año')
plt.ylabel('Total de Viajes')
plt.xticks(total_trips_per_year['year'])  # Asegurarse de que se muestren todos los años
plt.grid()
plt.tight_layout()

# Crear la carpeta 'grafic' si no existe
if not os.path.exists('grafic'):
    os.makedirs('grafic')

# Guardar el gráfico en la carpeta 'grafic'
plt.savefig('grafic/conteo_viajes_por_año.png')

# Mostrar el gráfico
plt.show()


