import os
import re
import requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()

BOT_TOKEN = os.getenv("8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ")
ML_CLIENT_ID = os.getenv("1407108334528056")
ML_CLIENT_SECRET = os.getenv("YtlxTYm01Xc6LlnzXAdsjJikZJV9lyfD")

def get_access_token():
    url = "https://api.mercadolibre.com/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": ML_CLIENT_ID,
        "client_secret": ML_CLIENT_SECRET
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()
    return response.json()["access_token"]

def extract_product_id(url):
    match = re.search(r"/(MLB\d+)", url)
    return match.group(1) if match else None

def get_product_data(product_id, token):
    url = f"https://api.mercadolibre.com/items/{product_id}?access_token={token}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Envie um link de produto do Mercado Livre.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "mercadolivre.com" not in text:
        await update.message.reply_text("Por favor, envie um link válido do Mercado Livre.")
        return

    product_id = extract_product_id(text)
    if not product_id:
        await update.message.reply_text("Não consegui extrair o ID do produto.")
        return

    try:
        token = get_access_token()
        data = get_product_data(product_id, token)

        title = data.get("title")
        price = data.get("price")
        original_price = data.get("original_price")
        permalink = data.get("permalink")
        image_url = data["pictures"][0]["url"] if data.get("pictures") else None
        installments = data.get("installments", {})

        msg = f"*{title}*\n\n"
        if original_price:
            msg += f"De R${original_price:.2f} por *R${price:.2f}*\n"
        else:
            msg += f"*R${price:.2f}*\n"

        if installments:
            qty = installments.get("quantity")
            amount = installments.get("amount")
            msg += f"Ou {qty}x de R${amount:.2f} sem juros\n"

        keyboard = [[InlineKeyboardButton("Compre aqui", url=permalink)]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if image_url:
            await update.message.reply_photo(photo=image_url, caption=msg, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=reply_markup)

    except Exception as e:
        await update.message.reply_text(f"Ocorreu um erro ao buscar o produto: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
