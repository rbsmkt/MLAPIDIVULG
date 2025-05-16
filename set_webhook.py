import requests
import os

# Pegue o token da variável de ambiente ou coloque direto (menos seguro)
TOKEN = os.getenv("TELEGRAM_TOKEN", "8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ")

# Seu domínio no Render (sem barra no final)
RENDER_URL = "https://seu-app-no-render.onrender.com"

# Define a URL completa do webhook
WEBHOOK_URL = f"{RENDER_URL}/{TOKEN}"

# Chamada para definir o webhook
response = requests.get(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook",
    params={"url": WEBHOOK_URL}
)

# Resultado
if response.status_code == 200:
    print("✅ Webhook configurado com sucesso!")
    print(response.json())
else:
    print("❌ Erro ao configurar webhook:")
    print(response.text)
