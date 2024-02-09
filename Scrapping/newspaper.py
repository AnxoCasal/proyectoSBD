import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def scrapping_voz_galicia(amount):

    url_origen = 'https://www.lavozdegalicia.es/'
    paxina = requests.get(url_origen)
    soup = BeautifulSoup(paxina.content, 'html.parser')

    noticias = []

    for element in soup.find_all("h4","a-min-headline"):
        titular = element.text.strip()
        url = element.find_all("a")[0].get("href")
        noticias.append({"titular":titular,"url":url_origen+url})
        if len(noticias) >= amount:
            break
        
    return noticias