import requests

def get_chiste():
    
    url = "https://v2.jokeapi.dev/joke/Any?lang=es"    

    try:
        response = requests.get(url)
        response.raise_for_status()

        datos = response.json()
        return datos
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

def chiste_api():
    
    data = get_chiste()
    
    if data:
        if "joke" in data.keys():
            return (data["joke"])
        else:
            return data["setup"] +"\r\n"+ data["delivery"]