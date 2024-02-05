def scrapping_voz_galicia(amount):
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import json

    url = 'https://www.lavozdegalicia.es/'
    paxina = requests.get(url)
    soup = BeautifulSoup(paxina.content, 'html.parser')

    noticias = []

    for element in soup.find_all("h4","a-min-headline"):
        titular = element.text.strip()
        url = element.find_all("a")[0].get("href")
        noticias.append({"titular":titular,"url":url})
        if len(noticias) >= amount:
            break
        
    return noticias