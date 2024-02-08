import logging
import os
import sys

mainD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, mainD+'/APIs')
sys.path.insert(0, mainD+'/Archivos')
sys.path.insert(0, mainD+'/Scrapping')
sys.path.insert(0, mainD+'/AnxoBot')

from bot_consts import *
from nasa import nasa_apod
from dnd import dnd_master
from chistes import chiste_api
from tiempo import tiempo_api
from acciones import scrapping_acciones, lista_diccionarios_a_csv
from blockbuster import scrapping_cines
from newspaper import scrapping_voz_galicia
from csv_sniffer import analizar_csv
from file_converter import json_to_csv, csv_to_json
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, filters, CallbackQueryHandler

### MENUS

async def clear_screen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if type(context.user_data['original_message']) == list:
        for msg_id in context.user_data['original_message']:
            await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=msg_id)
    else:
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=context.user_data['original_message'])

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, title, buttons, extra_messages=None):
    keyboard = []
    for button in buttons:
        keyboard.append([InlineKeyboardButton(button["nombre"], callback_data=button["data"])])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    original_message = await context.bot.send_message(chat_id=update.effective_chat.id, text=title, reply_markup=reply_markup)
    context.user_data['original_message'] = original_message.message_id
    if extra_messages:
        extra_messages.append(original_message.message_id)
        context.user_data['original_message'] = extra_messages

async def show_menu_type_2(update: Update, context: ContextTypes.DEFAULT_TYPE, title, left_buttons, right_buttons, extra_messages=None):
    
    keyboard = []
    
    for i in range(len(left_buttons)):
        keyboard.append([InlineKeyboardButton(left_buttons[i]["nombre"], callback_data=left_buttons[i]["data"]),InlineKeyboardButton(right_buttons[i]["nombre"], callback_data=left_buttons[i]["data"])])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    original_message = await context.bot.send_message(chat_id=update.effective_chat.id, text=title, reply_markup=reply_markup)
    context.user_data['original_message'] = original_message.message_id
    if extra_messages:
        extra_messages.append(original_message.message_id)
        context.user_data['original_message'] = extra_messages

async def show_links_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, title, buttons):
    
    keyboard = []
    
    for button in buttons:
        keyboard.append([InlineKeyboardButton(button["name"], url=button['url'])])
    
    keyboard.append([InlineKeyboardButton(f"<-- Volver", callback_data="go_back")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    original_message = await context.bot.send_message(chat_id=update.effective_chat.id, text=title, reply_markup=reply_markup)
    context.user_data['original_message'] = original_message.message_id

### APIS

async def bot_do_apod(update: Update, context: ContextTypes.DEFAULT_TYPE):

    extra_msg = []

    data = nasa_apod()
    titulo = await context.bot.send_message(chat_id=update.effective_chat.id, text=data["titulo"])
    photo = await context.bot.send_photo(chat_id=update.effective_chat.id, photo=data["img_path"])
    extra_msg.append(titulo.message_id)
    extra_msg.append(photo.message_id)
    await show_menu(update, context, data["explanation"], back_menu["buttons"], extra_messages=extra_msg)
    
async def bot_do_tiempo(update: Update, context: ContextTypes.DEFAULT_TYPE, ciudad):
    
    tiempo = tiempo_api(ciudad)
    
    await show_menu(update, context, tiempo, back_menu["buttons"])
    
async def bot_do_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    joke = chiste_api()
    
    await show_menu(update, context, joke, back_menu["buttons"])
    
    ### DND
    
async def bot_do_dnd_intro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    history = dnd_master.dnd_minigame()
    await show_menu(update, context, history["start"], dnd_menu["buttons"])
    
async def bot_do_dnd_weapon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    history = dnd_master.get_book()
    await show_menu(update, context, history["weapon"], back_menu["buttons"])
    
async def bot_do_dnd_spell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    history = dnd_master.get_book()
    await show_menu(update, context, history["spell"], back_menu["buttons"])
    
### SCRAPPING
    
async def bot_do_cinema(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    peliculas = scrapping_cines()
    botones = []
    
    for pelicula in peliculas:
        botones.append({"name":f"{pelicula['name']}: {pelicula['horario']}","url":pelicula['url']})
    
    await show_links_menu(update,context,"Cartelera Cines Gran Via Vigo",botones)
    
async def bot_do_market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    data = scrapping_acciones()
    extra_msg = []
    
    file_name = "acciones.csv"
    lista_diccionarios_a_csv(data, file_name)
    
    with open(file_name, 'rb') as file:
            msg = await context.bot.send_document(chat_id=update.effective_chat.id, document=file, filename=file_name)
            
    extra_msg.append(msg.message_id)

    await show_menu(update, context, "Aqui tiene las acciones del mundo:", back_menu["buttons"], extra_messages=extra_msg)
    
async def bot_do_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    noticias = scrapping_voz_galicia(6)
    botones = []
    
    for noticia in noticias:
        botones.append({"name":noticia['titular'],"url":noticia['url']})
    
    await show_links_menu(update,context,"La Voz de Galicia",botones)
    
### FILES

async def bot_create_sniffer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await show_menu(update, context, "Suelte aqui su archivo:", back_menu["buttons"])

async def bot_create_converter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await show_menu(update, context, "Suelte aqui su archivo:", back_menu["buttons"])
    
async def dowload_file(update: Update, context: ContextTypes.DEFAULT_TYPE, path):
    
    new_file = await update.message.effective_attachment.get_file()
    await new_file.download_to_drive(custom_path=path)

async def bot_do_sniffer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await clear_screen(update, context)
    
    path = "dowloaded_file"
    await dowload_file(update, context,path)
    analizar_csv(path)
    
    extra_msg = []
    
    with open(path, 'rb') as file:
            msg = await context.bot.send_document(chat_id=update.effective_chat.id, document=file, filename=path+".txt")
            
    extra_msg.append(msg.message_id)

    await show_menu(update, context, "Aqui tiene el analisis de su archivo:", back_menu["buttons"], extra_messages=extra_msg)
    
    
async def bot_do_converter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await clear_screen(update, context)
    
    path = "dowloaded_file"
    await dowload_file(update, context,path)
    
    if update.message.document.file_name.endswith(".csv"):
        new_file = csv_to_json(path)
    elif update.message.document.file_name.endswith(".json"):
        new_file = json_to_csv(path)
    
    extra_msg = []
    
    with open(new_file, 'rb') as file:
            msg = await context.bot.send_document(chat_id=update.effective_chat.id, document=file, filename=new_file)
            
    extra_msg.append(msg.message_id)

    await show_menu(update, context, "Aqui tiene su archivo convertido:", back_menu["buttons"], extra_messages=extra_msg)
        