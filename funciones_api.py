## FUNCIONES A UTILIZAR EN app.py


# Importaciones
import pandas as pd
import gc
import time 
from typing import List, Tuple,Dict
#Asigmanos el parquet a distintos df con los que vamos a trabajar


#developer
df_dev = pd.read_parquet("./0 Dataset/f_df_funciones.parquet")
#userdata
df_userdata = pd.read_parquet("./0 Dataset/F_df_funciones.parquet")                    
#UserForGenre
df_UserForGenre = pd.read_parquet("./0 Dataset/F_df_funciones.parquet")                    
# best_developer_year
df_best_developer_year = pd.read_parquet("./0 Dataset/F_df_funciones.parquet")                    
#developer_reviews_analysis
funcion5 = pd.read_parquet("./0 Dataset/F_df_funciones.parquet")                    


# ________________________________________________________
# DEVELOPER
def developer(desarrollador)
        start_time = time.time()  # Registro del tiempo de inicio
        
        
        # Filtrar por desarrollador
        df_dev = df_steam_games[df_steam_games['developer'] == desarrollador]
        # Obtener la cantidad de ítems por año
        items_por_anio = df_dev.groupby('release_date').size()
        
        # Obtener la cantidad de ítems gratuitos por año
        gratis_por_anio = df_dev[df_dev['price'] == 0].groupby('release_date').size()
        # Calcular el porcentaje de contenido gratuito por año
        porcentaje_gratis_por_anio = (gratis_por_anio / items_por_anio * 100).round(0)
        # Reemplazar valores NaN en "Contenido Gratuito" con "0%"
        porcentaje_gratis_por_anio = porcentaje_gratis_por_anio.fillna(0)
        
        ###
        end_time = time.time()  # Registro del tiempo de finalización
        response_time = end_time - start_time  # Cálculo del tiempo de respuesta
        
        # Liberar memoria utilizando el recolector de basura
        gc.collect()    
                    
        resultado = {
            "Año": porcentaje_gratis_por_anio.index,
            "Contenido Gratuito (%)": porcentaje_gratis_por_anio.values,
            "Tiempo de respuesta": f"{response_time} segundos"
        }
        
        return resultado

# ________________________________________________________
# 

