start_menu = {"title":"Bienvenido, soy AnxoBot. Seleccione el campo que desee:", "buttons": [{"nombre":"API's", "data":'apis_menu'},
                                                                                            {"nombre":"Archivos", "data":'files_menu'},
                                                                                            {"nombre":"Scrapping", "data":'scrapping_menu'},
                                                                                            {"nombre":"BBDD", "data":"..."}]}

apis_menu = {"title":"Seleccione la API que desea consultar:", "buttons":   [{"nombre":"NASA APOD", "data":'nasa_apod'},
                                                                            {"nombre":"Chistes", "data":'...'},
                                                                            {"nombre":"D&D Adventure", "data":"dnd_adventure"},
                                                                            {"nombre":"<-- Volver", "data":"go_back"}]}

files_menu = {"title":"Seleccione la API que desea consultar:", "buttons":   [{"nombre":"Conversor de archivos", "data":'...'},
                                                                            {"nombre":"Informacion de CSV", "data":"..."},
                                                                            {"nombre":"<-- Volver", "data":"go_back"}]}

scrapping_menu = {"title":"Seleccione la API que desea consultar:", "buttons":   [{"nombre":"La Voz de Galicia", "data":'...'},
                                                                            {"nombre":"Gran Via Cines", "data":'...'},
                                                                            {"nombre":"Acciones del mundo", "data":"..."},
                                                                            {"nombre":"<-- Volver", "data":"go_back"}]}

dnd_menu = {"title":"", "buttons":  [{"nombre":"WEAPONS", "data":'dnd_weapon'},
                                                    {"nombre":"SPELLS", "data":'dnd_magic'}]}

back_menu = {"title":"", "buttons":   [{"nombre":"<-- Volver", "data":"go_back"}]}