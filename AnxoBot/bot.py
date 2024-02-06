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
        
        if type(context.user_data['original_message']) == list:
            for msg_id in context.user_data['original_message']:
                await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=msg_id)
        else:
            await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=context.user_data['original_message'])
            
        if opcion_seleccionada == 'apis_menu':
            await show_menu(update, context, apis_menu["title"], apis_menu["buttons"])
        elif opcion_seleccionada == 'files_menu':
            await show_menu(update, context, files_menu["title"], files_menu["buttons"])
        elif opcion_seleccionada == 'scrapping_menu':
            await show_menu(update, context, scrapping_menu["title"], scrapping_menu["buttons"])
        elif opcion_seleccionada == 'nasa_apod':
            await bot_do_apod(update, context)
        elif opcion_seleccionada == 'dnd_adventure':
            await bot_do_dnd(update, context)
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