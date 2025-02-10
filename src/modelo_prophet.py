import pandas as pd
import matplotlib.pyplot as plt
import os
from prophet import Prophet

df = pd.read_csv(r"data_prosseced\test_set_Preproceced_090225_V1.0.0_JT.csv", low_memory=False)

df['start_date'] = pd.to_datetime(df['start_date'])

df['year'] = df['start_date'].dt.year
df['month'] = df['start_date'].dt.month
df['day_of_week'] = df['start_date'].dt.day_name()

total_trips_per_year = df.groupby('year').size().reset_index(name='total_trips')

plt.figure(figsize=(10, 6))
plt.plot(total_trips_per_year['year'], total_trips_per_year['total_trips'], marker='o')
plt.title('Conteo de Viajes en el sistema compartido de bicilcetas, ciudad: LA\n Periodo data-set: 2016-2021')
plt.xlabel('Año')
plt.ylabel('Total de Viajes')
plt.xticks(total_trips_per_year['year']) 
plt.grid()
plt.tight_layout()
plt.show()

total_trips_per_day = df.groupby('start_date').size().reset_index(name='total_trips')

total_trips_per_day.columns = ['ds', 'y']

model = Prophet(weekly_seasonality=True, yearly_seasonality=True)
model.fit(total_trips_per_day)

future = model.make_future_dataframe(periods=1095) 
forecast = model.predict(future)
fig = model.plot_components(forecast)

for ax in fig.axes:
    ax.set_xlabel('Período', fontsize=12)  
    ax.set_ylabel('Total de Viajes', fontsize=12)  
    ax.grid(True)  

fig.axes[0].set_title('Tendencia en el data-set y proyección a 3 años\n', fontsize=14)
fig.axes[1].set_title('Tendencia Semanal, Periodo: 2016-2021', fontsize=14)
fig.axes[2].set_title('Tendencia Anual, Periodo: 2016-2021', fontsize=14)

plt.suptitle('Tendencias en el sistema compartido de bicicletas, ciudad: LA\n Periodo: 2016-2021', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.savefig('grafic/Modelo_analitcico_Prophet_Tendencias.png')
plt.show()

fig2 = model.plot(forecast)
plt.title('Predicción a 3 años de la tendencia Semanal en el uso del sistema Bicicletas compartidas\n Ciudad: LA', fontsize=16)
plt.xlabel('Fecha', fontsize=14)
plt.ylabel('Total de Viajes', fontsize=14)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  
plt.savefig('grafic/Modelo_analitcico_Prophet_Tendencias_actuales.png')
plt.show()

annual_forecast = forecast.resample('Y', on='ds').sum() 
plt.figure(figsize=(10, 6))
plt.bar(annual_forecast.index.year, annual_forecast['yhat'], color='skyblue', label='Predicción Anual')
plt.title('Predicción a 3 años (2022-2024) en el uso del sistema de bicicletas\n compartidas Ciudad: LA', fontsize=16)
plt.xlabel('Año', fontsize=14)
plt.ylabel('Total de Viajes', fontsize=14)
plt.xticks(annual_forecast.index.year)  
plt.grid()
plt.tight_layout()
plt.legend()
plt.savefig('grafic/Modelo_analitcico_Prophet_predicción_3años.png')
plt.show()
