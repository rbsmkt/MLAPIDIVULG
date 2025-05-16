from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)  # 👈 Isso é essencial para o gunicorn encontrar

# Dispatcher configurado para funcionar via webhook
from telegram.ext import Dispatcher

dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

# Comandos
def start(update, context):
    update.message.reply_text("Bot ativo via webhook!")

dispatcher.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200
