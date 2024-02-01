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

def main():
    clave_api = 'RKwmUXGADixrEuY9ZVCfIaRfJXwxB5tH59c642zj'
    resultado = obtener_imagen_apod(clave_api)

    if resultado:
        titulo = resultado['title']
        url_imagen = resultado['url']
        nombre_archivo = "NASA_pic.jpg"

        print(titulo)
        descargar_imagen(url_imagen, nombre_archivo)
        
main()