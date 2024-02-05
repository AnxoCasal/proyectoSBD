def scrapping_acciones(amount):
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import json

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
        if len(acciones) >= amount:
            break
        
    return acciones