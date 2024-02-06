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
from dnd import dnd_minigame
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, filters, CallbackQueryHandler


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

async def bot_do_apod(update: Update, context: ContextTypes.DEFAULT_TYPE):

    extra_msg = []

    data = nasa_apod()
    titulo = await context.bot.send_message(chat_id=update.effective_chat.id, text=data["titulo"])
    photo = await context.bot.send_photo(chat_id=update.effective_chat.id, photo=data["img_path"])
    extra_msg.append(titulo.message_id)
    extra_msg.append(photo.message_id)
    await show_menu(update, context, data["explanation"], back_menu["buttons"], extra_messages=extra_msg)
    
async def bot_do_dnd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    history = dnd_minigame()
    await show_menu(update, context, history["start"], dnd_menu["buttons"])
    
async def bot_do_tiempo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ...
    
async def bot_do_chistes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ...