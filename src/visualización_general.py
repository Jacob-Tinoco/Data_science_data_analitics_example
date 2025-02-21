import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"data_prosseced\test_set_Preproceced_090225_V1.0.0_JT.csv", low_memory=False)
df['start_date'] = pd.to_datetime(df['start_date'])
df['year'] = df['start_date'].dt.year
total_trips_per_year = df.groupby('year').size().reset_index(name='total_trips')

plt.figure(figsize=(10, 6))
plt.plot(total_trips_per_year['year'], total_trips_per_year['total_trips'], marker='o')
plt.title('Conteo de Viajes en el sistema compartido de bicicletas, ciudad: LA', fontsize=16, loc='center', pad=20)
plt.text(0.5, 1.02, 'Periodo data-set: 2016-2021', fontsize=12, ha='center', va='center', transform=plt.gca().transAxes)
plt.xlabel('Año')
plt.ylabel('Total de Viajes')

for i in range(len(total_trips_per_year)):
    plt.text(total_trips_per_year['year'][i] + 0.1, total_trips_per_year['total_trips'][i],  # Ajustar la posición horizontal
             str(total_trips_per_year['total_trips'][i]), ha='left', va='center', fontsize=9)

plt.xticks(total_trips_per_year['year'])  
plt.grid()
plt.tight_layout()

if not os.path.exists('grafic'):
    os.makedirs('grafic')

plt.savefig('grafic/conteo_viajes_por_año.png')
plt.show()