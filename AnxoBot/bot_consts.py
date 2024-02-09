## ARCHIVO PARA GUARDAR CONSTANTES: MENUS Y LISTAS DE ELEMENTOS

start_menu = {"title":"Bienvenido! Soy AnxoBot, en que quiere que le ayude:", "buttons": [{"nombre":"API's", "data":'apis_menu'},
                                                                                            {"nombre":"Archivos", "data":'files_menu'},
                                                                                            {"nombre":"Scrapping", "data":'scrapping_menu'},
                                                                                            {"nombre":"BBDD", "data":"bbdd"}]}

apis_menu = {"title":"Seleccione la API que desea consultar:", "buttons":   [{"nombre":"D&D Adventure", "data":"dnd_adventure"},
                                                                            {"nombre":"NASA APOD", "data":'nasa_apod'},
                                                                            {"nombre":"Chistes", "data":'chistes_api'},
                                                                            {"nombre":"Clima", "data":"tiempo_api"},
                                                                            {"nombre":"<-- Volver", "data":"go_back"}]}

files_menu = {"title":"Seleccione la funcion que desea utilizar:", "buttons":   [{"nombre":"JSON <-> CSV", "data":'file_conversor'},
                                                                            {"nombre":"Informacion de CSV", "data":"file_info"},
                                                                            {"nombre":"<-- Volver", "data":"go_back"}]}

scrapping_menu = {"title":"Seleccione la WEB que desea consultar:", "buttons":   [{"nombre":"La Voz de Galicia", "data":'news_scrap'},
                                                                            {"nombre":"Gran Via Cines", "data":'cinema_scrap'},
                                                                            {"nombre":"Acciones del mundo", "data":"market_scrap"},
                                                                            {"nombre":"<-- Volver", "data":"go_back"}]}

ciudades_menu_left = {"title":"Seleccione la ciudad que desea consultar:", "buttons":   [{"nombre":"Barcelona", "data":'Barcelona'},
                                                                            {"nombre":"Madrid", "data":'Madrid'},
                                                                            {"nombre":"Sevilla", "data":"Sevilla"},
                                                                            {"nombre":"Bilbao", "data":'Bilbao'},
                                                                            {"nombre":"A Coruña", "data":"CoruÃ±a, A"},
                                                                            {"nombre":"Valencia", "data":"ValÃšncia"}]}

ciudades_menu_right = {"title":"Seleccione la ciudad que desea consultar:", "buttons":   [{"nombre":"Oviedo", "data":'Oviedo'},
                                                                            {"nombre":"Puerto de la Cruz", "data":'Puerto de la Cruz'},
                                                                            {"nombre":"Ibiza", "data":"Eivissa"},
                                                                            {"nombre":"Cáceres", "data":'CÃ¡ceres'},
                                                                            {"nombre":"Almeria", "data":"AlmerÃ­a"},
                                                                            {"nombre":"Cazorla", "data":"Cazorla"}]}

condenados_menu_left = {"title":"Seleccione el condenado que desea consultar:", "buttons":     [{"nombre":"Misaki", "data":'Misaki'},
                                                                                                {"nombre":"Vanesa", "data":'Vanesa'},
                                                                                                {"nombre":"Anxo", "data":"Anxo"},
                                                                                                {"nombre":"Martín", "data":'Martín'},
                                                                                                {"nombre":"Carla", "data":"Carla"},
                                                                                                {"nombre":"Iván", "data":'Iván'},
                                                                                                {"nombre":"Alejandro", "data":"Alejandro"},
                                                                                                {"nombre":"Javier", "data":'Javier'},
                                                                                                {"nombre":"Óscar", "data":"Óscar"},
                                                                                                {"nombre":"Maite", "data":"Maite"}]}

condenados_menu_right = {"title":"Seleccione el condenado que desea consultar:", "buttons":     [{"nombre":"Pedro", "data":'Pedro'},
                                                                                                {"nombre":"Andrea", "data":'Andrea'},
                                                                                                {"nombre":"Pablo", "data":"Pablo"},
                                                                                                {"nombre":"Iago", "data":'Iago'},
                                                                                                {"nombre":"Pedro", "data":"Pedro"},
                                                                                                {"nombre":"Nerea", "data":'Nerea'},
                                                                                                {"nombre":"Pana", "data":"Pana"},
                                                                                                {"nombre":"José Manuel", "data":'José Manuel'},
                                                                                                {"nombre":"Marcos", "data":"Marcos"},
                                                                                                {"nombre":"Iago", "data":"Iago"}]}

dnd_menu = {"title":"", "buttons":  [{"nombre":"WEAPONS", "data":'dnd_weapon'},
                                                    {"nombre":"SPELLS", "data":'dnd_magic'}]}

back_menu = {"title":"", "buttons":   [{"nombre":"<-- Volver", "data":"go_back"}]}

ciudades = ["Barcelona","Madrid","Sevilla","ValÃšncia","Bilbao","CoruÃ±a, A","Oviedo","Puerto de la Cruz","Eivissa","CÃ¡ceres","AlmerÃ­a","Cazorla"]

condenados = ['Misaki','Vanesa','Anxo','Martín','Carla','Iván','Alejandro','Javier','Óscar','Maite','Pedro','Andrea','Pablo','Iago','Pedro','Nerea','Pana','José Manuel','Marcos','Iago']