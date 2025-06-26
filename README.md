# Como usar o PyNgrok

## Índices

## Introdução
Este repositório mostra como colocar a sua aplicação no 'ar' com o pyngrok. O pyngrok é uma biblioteca python que facilita o uso da ferramenta ngrok, já que com a biblioteca não é necessário baixar o ngrok, só ter o seu _auth token_. O ngrok é uma ferramenta "transforma" o seu computador em um servidor e te dá um link temporário onde você e outras pessoas conseguem usar a sua aplicação através de algum navegador.

## Baixando o pyngrok
Primeiro, você deve ter o python instalado em sua máquina para baixar a biblioteca (se você não tem o python baixado clique [aqui](https://www.python.org/)). Agora, vamos criar um ambiente virtual para garantir que nenhum conflito aconteça, para isso abra o CMD (Prompt de comando) e insira o comando: `python -m venv nome_do_seu_ambiente_virtual`. Depois disso vamos ativar o ambiente virtual, se você estiver no Windows insira o comando: `cd nome nome_do_seu_ambiente_virtual\Scripts` e depois: `activate` . Se você não estiver no Windows insira o comando: `source nome_do_seu_ambiente_virtual/bin` e depois: `activate` . Agora que já iniciamos o ambiente podemos baixar a biblioteca usando o comando: `pip install pyngrok` .

## Copiando o token
Entre nesse site da [ngrok](https://dashboard.ngrok.com/get-started/your-authtoken) se cadastre e clique em _copy_ para copiar seu Authtoken.

## Método 1: Usar o CMD (Prompt de comando)
Abra o seu CMD e ative o seu ambiente virtual, da mesma forma que você ativou quando estava baixando o pyngrok, e insira o comando: `ngrok config add-authtoken seu_token` (o seu_token é o token que você copiou após ter se logado no site da ngrok). Depois que já estiver concluído é só colocar ngrok + protocolo de comunicação + porta onde a aplicação está rodando. Ex: `ngrok http 80`. Depois disso copie o link que está depois de forwarding. O local onde vai aparecer o link está em amarelo. ![](Imagens/url.png)
É só colocar esse link em um navegador e você poderá utilizar a sua aplicação.

## Método 2: Usar um arquivo python
Crie um arquivo .py e insira o código:
```python
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
```
seu_auth_token é o token que você copiou do site da ngrok, a porta é a porta onde a sua aplicação está rodando Ex: 8000, protocolo_comunicacao