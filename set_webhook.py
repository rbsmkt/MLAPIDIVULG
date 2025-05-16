import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")

bot = Bot(token=TOKEN)
webhook_url = f"{RENDER_URL}/{TOKEN}"

bot.set_webhook(url=webhook_url)
print(f"Webhook set to: {webhook_url}")