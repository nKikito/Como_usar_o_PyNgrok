from pyngrok import ngrok
import time

# Establish connectivity
ngrok.set_auth_token(seu_auth_token)
url = ngrok.connect(porta, protocolo_comunicacao)

# Output ngrok url to console
print(f"Link da sua aplicação {url.public_url}")

# Keep the listener alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Fechando a comunicação")