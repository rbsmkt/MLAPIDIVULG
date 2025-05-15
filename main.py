import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

app = Flask(__name__)

TOKEN = "8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# exemplo de comando
def start(update, context):
    update.message.reply_text("Bot está funcionando!")

dispatcher.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
