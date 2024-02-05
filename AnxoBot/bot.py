import logging
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, filters, CallbackQueryHandler

def launch_bot():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    
    start_menu = {"title":"Bienvenido, soy AnxoBot. Seleccione el campo que desee:", "buttons": [{"nombre":"API's", "data":'apis_menu'},
                                                                                                {"nombre":"Archivos", "data":'files_menu'},
                                                                                                {"nombre":"Scrapping", "data":'scrapping_menu'},
                                                                                                {"nombre":"BBDD", "data":"..."}]}
    
    apis_menu = {"title":"Seleccione la API que desea consultar:", "buttons":   [{"nombre":"NASA APOD", "data":'...'},
                                                                                {"nombre":"Chistes", "data":'...'},
                                                                                {"nombre":"D&D Adventure", "data":"..."},
                                                                                {"nombre":"<-- Volver", "data":"go_back"}]}
    
    files_menu = {"title":"Seleccione la API que desea consultar:", "buttons":   [{"nombre":"Conversor de archivos", "data":'...'},
                                                                                {"nombre":"Informacion de CSV", "data":"..."},
                                                                                {"nombre":"<-- Volver", "data":"go_back"}]}
    
    scrapping_menu = {"title":"Seleccione la API que desea consultar:", "buttons":   [{"nombre":"La Voz de Galicia", "data":'...'},
                                                                                {"nombre":"Gran Via Cines", "data":'...'},
                                                                                {"nombre":"Acciones del mundo", "data":"..."},
                                                                                {"nombre":"<-- Volver", "data":"go_back"}]}
    
    
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await show_menu(update, context, start_menu["title"], start_menu["buttons"])

    async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, title, buttons):
        keyboard = []
        for button in buttons:
            keyboard.append([InlineKeyboardButton(button["nombre"], callback_data=button["data"])])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        original_message = await context.bot.send_message(chat_id=update.effective_chat.id, text=title, reply_markup=reply_markup)
        context.user_data['original_message'] = original_message.message_id

    async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        opcion_seleccionada = query.data
            
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id,
            message_id=context.user_data['original_message'],
            reply_markup=None
        )

        # Eliminar el mensaje original con los botones
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=context.user_data['original_message'])
            
        if opcion_seleccionada == 'apis_menu':
            await show_menu(update, context, apis_menu["title"], apis_menu["buttons"])
        elif opcion_seleccionada == 'files_menu':
            await show_menu(update, context, files_menu["title"], files_menu["buttons"])
        elif opcion_seleccionada == 'scrapping_menu':
            await show_menu(update, context, scrapping_menu["title"], scrapping_menu["buttons"])
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
