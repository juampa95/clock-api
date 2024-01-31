import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recursos.caracteres import letras
from starlette.responses import RedirectResponse



def frase(palabras):
    frase = []
    for palabra in palabras:
        for caracter in palabra:
            car = letras[caracter]
            for i in range(4):
                for j in reversed(range(8)):
                    if j < 3:
                        frase.append(0)
                    else:
                        frase.append(car[j-3][i])
            frase.extend([0, 0, 0, 0, 0, 0, 0, 0])
        frase.extend([0, 0, 0, 0, 0, 0, 0, 0])  # Agrega espacio entre palabras
    return frase


app = FastAPI()

# origin = ['*']

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origin,
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*']
# )

@app.get("/")
async def root():
    return RedirectResponse(url='/docs/')


@app.get("/obtener_matriz/{letra}")
async def obtener_matriz(letra: str):
    if letra in letras:  # Cambié 'caracteres' por 'letras'
        matriz = letras[letra]
        return {letra: matriz}
    else:
        return {"error": "Letra no encontrada"}


# @app.get("/procesar_palabras/{palabras}")
# async def procesar_palabras(palabras: str):
#     # Dividir la cadena de palabras en palabras individuales
#     palabras_lista = palabras.split()
#     # Aplicar la función 'frase' a cada palabra individual
#     resultado = frase(palabras_lista)
#     return {"resultado": resultado}

# Endpoint para procesar palabras y guardar la respuesta en un archivo JSON
@app.get("/procesar_palabras/{palabras}")
async def procesar_palabras(palabras: str):
    # Dividir la cadena de palabras en palabras individuales
    palabras_lista = palabras.split()
    # Aplicar la función 'frase' a cada palabra individual
    resultado = frase(palabras_lista)

    # Guardar la respuesta en un archivo JSON
    with open("respuesta.json", "w") as json_file:
        json.dump({"resultado": resultado}, json_file)

    return {"mensaje": "Respuesta guardada en respuesta.json"}


# Endpoint para consultar el contenido del archivo JSON
@app.get("/consultar_respuesta_json")
async def consultar_respuesta_json():
    try:
        # Leer el contenido del archivo JSON
        with open("respuesta.json", "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return {"message": "El archivo JSON no existe"}