# Importações de bibliotecas
import os
import requests
from dotenv import load_dotenv

# 1. Carrega as variáveis do .env
load_dotenv()

# 2. Guarda elas em variáveis Python
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
zapi_instance_id = os.getenv("ZAPI_INSTANCE_ID")
zapi_token = os.getenv("ZAPI_TOKEN")
zapi_client_token = os.getenv("ZAPI_CLIENT_TOKEN")

# url que leva pra o banco de dados, que está salvo os usuários.
url = supabase_url + "/rest/v1/contatos"

# headers que fica salvo com as chaves para ter acesso ao banco de dados
headers = {
    "apikey" : supabase_key,
    "Authorization" : "Bearer " + supabase_key
}
try:
    # variável que salva a resposta do chamada do banco de dados, junto a request.get que puxa as informações
    response = requests.get(url, headers=headers)

    # Caso a resposta seja positiva, retorne um sucesso
    if response.status_code == 200:
        #Váriavel que salva os resultados em um dicionário
        contatos = response.json()

    # Se não irá retornar um erro no console, e uma lista vázia para evitar o código quebrar
    else:
        print(f"Erro ao buscar contatos: {response.status_code}")
        contatos = []

#Caso haja um erro de conexção com o Supabase
except Exception as e:
    print(f"Erro de conexão: {e}")
    contatos = []


# URL da Z-api, para fazer a requisição.
zapi_url = f"https://api.z-api.io/instances/{zapi_instance_id}/token/{zapi_token}/send-text"


# Header da Z-api, identificação e o outro garante que seja em formato JSON
headers_zapi = {
    "Client-Token" : zapi_client_token,
    "Content-Type" : "application/json"
}

# for que faz a mensagem com cada nome e contato seja salva na variavel body, para enviar para o whatsapp
for contato in contatos:
    try:
        mensagem = f'Olá, {contato["nome"]} tudo bem com você?'
        body = {
            'phone' : contato["telefone"],
            'message' : mensagem
        }
        #envio da mensagem para o Z-Api, para ser enviado ao WhatsApp
        reposta_zapi = requests.post(zapi_url, headers=headers_zapi, json=body)
        #verificação de status no console
        if reposta_zapi.status_code == 200:
            print(f"mensagem para {contato['nome']} enviada com sucesso!")
        else:
            print(f"falha ao enviar a mensagem para {contato["nome"]}, {reposta_zapi.status_code}")

    #Caso tenha algum erro em algum número cadastrado
    except Exception as e:
        print(f'Erro ao enviar mensagem para {contato["nome"]} : {e}')
