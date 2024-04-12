🎯

🎯

🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯

## Machine Learning Operations de Steam Games

TODO EN INGLES

1 TITULO, PORTADA,IDENTIFICACION

2 Declaracion de importaciones

3 Breve indice de archivos del documento

4 1_AnalisisEda.ipynb

5 Archivos unicamente necesarios en la carpeta

FOTO TOPE

# 🎮SteamGames MLOps+ FastAPI

### 🌐 Contexto:

💼 Soy un Cientifico de Datos que trabaja para Steam, una plataforma multinacional de videojuegos y lleve a cabo este trabajo en un lapso de 7 dias:

**🤖 Implementacion de un sistema de recomendación de videojuegos para usuarios**

- 🤖 1_ Modelo con relación **ítem-ítem**:

  - toma un juego, en base a que tan similar esa ese juego al resto, recibimos una lista con 5 juegos recomendados similares al ingresado.
- 🤖 2_ Modelo con relación **user-item:**

  - toma un usuario, se encuentran usuarios similares, recibimos una lista con 5 juegos recomendados para dicho usuario.

En general se explican como**“A usuarios que son similares a tí también les gustó…**”.

📂 **La fuente de datos para este proyecto:**

- - **📂 steam_games.json**
  - **📂 users_items.json**
  - **📂 user_reviews.json**
  - Visualiza la informacion de estos datos tocando ACA

### 🎯Objetivos y roles:

- **`🛠️` Data Engineer:** Limpiar y preparar los 📂 dataset de Steam para el análisis.
- **`🤖` Machine Learning Operations:** Implementar un sistema de recomendación de videojuegos para usuarios..
- 🌐 **API**: con endpoints que proporcionarán acceso a los resultados.
- 📹 **VideoDemo:**

Este sistema se basa en el procesamiento y exploración de datos, incluyendo características como XXXX.

**🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯**

**FOTO GRAFICO FLUJO DE TRABAJO**

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=400>
</p>

🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯


## 🛠️Data Engineer - ETL

### **🛠️ ETL (Extract, Transform, Load)**

#### **📦 EXTRACT**

**La fuente de datos para este proyecto fueron** 📂 **3 archivos JSON comprimidos en gz,**

Puedes ver la informacion de estos archivos mirando el diccionario de datos tocando **ACA**

Estos archivos son descomprimidos, limpiados, transformados, y exportados en formato parquet.

#### 🔄 **TRANsFORM** 

#### **🔌 Las columnas que vamos a requerir para nuestras funciones son:**

1. 🌐 `developer(desarrollador: str)`:

   - **📂 steam_games.json**: developer, release_date, price
2. `🌐 userdata(User_id)`:

   - **📂 user_reviews.json**: user_id, recommend, helpful.total
   - **📂 users_items.json**: user_id, items_count
3. `🌐 UserForGenre(genero)`:

   - **📂 steam_games.json**:  id, release_date, genres
   - **📂 users_items.json**: user_id, item
4. `🌐 best_developer_year(año: int)`:

   - **📂 steam_games.json**: developer, release_date, id.-
   - **📂 user_reviews.json**: item_id, recommend
5. 🌐 `developer_reviews_analysis(desarrolladora: str)`:

   - **📂 steam_games.json**: developer, release_date, price.
   - **📂 user_reviews.json**: item_id, sentiment_analysis

**🔄 Preparamos los dataset de Steam para la correcta lectura.**

    🗑️ ✅ Eliminados columnas irrelevantes para optimizar el rendimiento de la API.

    🗑️ ✅ Eliminados datos faltantes o nulos

    🗑️ ✅ Eliminados registros o filas repetidas

📂 1_ **steam_games.json**:

- `release_date`:

  - Se extrae el año de la fecha en la columna 'release_date' y ~~se agrega como una nueva columna `'year'` .~~
  - 🔄 Se convierte en un tipo de dato datetime.
- 🔄 `app_name` en string
- 🔄 `tags` en string
- 🔄 `ID `en str
- 🗃️ `Genres `: Rellenamos la informacion faltante de genres en cada juego, con los genres disponibles en la columna tag

📂 2_ **users_items.json**:

- 🗃️ `Items `**:** Desanidado: eran una lista de diccionarios
- 🔄 `Playtime_forever `: Transformamos los minutos a horas

📂 3_ **user_reviews.json:**

- 🗑️ Eliminado `reviews_funny`
- 🗑️ Eliminado `reviews_last_edited `
- `reviews_posted:`
  - Extraemos de las fechas el año en formato YYYY
  - Cambiamos de string a int
- 🗃️ `reviews`: Desanidado: era una lista de diccionarios

Se pueden visualizar las transformaciones y los análisis realizados [aquí](https://github.com/Angiea18/1-proyecto-individual-MLOps/blob/main/steam_games_ML.ipynb)

### **📤 LOAD - CARGAR**

📁 Exportamos los archivos en formato parquet por su **peso, eficiencia en la lectura o escritura de datos y acelerando **las consultas.****

## PENDIENTE

- 
- ~~La columna `'metascore'` se convierte en valores numéricos, ya que contenía puntajes en formato de texto.~~
- Se realizan cambios en la columna `'price'`:
  - Los valores que indican gratuidad se reemplazan con 0.
  - Los valores que comienzan con 'Starting at $' se reemplazan por el valor numérico correspondiente.
  - Los valores no numéricos se reemplazan por NaN.

## 🔌 Deployment API RESTful

🚀 Desplegar la API en Render, Railway o cualquier otro servicio similar.

🌐 El sistema se implementa como una **API** a traves del Framework **FastAPI** , lo que permite a los usuarios interactuar con el modelo a través de solicitudes HTTP.

🚀 Para este proyecto, la API ofrece la funcionalidad para obtener la informacion de los siguientes 5 endpoints :

1. 🌐 `b`:Devuelve la cantidad de ¿items? y porcentaje de contenido Free por año según empresa desarrolladora

   1. 📂 Usa steam_games.json: developer, release_date, price
2. `🌐 `: Dinero gastado por el usuario, porcentaje de recomendación y cantidad de items.

   1. 📂 user_reviews.json: user_id, recommend, helpful.total
   2. 📂 users_items.json: user_id, items_count
3. `🌐 UserForGenre(genero)`: Usuario con más horas jugadas para el género dado y acumulación de horas jugadas por año de lanzamiento.

   1. 📂 steam_games.json:  id, release_date, genres
   2. 📂 users_items.json: user_id, item
4. `🌐 best_developer_year(año: int)`: Top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado.

   1. 📂 steam_games.json: developer, release_date, id.
   2. 📂 user_reviews.json: item_id, recommend
5. 🌐 `developer_reviews_analysis(desarrolladora: str)`: Diccionario con el nombre del desarrollador y la cantidad de reseñas positivas y negativas.-

   1. 📂 steam_games.json: developer, release_date, price.
   2. 📂 user_reviews.json: item_id, sentiment_analysis

🔌 El código para ejecutar la API en FastAPI **ACA** .

🔗 Explora la API **ACA** 😃

🛠️ Una vez que toda la data limpia es consumible por la API:

## 🤖 Machine Learning Operations

🤖 Comenzamos con un análisis exploratorio de datos (EDA)  para entender bien los datos a los que tenemos acceso.

#### EDA (Análisis Exploratorio de Datos)

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
- 

**🛠️Feature engineering**

- 📂 user_reviews.json: La columna "sentiment_analysis" se ha creado para las reseñas de los usuarios aplicando análisis de sentimiento con NLP en el dataset

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

## 📺 Video demo

📺 Para obtener información detallada sobre los pasos del proceso y una explicación más profunda.

📹 Disfruta la demostracion del funcionamiento de la API y del modelo de ML en el siguiente enlace:  (Duración: x minutos).

¡Disfruta del video! 😊
