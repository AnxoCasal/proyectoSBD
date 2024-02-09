import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def lista_diccionarios_a_csv(lista_diccionarios, nombre_archivo):
    
    encabezados = lista_diccionarios[0].keys()
    
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados)
        
        escritor_csv.writeheader()
        
        for diccionario in lista_diccionarios:
            escritor_csv.writerow(diccionario)

def scrapping_acciones():

    url = 'https://www.expansion.com/mercados/cotizaciones/indices/ibex35_I.IB.html'
    paxina = requests.get(url)
    soup = BeautifulSoup(paxina.content, 'html.parser')

    acciones = []
    
    rows = soup.find(id="listado_valores").find_all("tr")[1:]
    
    for row in rows:
        columnas = row.find_all(['th', 'td'])
        valores = [col.text.strip() for col in columnas[:-1]]
        accion = {"Empresa":valores[0],"Último":valores[1],"Var. %":valores[2],"Ac. %\ año":valores[3],"Máx.":valores[4],"Mín.":valores[5],"Vol.":valores[6],"Capit.":valores[7],"Hora":valores[8],}
        acciones.append(accion)
        
    return acciones