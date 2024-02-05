def scrapping_cines_norte():
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import json

    url = 'https://www.granviacines.com/peliculas/cartelera'
    paxina = requests.get(url)
    soup = BeautifulSoup(paxina.content, 'html.parser')

    peliculas = []

    for element in soup.find_all("h3"):
        titular = element.text.strip()
        url = element.find_all("a")[0].get("href")
        peliculas.append({"titular":titular,"url":url})
        
    return peliculas