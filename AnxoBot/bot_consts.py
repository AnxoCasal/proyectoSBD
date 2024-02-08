start_menu = {"title":"Bienvenido! Soy AnxoBot, en que quiere que le ayude:", "buttons": [{"nombre":"API's", "data":'apis_menu'},
                                                                                            {"nombre":"Archivos", "data":'files_menu'},
                                                                                            {"nombre":"Scrapping", "data":'scrapping_menu'},
                                                                                            {"nombre":"BBDD", "data":"..."}]}

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

ciudades = ["Barcelona","Madrid","Sevilla","ValÃšncia","Bilbao","CoruÃ±a, A","Oviedo","Puerto de la Cruz","Eivissa","CÃ¡ceres","AlmerÃ­a","Cazorla"]

dnd_menu = {"title":"", "buttons":  [{"nombre":"WEAPONS", "data":'dnd_weapon'},
                                                    {"nombre":"SPELLS", "data":'dnd_magic'}]}

back_menu = {"title":"", "buttons":   [{"nombre":"<-- Volver", "data":"go_back"}]}