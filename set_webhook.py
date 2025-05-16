import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega as variáveis do ambiente
TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")  # exemplo: https://meuapp.onrender.com

if not TOKEN or not RENDER_URL:
    raise ValueError("❌ TELEGRAM_TOKEN ou RENDER_URL não definidos no .env")

# Define o endpoint do webhook
WEBHOOK_URL = f"{RENDER_URL}/{TOKEN}"

# Faz a requisição para o Telegram
response = requests.get(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook",
    params={"url": WEBHOOK_URL}
)

# Mostra o resultado
if response.status_code == 200:
    print("✅ Webhook configurado com sucesso!")
    print(response.json())
else:
    print("❌ Erro ao configurar webhook:")
    print(response.text)
