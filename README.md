# Proyecto: Data science example

## Autores

- **Jacob Tinoco** - *Repositorio de educación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)

## Bienvenido
¡Hola! 👋 Bienvenido al repositorio **Data_science_data_analitics_example**. Este proyecto contiene la documentación y respuesta a las requisiciones de una prueba técnica como Data Science

# Descripción del Repositorio:

Este repositorio contiene el proyecto completo y la documentación relacionada con el análisis de datos y modelado predictivo del sistema de bicicletas compartidas en Los Ángeles, EU. El objetivo principal del proyecto es explorar la demanda del servicio y prever el crecimiento de los planes de uso de bicicletas a través de técnicas de análisis de datos y modelos predictivos.

## Disclaimer
Los datos de entrada fueron proporcionados por parte de una prueba técnica para ser candidato como Data Scientist MD en Arkon Data, se atribuyen los datos de entrada al perfil de Salvador Garcia en Kaggle
  
## Estructura del Proyecto:
En este Readme se encuentra el informe_JT.pdf dentro del informe no se contempla a si mismo en la estructura del proyecto. 

```
Solución_prueba_tecnica_100225_V1.5.0_JT/
Data_science_data_analitics_example/
│
├── data/
│   ├── train_set.csv
│   ├── test_set.csv
│   └── sample_submission.csv
│
├── data_prosseced
│   ├── test_set_Preproceced_090225_V1.0.0_JT
│   ├── train_set_Preproceced_070225_V1.1.0_JT.csv
│   └── sample_submission.csv
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
├── Informe_JT.pdf
└── requirements.txt

```

### Descripción de la Estructura

- **data/**: Contiene los csv de datos utilizados en el análisis para el preprocesamiento.
- **data_prosseced/**: Contiene los csv procesados.
- **grafic/**: Almacena las gráficas generadas a partir del análisis.
- **notebook/:** Incluye el Jupyter Notebooks con los codigos de prueba para el análisis exploratorio y los modelos analíticos.
- **notebook/grafic/**: Almacena las gráficas generadas a partir del análisis.
- **src/**: Contiene los scripts para visualizaciones del análisis exploratorio y modelos analíticos.
- [**README.md**](http://readme.md/): Documento que proporciona una visión general del proyecto y sus objetivos.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.

## Contenido del Repositorio:
Datos: Archivos .csv de datos originales y procesados utilizados en el análisis.

Notebooks: Jupyter Notebooks con el análisis exploratorio de datos (EDA) y la implementación de modelos predictivos.

Scripts: Códigos en Python para la visualización de datos, preprocesamiento, y modelos analíticos (Regresión Lineal y Prophet).

Gráficos: Visualizaciones generadas a partir del análisis, incluyendo tendencias, distribución de viajes y predicciones a futuro.

Informe: Documento detallado que describe el proceso, metodología de analisis, resultados y conclusiones del proyecto.

## Herramientas y Tecnologías Utilizadas:

Librerías: Pandas, Matplotlib, Seaborn, Scikit-learn, Prophet (Meta)

Metodologías: Análisis Exploratorio de Datos (EDA), Regresión Lineal, Series Temporales (Prophet)

## Resultados Clave:
Identificación de tendencias de uso del servicio a lo largo del tiempo.

Predicción de la demanda del servicio para los próximos 3 años.

Análisis de saturación de estaciones y horarios más concurridos.

# ¿Cómo Usar este Repositorio?
Clona el repositorio.

Instala las dependencias necesarias (requirements.txt).

Explora los notebooks y scripts para replicar el análisis.

## Requerimientos del Repositorio
 - Puedes ejecutar en la terminal de tu proyecto el siguinte comando para instalar los rquerimientos necesarios, no olvides que para no
  causar conflictos en tu computadora debes crear una maquina virtual y ahi instalar las dependendncias:
  
    ```bash
    pip install -r requirements.txt
     ```
## Actualizaciones
Posteriormente actualizaré este archivo README para proporcionar más detalles sobre el proyecto.

**Fecha de última actualización:** 10/02/25

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto
Puedes encontrarme en [LinkedIn](https://www.linkedin.com/in/jacob-t-329675258/) o en [Instagram](https://www.instagram.com/jknc.0/).
