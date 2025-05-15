from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Envie um link do Mercado Livre para começar.")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if "mercadolivre.com.br" in text:
        update.message.reply_text(f"Você mandou um link do Mercado Livre: {text}")
    else:
        update.message.reply_text("Envie um link válido do Mercado Livre.")
