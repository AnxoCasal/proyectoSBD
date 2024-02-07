def scrapping_cines():
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import json

    url = 'https://www.granviacines.com/peliculas/cartelera'
    paxina = requests.get(url)
    soup = BeautifulSoup(paxina.content, 'html.parser')

    peliculas = []
    horarios = []

    for element in soup.find_all("h3"):
        titular = element.text.strip()
        url = element.find_all("a")[0].get("href")
        peliculas.append({"titular":titular,"url":url})
        
    for pelicula in soup.find_all("div", "float-left"):
        for dia in pelicula.find_all("div", "clearfix"):
            new_horarios = dia.find_all("span", "horario sesion")
            horas = ""
            for hora in new_horarios:
                horas+= (hora.text.strip()+" ")
            horarios.append(horas)
            break
        
    horas_clear = []
    
    for i in range(0,len(horarios),2):
        horas_clear.append(horarios[i])
        
    resultado = []
        
    for pelicula, horario in zip(peliculas,horas_clear):
        resultado.append({"name":pelicula["titular"],"url":pelicula["url"],"horario":horario})
            
    return resultado