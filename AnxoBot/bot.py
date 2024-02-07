import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/AnxoBot')

from bot_actions import *
from bot_consts import *
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, filters, CallbackQueryHandler

def launch_bot():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")    

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await show_menu(update, context, start_menu["title"], start_menu["buttons"])

    async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        opcion_seleccionada = query.data
        
        await clear_screen(update, context)

        if opcion_seleccionada == 'apis_menu':
            await show_menu(update, context, apis_menu["title"], apis_menu["buttons"])
            
        elif opcion_seleccionada == 'files_menu':
            await show_menu(update, context, files_menu["title"], files_menu["buttons"])
            
        elif opcion_seleccionada == 'scrapping_menu':
            await show_menu(update, context, scrapping_menu["title"], scrapping_menu["buttons"])
            
        elif opcion_seleccionada == 'nasa_apod':
            await bot_do_apod(update, context)
            
        elif opcion_seleccionada == 'chistes_api':
            await bot_do_joke(update, context)
        
        elif opcion_seleccionada == 'tiempo_api':
            await show_menu_type_2(update, context, start_menu["title"], ciudades_menu_left["buttons"], ciudades_menu_right["buttons"])
        
        elif opcion_seleccionada in ciudades:
            await bot_do_tiempo(update, context, opcion_seleccionada)
        
        elif opcion_seleccionada == 'dnd_adventure':
            await bot_do_dnd_intro(update, context)
        
        elif opcion_seleccionada == 'dnd_weapon':
            await bot_do_dnd_weapon(update, context)
        
        elif opcion_seleccionada == 'dnd_magic':
            await bot_do_dnd_spell(update, context)
        
        elif opcion_seleccionada == 'news_scrap':
            await bot_do_news(update, context)
        
        elif opcion_seleccionada == 'cinema_scrap':
            await bot_do_cinema(update, context)
        
        elif opcion_seleccionada == 'market_scrap':
            await bot_do_market(update, context)
        
        elif opcion_seleccionada == 'file_conversor':
            await bot_do_converter(update, context)
        
        elif opcion_seleccionada == 'file_info':
            await bot_do_sniffer(update, context)
        
        elif opcion_seleccionada == 'go_back':
            await show_menu(update, context, start_menu["title"], start_menu["buttons"])

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    button_handler = CallbackQueryHandler(button_callback)
    application.add_handler(button_handler)

    print("Launch")
    application.run_polling()

launch_bot()