from pyngrok import ngrok

ngrok.set_auth_token(seu_auth_token)

url = ngrok.connect(porta, 'http')
print(url.public_url)
while True:
    pass