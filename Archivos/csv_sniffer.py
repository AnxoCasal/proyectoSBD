import pandas as pd

def analizar_csv(analizar_csv):
    df = pd.read_csv(analizar_csv)
    info_campos_tipos = df.dtypes
    info_estadistica = df.describe()
    return info_campos_tipos, info_estadistica

print(analizar_csv("/home/anxocasal/proyectoSBD/biostats.csv"))