from pyngrok import ngrok
import time

# Estabiliza a conexão
ngrok.set_auth_token(seu_auth_token)
url = ngrok.connect(porta, protocolo_comunicacao)

# Mostra url no terminal
print(f"Link da sua aplicação {url.public_url}")

# Mantém a url funcionando
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Fechando a comunicação")
