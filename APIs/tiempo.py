import requests

def obtener_datos_meteorologicos():
    
    url = "https://www.el-tiempo.net/api/json/v2/home"    

    try:
        response = requests.get(url)
        response.raise_for_status()

        datos = response.json()
        return datos
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

def tiempo_api(target):
    
    data = obtener_datos_meteorologicos()
    
    if data:
        for ciudad in data["ciudades"]:
            if target == ciudad["name"]:
                nombre = ciudad["name"]
                cielo = ciudad["stateSky"]["description"]
                maxT = ciudad["temperatures"]["max"]
                minT = ciudad["temperatures"]["min"]
                
                return f"En {nombre} tienen unas temperaturas entre ({maxT} - {minT})Cº y un cielo: {cielo}"