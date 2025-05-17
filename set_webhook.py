import requests

TOKEN = "8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ"
URL = f"import requests

TOKEN = "8085126675:AAEC4utEtdNH1gyK_FRhdz-fgZqyirwtYCQ"
URL = f"https://mlapidivulg.onrender.com/{TOKEN}"

res = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}")
print(res.text)
/{TOKEN}"

res = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}")
print(res.text)
