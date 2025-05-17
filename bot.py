from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

# Corrigido: Pegando variável de ambiente corretamente
TOKEN = os.getenv("8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ")
bot = Bot(token=TOKEN)

app = Flask(__name__)

# Dispatcher
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

# Comando /start
def start(update, context):
    update.message.reply_text("Bot ativo via webhook!")

dispatcher.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

# Para testes locais
if __name__ == "__main__":
    app.run(debug=True)
