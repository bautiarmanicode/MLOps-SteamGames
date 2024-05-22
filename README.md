 datos) FOTO TOPE

## Steam Games Machine Learning Operations + FastAPI

### ❌🌐 Contexto:

~~❌💼 Soy un Cientifico de Datos que trabaja para Steam, una plataforma multinacional de videojuegos y lleve a cabo este trabajo en un lapso de 7 dias:~~

### 🎯Objetivos y roles:

- **🛠️ Data Engineer:** Limpiar y preparar los 📂 dataset de Steam para el análisis.
- **`🤖` Machine Learning Operations:** Implementar un sistema de recomendación de videojuegos para usuarios..

  - 🤖 1_ Modelo con relación **ítem-ítem**: toma un juego, en base a que tan similar esa ese juego al resto, recibimos una lista con 5 juegos recomendados similares al ingresado.
  - 🤖 2_ Modelo con relación **user-item:** toma un usuario, se encuentran usuarios similares, recibimos una lista con 5 juegos recomendados para dicho usuario.
  - En general se explican como:“A usuarios que son similares a tí también les gustó…”.

* 🌐 **API**: con endpoints que proporcionarán acceso a los resultados.

## **❌GRAFICO FLUJO DE TRABAJO**

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=400>
</p>

## PRIMERA ETAPA: Data Engineer

### 🛠️Empezamos por el proceso **ETL (📦 Extract, 🔄 Transform, 📤 Load)**

1. **📦 Extraccio**n de datos
   1. La fuente de datos para este proyecto fueron 3 **📂 archivos JSON** comprimidos en gz
   2. Puedes ver el **diccionario de datos** de estos archivos tocando [aquí](https://github.com/bautiarmanicode/MachineLearning/blob/main/Diccionario_de_datos.md).
2. 🔄 **Transformacion de los datos:** Preparamos los dataset de Steam para la correcta lectura:
   1. Eliminados columnas irrelevantes para optimizar el rendimiento de la API.
   2. Eliminados datos faltantes o nulos
   3. Eliminados registros o filas repetidas
   4. Transformaciones en los tipos de datos.
3. **📤 Carga de datos limpios**
   1. Exportamos los archivos en formato parquet por su **peso, eficiencia en la lectura o escritura de datos y acelerando **las consultas.	****
   2. Se puede visualizar el proceso 🛠️ ETL en los siguientes links:
      1. [🛠️ ETL 📂 steam_games.json](https://github.com/bautiarmanicode/MLOps-SteamGames/blob/main/1_JupyterNotebooks/1.1_ETL_steam_games.ipynb)
      2. [🛠️ ETL 📂 users_items.json](https://github.com/bautiarmanicode/MachineLearning/blob/main/1_JupyterNotebooks/1.2_ETL_user_items.ipynb)
      3. [🛠️ ETL 📂 user_reviews.json](https://github.com/bautiarmanicode/MachineLearning/blob/main/1_JupyterNotebooks/1.3_ETL_user_reviews.ipynb)

## 🌐 Desarrollo de API RESTful Render

El sistema se implementa como una **API** a traves del Framework **FastAPI** , lo que permite a los usuarios interactuar con el modelo a través de solicitudes HTTP.

**La API ofrece la funcionalidad para obtener la informacion de los siguientes 5 endpoints** :

1. 🌐 `developer(desarrollador:str)`: Devuelve la cantidad de juegos y porcentaje de contenido Free por año según la empresa desarrolladora
2. 🌐 `userdata(User_id:str): `Dinero gastado por el usuario, porcentaje de recomendación y cantidad de items.
3. `🌐 UserForGenre(genero)`: Usuario con más horas jugadas para el género dado y acumulación de horas jugadas por año de lanzamiento.
4. `🌐 best_developer_year(año: int)`: Top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado.
5. 🌐 `developer_reviews_analysis(desarrolladora: str)`: Diccionario con el nombre del desarrollador y la cantidad de reseñas positivas y negativas.

El desarrollo del codigo para estas funciones se encuentra en [2_FeatureEngineering_Funciones_Api.ipynb](https://github.com/bautiarmanicode/MLOps-SteamGames/blob/main/1_JupyterNotebooks/2_FeatureEngineering_Funciones_Api.ipynb) .

El codigo para generar la api se encuentra en [main.py](https://github.com/bautiarmanicode/MLOps-SteamGames/blob/main/main.py)

Las funciones de la api se encuentran desarrolladas en [funciones_api.py](https://github.com/bautiarmanicode/MLOps-SteamGames/blob/main/funciones_api.py)

#### **Pasos para ejecutar la api desde localHost:**

1. 📥 **Clonar el Proyecto:** Usa `git clone https://github.com/` para descargar el proyecto. ❌
2. 🛠️ **Preparar el Entorno de Trabajo:**
   * Crea un entorno virtual con `Python -m venv venv`.
   * Activa el entorno con `venv\Scripts\activate`.
   * Instala las dependencias con `pip install -r requirements.txt`.
3. ▶️ **Ejecutar el Servidor:**
   * Inicia el servidor ejecutando `uvicorn main:app --reload` desde la consola.
4. 🌐 **Acceder al Servidor:**
   * Haz clic en la dirección mostrada en la consola ([http://XXX.X.X.X:XXXX](http://xxx.x.x.x:XXXX/)).
5. 📄 **Explorar la Documentación:**
   * Agrega `/docs` en el navegador para acceder a ReDoc y explorar la documentación.
6. 🛠️ **Probar las Funciones:**
   * En cada función, haz clic en  *Try it out* , ingresa los datos necesarios o usa los ejemplos predeterminados, y luego ejecuta y observa la respuesta.

### 🌐 Deployment en Render

[Pagina web Render](https://render.com/) : (nube unificada para aplicaciones y sitios web)

**Objetivo:** Despliegue automático desde GitHub

1. Creamos un nuevo servicio en Render, conectado a este repositorio.
2. Conectamos Render con nuestro repositorio de GitHub.
3. Nuestro servicio está corriendo en: [Deployment Render](https://machinelearning-xb5s.onrender.com)   ❌

**Detalles adicionales:**

* Para ahorrar espacio en el plan gratuito de Render, utilizamos un repositorio exclusivo para el despliegue (aquí [Github Deployment Render](https://github.com/bautiarmanicode/MachineLearningRENDERDEPLOY)). ❌
* 🛠️ Una vez que toda la data limpia es consumible por la API: EDA(Analisis exploratorio de Datos) ❌

## Segunda etapa:🤖 Machine Learning Operations

🤖 Comenzamos con un análisis exploratorio de datos (EDA)  para entender bien los datos a los que tenemos acceso.

#### ❌EDA (Análisis Exploratorio de Datos)

Realizamos visualizaciones utilizando las librerías seaborn y matplotlib para comprender la distribución y relaciones entre las características del conjunto de datos

- investigar las relaciones entre las variables del dataset
- identificar posibles valores atípicos o anomalías
- descubrir patrones interesantes que puedan ser dignos de exploración en análisis futuros. 📊🔍
- Se generó una *nube de palabras* a partir de los títulos de los juegos para visualizar las palabras más frecuentes en ellos.

**🛠️Feature engineering**

- 📂 user_reviews.json: La columna "sentiment_analysis" se ha creado para las reseñas de los usuarios aplicando análisis de sentimiento con NLP en el dataset

🛠️ Una vez que toda la data esta limpia nuestro **EDA** nos permite entender bien los datos a los que tenemos acceso

- investigar las relaciones entre las variables del dataset
- identificar posibles valores atípicos o anomalías
- descubrir patrones interesantes que puedan ser dignos de exploración en análisis futuros. 📊🔍
- nubes de palabras

❌❌❌❌❌❌❌❌❌❌❌❌❌❌

#### Opcion 1

Para el modelo de predicción **Machine Learning** se utilizó del dataset X las características **'x'**, **'x'** y **'x'** para predecir el **`''`** de los X de Steam.

Creación del modelo:

- ~~Se eliminaron las filas con valores faltantes en las columnas de interés ('genres', 'metascore', 'year').~~
- ~~Se aplicó *one-hot encoding* para convertir las variables categóricas 'genres' en variables numéricas.~~
- ~~Los datos se dividieron en conjuntos de entrenamiento y prueba.~~
- ~~Se creó un modelo de regresión lineal múltiple y se utilizó como base para el modelo Bagging.~~
- ~~Se entrenó el **`modelo Bagging`** utilizando el ensamble de 10 modelos de regresión lineal.~~

Evaluación del modelo:

- ~~Se realizaron predicciones en el conjunto de prueba utilizando el modelo Bagging.~~
- ~~Se calculó el **`RMSE`** utilizando las predicciones y los valores reales del precio de los videojuegos en el conjunto de prueba.~~
- ~~Se guardó el modelo Bagging entrenado en un archivo llamado "modelo_bagging.pkl" utilizando la librería **`pickle`**.~~

### Opcion 2

### Modelo de aprendizaje automático

~~Se crearon dos modelos de recomendación, que generan cada uno, una lista de 5 juegos ya sea ingresando el nombre de un juego o el id de un usuario.~~

~~En el primer caso, el modelo tiene una relación ítem-ítem, esto es, se toma un juego y en base a que tan similar es ese juego con el resto de los juegos se recomiendan similares. En el segundo caso, el modelo aplicar un filtro usuario-juego, es decir, toma un usuario, encuentra usuarios similares y se recomiendan ítems que a esos usuarios similares les gustaron.~~

~~Para generar estos modelos se adoptaron algoritmos basados en la memoria, los que abordan el problema del **filtrado colaborativo** utilizando toda la base de datos, tratando de encontrar usuarios similares al usuario activo (es decir, los usuarios para los que se les quiere recomendar) y utilizando sus preferencias para predecir las valoraciones del usuario activo.~~

~~Para medir la similitud entre los juegos (item_similarity) y entre los usuarios (user_similarity) se utilizó la **similitud del coseno** que es una medida comúnmente utilizada para evaluar la similitud entre dos vectores en un espacio multidimensional. En el contexto de sistemas de recomendación y análisis de datos, la similitud del coseno se utiliza para determinar cuán similares son dos conjuntos de datos o elementos, y se calcula utilizando el coseno del ángulo entre los vectores que representan esos datos o elementos.~~

~~El desarrollo para la creación de los dos modelos se presenta en la Jupyter Notebook~~ [04_Modelo_recomendacion](https://github.com/IngCarlaPezzone/PI1_MLOps_videojuegos/blob/main/JupyterNotebooks/04_Modelo_recomendacion.ipynb).

🔧 Además, el proyecto incorpora técnicas de **MLOps** para asegurar la reproducibilidad y mantenibilidad del modelo.

Esto incluye el uso de entornos virtuales para aislar dependencias y la automatización de tareas de entrenamiento y despliegue mediante scripts y comandos de terminal.

❌❌❌❌❌❌❌❌❌❌❌❌❌

## 📺 Video demo

📺 Para obtener información detallada sobre los pasos del proceso y una explicación más profunda.

📹 Disfruta la demostracion del funcionamiento de la API y del modelo de ML en el siguiente enlace:  (Duración: x minutos).

¡Disfruta del video! 😊
