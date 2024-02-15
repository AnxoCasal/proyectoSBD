import requests
import os
from dotenv import load_dotenv

def obtener_imagen_apod(api_key):
    
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    return data

def nasa_apod():
    load_dotenv
    TOKEN = os.getenv("API_NASA")    
    clave_api = API_NASA
    resultado = obtener_imagen_apod(clave_api)

    if resultado:
        return {"titulo":resultado['title'], "img_path":resultado['url'], "explanation":resultado["explanation"]}