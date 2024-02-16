import mysql.connector

def mostrar_persoa_inferno(target):
    
    config = {
    'user': 'Anxo',
    'password': '1Super-Password',
    'host': '193.144.42.124',
    'port': '33306',
    'database': 'inferno',
    'raise_on_warnings': True
    }

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("use inferno;")

            cursor.execute(f"Select * from admision where nome=\'{target}\';")
            datos = cursor.fetchall()[0]
            return {"cod":datos[0],"Nome":datos[1],"Nivel":datos[2],"Nome_nivel":datos[3]}
    
    finally:
        if 'connection' in locals():
            connection.close()