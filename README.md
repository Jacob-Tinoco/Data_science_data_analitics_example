## Estructura del Proyecto:

```
Solución_prueba_tecnica_100225_V1.5.0_JT/
│
├── data/
│   ├── train_set.csv
│   ├── test_set.csv
│   └── sample_submission.csv
│
├── data_prosseced
│   ├── test_set_Preproceced_090225_V1.0.0_JT
│   
├── grafic/
│   ├── conteo_viajes_por_año.png
│   ├── distribucion_duracion_viajes.png
|   ├── distribucion_duracion_(año).png
|   ├── ...
|   ├── Modelo_analitcico_Prophet_predicción_3años.png
│   ├── Modelo_analitcico_Prophet_Tendencias.png
│   ├── Modelo_analitcico_Prophet_Tendencias_actuales.png
|   └── Modelo_analitico_(LR).png
│
├── notebook/  
│   └── notebook.ipynb
│
├── src/
│   ├── estaciones_saturadas.py
│   ├── grafic_lines.py
│   ├── horarios_saturados.py
│   ├── modelo_LR.py
│   ├── modelo_prophet.py
│   ├── modelo_prophet.py
│   └── visualización_general.py
│
├── README.md
└── requirements.txt

```

### Descripción de la Estructura

- **data/**: Contiene los conjuntos de datos utilizados en el análisis para el preprocesamiento.
- data_prosseced**/**: Contiene los conjuntos preprocesados.
- **grafic/**: Almacena las gráficas generadas a partir del análisis.
- **notebook/:** Incluye el Jupyter Notebooks con los codigos de prueba para el análisis exploratorio y los modelos analíticos.
- **notebook/grafic/**: Almacena las gráficas generadas a partir del análisis.
- **src/**: Contiene los scripts para visualizaciones del análisis exploratorio y modelos analíticos.
- [**README.md**](http://readme.md/): Documento que proporciona una visión general del proyecto y sus objetivos.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.