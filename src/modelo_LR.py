import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"data_prosseced\test_set_Preproceced_090225_V1.0.0_JT.csv", low_memory=False)

df['start_datetime'] = pd.to_datetime(df['start_date'] + ' ' + df['start_hour'])
df['year'] = df['start_datetime'].dt.year
df['month'] = df['start_datetime'].dt.month
df['day'] = df['start_datetime'].dt.day
df['day_of_week'] = df['start_datetime'].dt.dayofweek 
df['hour'] = df['start_datetime'].dt.hour

total_trips_per_month = df.groupby(['year', 'month']).size().reset_index(name='total_trips')
total_trips_per_month['time'] = total_trips_per_month['year'] + total_trips_per_month['month'] / 12

X = total_trips_per_month[['time']]  
y = total_trips_per_month['total_trips'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Error Cuadrático Medio: {mse}')

future_years_months = []
for year in range(total_trips_per_month['year'].max(), total_trips_per_month['year'].max() + 3):
    for month in range(1, 13): 
        future_years_months.append(year + month / 12)

future_predictions = model.predict(np.array(future_years_months).reshape(-1, 1))

for year_month, prediction in zip(future_years_months, future_predictions):
    year = int(year_month)
    month = int((year_month - year) * 12) + 1
    print(f'Predicción de viajes para {year}-{month:02d}: {prediction}')

plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos Reales')
plt.plot(X_test, y_pred, color='red', label='Predicción')
plt.scatter(future_years_months, future_predictions, color='green', label='Predicción Futura', marker='x')
plt.title('Predicción con LR a 3 años en el sistema de uso compartido de bicicletas',fontsize=16, loc='center', pad=20)
plt.text(0.5, 1.02, 'Ciudad: LA. Periodo data-set: 2016-2021', fontsize=12, ha='center', va='center', transform=plt.gca().transAxes)
plt.xlabel('Periodo')
plt.ylabel('Total de Viajes')
plt.legend()
plt.savefig('grafic/Modelo_analitico_(LR).png')
plt.show()

