from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = '8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ'
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler('start', lambda update, context: update.message.reply_text("Olá!")))
