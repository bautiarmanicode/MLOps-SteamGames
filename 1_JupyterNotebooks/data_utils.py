# Funciones utiles para ETL Y EDA
import pandas as pd
import datetime
import inspect
import re


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


def extraer_anio_release(fecha):
    '''
    Extrae el año de una fecha en formato 'yyyy-mm-dd' y maneja valores nulos.

    Esta función toma como entrada una fecha en formato 'yyyy-mm-dd' y devuelve el año de la fecha si
    el dato es válido. Si la fecha es nula o inconsistente, devuelve 'Dato no disponible'.

    Parameteros:
        fecha (str or float or None): La fecha en formato 'yyyy-mm-dd'.

    Retorna:
        str: El año de la fecha si es válido, 'Dato no disponible' si es nula o el formato es incorrecto.
    '''
    if pd.notna(fecha):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
            return fecha.split('-')[0]
    return '0000'


def filtrar_valores_letras(values):
    return [value for value in values if isinstance(value, str)]