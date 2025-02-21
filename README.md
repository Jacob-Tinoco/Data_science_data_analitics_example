# Proyecto: Data science example V2

## Sobre la V2 de este repositorio:
Al crear este repositorio se creó la documentación en un plazo de 2 días por limitaciones de tiempo. Esto de ninguna manera justifica los errores cometidos en la versión anterior. Para esta nueva versión se contó con un plazo de 4 días donde los cambios son: 
- Mejoras en las visualizaciones de los datos: títulos, subtítulos, etiquetas, leyendas, diferenciadores de color, en los casos necesarios.
- Se creó un archivo Word para la elaboración del reporte.
- Dentro del reporte se agregó una portada adecuada a consideración propia.
- Dentro del reporte se agregó un índice.
- Dentro del reporte se cambiaron las visualizaciones de datos (tablas, gráficos, diagramas...).
- Dentro del reporte se corrigieron errores de dedo, ortográficos y cambios en anexos correspondientes a los siguientes puntos.
- Se eliminó en la carpeta src: grafic_lines.py.
- Se agregó dentro de la carpeta src: histograma.py.
- Sobre los dos puntos anteriores, se cambió información en la sección de estructura del proyecto.

Esta nueva versión fue creada para la mejora continua del repositorio. Más adelante actualizaré la versión a una V3, donde utilizaré R para la visualización y análisis de datos.

## Autores

- **Jacob Tinoco** - *Repositorio de educación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)

## Bienvenido
¡Hola! 👋 Bienvenido al repositorio **Data_science_data_analitics_example_V2**. Este proyecto contiene la documentación y respuesta a las requisiciones de una prueba técnica como Data Science.

# Descripción del Repositorio:

Este repositorio contiene el proyecto completo y la documentación relacionada con el análisis de datos y modelado predictivo del sistema de bicicletas compartidas en Los Ángeles, EU. El objetivo principal del proyecto es explorar la demanda del servicio y prever el crecimiento de los planes de uso de bicicletas a través de técnicas de análisis de datos y modelos predictivos.

## Disclaimer
Los datos de entrada fueron proporcionados por parte de una prueba técnica para ser candidato como Data Scientist MD en Arkon Data. Se atribuyen los datos de entrada al perfil de Salvador Garcia en Kaggle.
  
## Estructura del Proyecto:
En este Readme se encuentra el informe_JT.pdf. Dentro del informe no se contempla a sí mismo en la estructura del proyecto.

```
Solución_prueba_tecnica_100225_V1.5.2_JT/
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
│   ├── histograma.py
│   ├── horarios_saturados.py
│   ├── modelo_LR.py
│   ├── modelo_prophet.py
│   ├── modelo_prophet.py
│   └── visualización_general.py
│
├── README.md
├── Informe_JT.pdf
├── Informe_JT.docx
└── requirements.txt

```

### Descripción de la Estructura

- **data/**: Contiene los csv de datos utilizados en el análisis para el preprocesamiento.
- **data_processed/**: Contiene los csv procesados.
- **graphic/**: Almacena las gráficas generadas a partir del análisis.
- **notebook/**: Incluye los Jupyter Notebooks con los códigos de prueba para el análisis exploratorio y los modelos analíticos.
- **notebook/graphic/**: Almacena las gráficas generadas a partir del análisis.
- **src/**: Contiene los scripts para visualizaciones del análisis exploratorio y modelos analíticos.
- [**README.md**](README.md): Documento que proporciona una visión general del proyecto y sus objetivos.
- **Informe_JT.pdf**: Informe con documentación de la prueba técnica en formato pdf.
- **Informe_JT.docx**: Formato Word donde se creó el Informe de la prueba técnica.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.

## Contenido del Repositorio:
- **Datos**: Archivos .csv de datos originales y procesados utilizados en el análisis.
- **Notebooks**: Jupyter Notebooks con el análisis exploratorio de datos (EDA) y la implementación de modelos predictivos.
- **Scripts**: Códigos en Python para la visualización de datos, preprocesamiento y modelos analíticos (Regresión Lineal y Prophet).
- **Gráficos**: Visualizaciones generadas a partir del análisis, incluyendo tendencias, distribución de viajes y predicciones a futuro.
- **Informe**: Documento detallado que describe el proceso, metodología de análisis, resultados y conclusiones del proyecto, en formato .pdf y archivo Word.

## Herramientas y Tecnologías Utilizadas:
- **Librerías**: Pandas, Matplotlib, Seaborn, Scikit-learn, Prophet (Meta).
- **Metodologías**: Análisis Exploratorio de Datos (EDA), Regresión Lineal, Series Temporales (Prophet).

## Resultados Clave:
- Identificación de tendencias de uso del servicio a lo largo del tiempo.
- Predicción de la demanda del servicio para los próximos 3 años.
- Análisis de saturación de estaciones y horarios más concurridos.

# ¿Cómo Usar este Repositorio?
1. Clona el repositorio.
2. Instala las dependencias necesarias (requirements.txt).
3. Explora los notebooks y scripts para replicar el análisis.

## Requerimientos del Repositorio:
Puedes ejecutar en la terminal de tu proyecto el siguiente comando para instalar los requerimientos necesarios. No olvides que para no causar conflictos en tu computadora debes crear una máquina virtual y ahí instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Actualizaciones:
Posteriormente actualizaré este archivo README para proporcionar más detalles sobre el proyecto.

**Fecha de última actualización:** 20/02/25

## Licencia:
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto:
Puedes encontrarme en [LinkedIn](https://www.linkedin.com/in/jacob-t-329675258/) o en [Instagram](https://www.instagram.com/jknc.0/).
