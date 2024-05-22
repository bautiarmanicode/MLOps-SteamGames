
# 📚 Diccionario de datos para el proyecto:


#### **🎮 australian_user_reviews.json** :

[](https://github.com/bautiarmanicode/MachineLearning-SteamGames/blob/main/00_Diccionario_de_datos.md#-australian_user_reviewsjson-)

* Contiene comentarios de usuarios sobre juegos, recomendaciones, emoticones de gracioso y estadísticas de utilidad.
* Variables:
  * **user_id** 👤: Identificador único del usuario.
  * **user_url** 🔗: URL del perfil del usuario en Steam Community.
  * **reviews** 📝: Lista de diccionarios con revisiones, cada uno con:
    * **funny** 😄: Indica si contiene emoticones de gracioso.
    * **posted** 📅: Fecha de publicación del comentario.
    * **last_edited** 📅: Fecha de la última edición.
    * **item_id** 🎮: Identificador único del juego.
    * **helpful** 👍: Estadísticas de utilidad del comentario.
    * **recommend** 👍👎: Recomendación del juego por el usuario.
    * **review** 💬: Comentario sobre el juego.

#### **🕹️ australian_users_items.json** :

[](https://github.com/bautiarmanicode/MachineLearning-SteamGames/blob/main/00_Diccionario_de_datos.md#%EF%B8%8F-australian_users_itemsjson-)

* Contiene información sobre los juegos jugados por usuarios y el tiempo acumulado.
* Variables:
  * **user_id** 👤: Identificador único del usuario.
  * **items_count** 📊: Cantidad de juegos consumidos por el usuario.
  * **steam_id** 🔢: Número único de la plataforma.
  * **user_url** 🔗: URL del perfil del usuario.
  * **items** 📦: Lista de diccionarios de los juegos consumidos, cada uno con:
    * **item_id** 🎮: Identificador único del juego.
    * **item_name** 🎮: Nombre del juego.
    * **playtime_forever** ⏰: Tiempo acumulado de juego.
    * **playtime_2weeks** ⏰: Tiempo acumulado en las últimas dos semanas.

#### **🎯 output_steam_games.json** :

[](https://github.com/bautiarmanicode/MachineLearning-SteamGames/blob/main/00_Diccionario_de_datos.md#-output_steam_gamesjson-)

* Contiene datos relacionados con los juegos.
* Variables:
  * **publisher** 📤: Empresa publicadora del contenido.
  * **genres** 🎮: Género del juego (lista de géneros).
  * **app_name** 📜: Nombre del juego.
  * **title** 🏆: Título del juego.
  * **url** 🔗: URL del juego.
  * **release_date** 📅: Fecha de lanzamiento (formato: 2018-01-04).
  * **tags** 🏷️: Etiquetas del contenido (lista de etiquetas).
  * **reviews_url** 🔍: URL de reseñas del juego.
  * **specs** 📝: Especificaciones del juego (lista de cadenas de texto).
  * **price** 💰: Precio del juego.
  * **early_access** 🚀: Acceso temprano (True/False).
  * **id** 🔢: Identificador único del contenido.
  * **developer** 👨‍💻: Desarrollador del contenido.
