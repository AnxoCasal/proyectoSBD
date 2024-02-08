import pandas as pd

def analizar_csv(file):
    
    df = pd.read_csv(file)
    info_campos_tipos = df.dtypes
    info_estadistica = df.describe()
    
    
    with open(file, 'w') as file:
        
        file.write("Data Types:\n")
        dtypes_str = info_campos_tipos.to_string()
        file.write(dtypes_str)
        file.write("\n\n")
        
        file.write("Description:\n")
        describe_str = info_estadistica.to_string()
        file.write(describe_str)
    
    return file