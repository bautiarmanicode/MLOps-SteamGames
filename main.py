import importlib

import funciones_api_viejas as fa

importlib.reload(fa)

# import ML_itemxitem as ML
#importlib.reload(ML)


from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

# Invocamos FastAPI

app = FastAPI()
@app.get("/")
def index():
    return {"message" : "Hello, world!"}


# Desarrollador
#
#
@app.get('/desarrollador', 
         description="""
    <font color="blue">
        INSTRUCCIONES<br>
        1. Haga clic en "Try it out".<br>
        2. Ingrese el X en el cuadro de abajo.<br>
        3. Desplácese hacia "Resposes" para ver x que tiene el mismo.
    </font>
""", 
tags=["Consultas Generales"])
def desarrollador(genero: str = Query(..., 
                                   title="Desarrollador del videojuego", 
                                  description="Desarrolladores para consultar:   .... ",
                                 examples="Valve")):    
    desarrolladorx = fa.desarrollador(genero)
    return desarrolladorx

'''

## userdata

@app.get('/userdata',
         description="""
    <font color="blue">
        INSTRUCCIONES<br>        
        1. Haga clic en "Try it out".<br>
        2. Ingrese el id del usuario en el cuadro de abajo.<br>
        3. Desplácese hacia "Resposes" para ver el dinero gastado por el usuario, porcentaje de recomendación y cantidad de items.
    </font>
""", tags=["Consultas Generales"])
def userdata(anio: int = Query(..., 
                                        title="User_ID",
                                        description="Ingresa el ID para la consulta",
                                        examples=420)):
    usersdata = fa.userdata(anio)
    return usersdata



## `UserForGenre`


@app.get('/UserForGenre', 
         description="""
    <font color="blue">
        INSTRUCCIONES<br>
        1. Haga clic en "Try it out".<br>
        2. Ingrese el género en el cuadro de abajo.<br>
        3. Desplácese hacia "Resposes" para ver el usuario con más horas jugadas para el género dado y acumulación de horas jugadas por año de lanzamiento. 
    </font>
""", 
tags=["Consultas Generales"])
def UserForGenre(genero: str = Query(..., 
                                   title="Género del videojuego", 
                                  description="Géneros para consultar:Action, Adventure, Audio Production, Casual, Design & Illustration, Education, Indie, Massively Multiplayer, Photo Editing, RPG, Racing, Simulation, Software Training, Sports, Strategy, Utilities, Video Production",
                                 examples="Action")):    
    UserForGenree = fa.UserForGenre(genero)
    return UserForGenree

'''


## `best_developer_year`




## `developer_reviews_analysis`
'''
@app.get('/developer_reviews_analysis', 
         description="""
    <font color="blue">
        INSTRUCCIONES<br>
        1. Haga clic en "Try it out".<br>
        2. Ingresa la empresa desarrolladora en el cuadro de abajo.<br>
        3. Desplácese hacia "Resposes" para ver devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total
de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
    </font>
""", tags=["Sentiment Analysis"])
async def developer_reviews_analysis(empresa_desarrolladora: str =Query (..., 
                                    title="Empresa desarrolladora",
                                    description="Algunas empresas para consultar: Dovetail Games,Paradox Development Studio,Capcom,Choice of Games, Stainless Games",
                                    )):
    sent = fa.developer_reviews_analysis(empresa_desarrolladora)
    return sent

'''

'''

#recomendacion_juego

@app.get('/recomendacion_juego', 
           description="""
    <font color="blue">
        INSTRUCCIONES<br>
        1. Haga clic en "Try it out".<br>
        2. Ingrese el item_id del juego a partir del cual se hace la recomendación de otros juegos #en el cuadro de abajo.<br>
        3. Desplácese hacia "Resposes" para ver la cantidad de dinero gastado por el usuario, el porcentaje de recomendación que realiza el usuario y la cantidad de items que tiene el mismo.
    </font>
""", tags=["Machine Learning ITEM x ITEM"])
async def recomendacion_juego(item_id: int =Query (...,
                                            title="Item ID",
                                            description="Ingrese el ID del juego para obtener recomendaciones. Por ejemplo: 10,20,500",
                                            examples=123)):
    reco = ML.recomendacion_juego(item_id) 
    return reco
    
    
'''
