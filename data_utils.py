# Funciones utiles para ETL Y EDA
import pandas as pd
import datetime


def data_type_check(df):
    # Create a dictionary to store the data summary
    data_types = {"columna": [], "%_no_nulos": [], "%_nulos": [], "total_nulos": [], "tipo_dato": []}
    # Header
    print("\n" + "=" * 40)
    print(" Resumen del Dataframe ")
    print("=" * 40)
    for columna in df.columns:
        # Calculate the percentage of non-null values
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        # Obtain the data type directly
        tipo_dato = df[columna].dtype  
        # Append information to the dictionary
        data_types["columna"].append(columna)
        data_types["%_no_nulos"].append(round(porcentaje_no_nulos, 2))
        data_types["%_nulos"].append(round(100 - porcentaje_no_nulos, 2))
        data_types["total_nulos"].append(df[columna].isnull().sum())
        data_types["tipo_dato"].append(tipo_dato)
    # Create the DataFrame
    df_info = pd.DataFrame(data_types)
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
