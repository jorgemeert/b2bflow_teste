# Desafio b2bflow - Envio de Mensagens via WhatsApp

Desafio que foi dado pela b2bflow, código simples, deixei o mais comentado possível para melhor entendimento e leitura, usei as boas práticas que estou aprenendo na faculdade! Espero que atenda as expectativas!

## Tecnologias

- Python
- Supabase (banco de dados)
- Z-API (envio de WhatsApp)

## Setup da tabela no Supabase

- ID (Supabase faz sozinho)
- nome (Nome do usuário, ou a pessoa que irá receber a mensagem!)
- telefone (telefone do usuário, precisa estar no formato E.164"DDI,DDD e o número com 9 dígitos")

## Variáveis de ambiente (.env)

- SUPABASE_URL = url do supabse
- SUPABASE_KEY = chave de acesso para o banco de dados
- ZAPI_INSTANCE_ID = numero de identicação único
- ZAPI_TOKEN = Token do Z-Api
- ZAPI_CLIENT_TOKEN = Token de segurança

## Como rodar

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Crie um arquivo `.env` com as variáveis necessárias
4. Execute: `python main.py`
