import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"", low_memory=False)
df = df.dropna()  
df_filtered = df[(df['duration'] >= 0) & (df['duration'] <= 60)]

if not os.path.exists('grafic'):
    os.makedirs('grafic')

plt.figure(figsize=(10, 6))
sns.histplot(df_filtered['duration'], bins=30, kde=True)
plt.title('Distribución de la Duración de los Viajes (0 a 60 minutos)')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')
plt.xlim(0, 60) 
plt.tight_layout()
plt.savefig('grafic/distribucion_duracion_viajes.png')
plt.close()
