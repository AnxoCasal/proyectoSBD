# Bot de Telegram Multiusos

Este es un bot de Telegram multiusos creado en python.
Este tiene diversas funcionalidades relacionadas con:
- Apis
- Scrapping Web
- Bases de datos
- Archivos Json y CSV

Toda la interaccion del bot es a base de menús con botones y el único comando por teclado es /start, con el que se muestra el menú principal.

Para su correcto uso es necesario crear un archivo .env para añadir una clave de bot de Telegram con el nombre de "TOKEN" y otra del APOD de la NASA con el nombre de API_NASA.

Se recomienda usar Conda para la instalación de librerias o Docker para la creacion de un contenedor que ejecute el Programa.

![Menu de inicio](https://github.com/AnxoCasal/proyectoSBD/assets/107409500/413c4294-c21e-4144-a31f-00ef06f0a557)

## Instalación

A continuación se explica las opciones para instalar el bot:

Descarga del repositorio:
```bash
git clone https://github.com/AnxoCasal/proyectoSBD.git
```

Creación del archivo .env:
```bash
cd proyecto SBD![furrys](https://github.com/AnxoCasal/proyectoSBD/assets/107409500/a6a684d9-e76c-4842-a855-74add23a7ae5)
![Scrapping de Acciones](https://github.com/AnxoCasal/proyectoSBD/assets/107409500/ef2b9a24-4956-4d49-a319-afd2ad067fd2)
![La voz de Galicia](https://github.com/AnxoCasal/proyectoSBD/assets/107409500/56458d9e-35da-4623-89b6-8460ce60fcc4)
![Menu de inicio](https://github.com/AnxoCasal/proyectoSBD/assets/107409500/d5c559b3-1a61-4330-b682-7269de5fbcbb)

echo "TOKEN = \"TU TOKEN DE TELEGRAM\"" > .env
echo "API_NASA = \"TU TOKEN DE NASA APOD\"" >> .env
```

En caso de ejecutar en local:
```bash
conda env create -f environment.yml
python3 AnxoBot/bot.py
```

En caso de usar Docker:
```bash
docker build -t Anxo_Bot .
docker run -d Anxo_Bot
```
![Scrapping de Acciones](https://github.com/AnxoCasal/proyectoSBD/assets/107409500/47fa6fc0-e1e2-4540-94ec-0d2da7771808)
![La voz de Galicia](https://github.com/AnxoCasal/proyectoSBD/assets/107409500/0a6fae82-bbc3-43e9-95d4-be4818d06cef)
