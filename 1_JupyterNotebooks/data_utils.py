# Funciones utiles para ETL Y EDA
import pandas as pd
import datetime
import inspect


def data_type_check(df):
    # Create a dictionary to store the data summary
    dataframe = {"columna": [], "%_no_nulos": [], "%_nulos": [], "total_nulos": [], "tipo_dato": []}
    # Conseguir el nombre del df
    nombre_df = [nombre for nombre, var in inspect.currentframe().f_back.f_locals.items() if var is df][0]
    # Header
    print("\n" + "=" * 40)
    print(f" Resumen del dataframe '{nombre_df}': ")
    print("\n" + "=" * 40)
    for columna in df.columns:
        # Calcular el porcentaje de no nulos
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        # Obtener el tipo de dato directamente
        tipo_dato = df[columna].dtype  
        # Append la informacion a un diccionario
        dataframe["columna"].append(columna)
        dataframe["%_no_nulos"].append(round(porcentaje_no_nulos, 2))
        dataframe["%_nulos"].append(round(100 - porcentaje_no_nulos, 2))
        dataframe["total_nulos"].append(df[columna].isnull().sum())
        dataframe["tipo_dato"].append(tipo_dato)
    # Creamos el dataframe
    df_info = pd.DataFrame(dataframe)
    print("Dimensiones: ", df.shape)
    print(df_info)    

    
def verifica_duplicados(df, columna):    
    # Filter duplicated rows
    duplicated_rows = df[df.duplicated(subset=columna, keep=False)]  
    if duplicated_rows.empty:
        return "No hay duplicados"    
    # Sort duplicated rows for easy comparison
    duplicated_rows_sorted = duplicated_rows.sort_values(by=columna)
    return duplicated_rows_sorted

def analisis_sentimiento(review):
    
    if review is None:
        return 1
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    if polarity < -0.2:
        return 0
    elif polarity > 0.2:
        return 2
    else:
        return 1

   
def ej_review_sentimiento(reviews, sentiments):    
    for sentiment_value in range(3):
        print(f"En la sección de evaluación de sentimientos, se presentan los siguientes ejemplos de reseñas para {sentiment_value}:")
        sentiment_reviews = [review for review, sentiment in zip(reviews, sentiments) if sentiment == sentiment_value]        
        for i, review in enumerate(sentiment_reviews[:3], start=1):
            print(f"Reseña: {i}: {review}")        
        print("\n")


def duplicados_columna(df, columna): 
    #Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset=columna, keep=False)]
    if duplicated_rows.empty:
        return "No hay duplicados"    
    #se ordenan las filas duplicadas para comparar entre sí
    duplicated_rows_sorted = duplicated_rows.sort_values(by=columna)
    return duplicated_rows_sorted


def extraccion_fecha(cadena_fecha):    
    try:
        fecha_dt = datetime.datetime.strptime(cadena_fecha, '%B %d, %Y')
        return fecha_dt.strftime('%Y-%m-%d')
    except ValueError:
        return 'Fecha inválida'
