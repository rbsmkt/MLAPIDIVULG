from telegram import Bot

TOKEN = "8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ"
WEBHOOK_URL = f"https://telegram-ml-bot-production.up.railway.app/{TOKEN}"

bot = Bot(token=TOKEN)
bot.set_webhook(url=WEBHOOK_URL)

print("Webhook configurado com sucesso!")
