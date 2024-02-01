import requests
import os

def obtener_imagen_apod(api_key):
    
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    return data

def descargar_imagen(url, nombre_archivo):
    
    response = requests.get(url)
    response.raise_for_status()

    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(response.content)

def nasa_apod():
    clave_api = 'RKwmUXGADixrEuY9ZVCfIaRfJXwxB5tH59c642zj'
    resultado = obtener_imagen_apod(clave_api)

    if resultado:
        titulo = resultado['title']
        url_imagen = resultado['url']
        path = os.path.abspath(__file__)
        nombre_archivo = path +"NASA_pic.jpg"
        
        descargar_imagen(url_imagen, nombre_archivo)
        return {"titulo":titulo, "img_path":nombre_archivo}
    
nasa_apod()